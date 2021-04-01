from bs4 import BeautifulSoup
import requests
import pandas as pd

URL_PAYSCALE = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/'

page = 1

# Declare lists with all the data from all the pages
total_ranks_list = []
total_majors_list = []
total_early_career_pay_list = []
total_mid_career_pay_list = []
total_high_meaning_list = []

while page <= 34:

    response = requests.get(url=f"{URL_PAYSCALE}{page}")
    web_page_data = response.text

    soup = BeautifulSoup(web_page_data, 'html.parser')
    ranks = soup.find_all(name='td', class_='csr-col--rank')
    majors = soup.find_all(name='td', class_='csr-col--school-name')
    career_pays = soup.find_all(name='td', class_='csr-col--right')

    # Lists for each page to add to the total lists
    ranks_list = [rank.getText().split(':')[1] for rank in ranks]
    majors_list = [major.getText().split(':')[1] for major in majors]

    early_career_pay_list = []
    mid_career_pay_list = []
    high_meaning_list = []

    # Use for loop because it's easier to read at this case
    for pay in career_pays:
        if pay.getText().split(':')[0] == 'Early Career Pay':
            early_career_pay_list.append(pay.getText().split(':')[1])
        elif pay.getText().split(':')[0] == 'Mid-Career Pay':
            mid_career_pay_list.append(pay.getText().split(':')[1])
        elif pay.getText().split(':')[0] == '% High Meaning':
            high_meaning_list.append(pay.getText().split(':')[1])

    total_ranks_list.append(ranks_list)
    total_majors_list.append(majors_list)
    total_early_career_pay_list.append(early_career_pay_list)
    total_mid_career_pay_list.append(mid_career_pay_list)
    total_high_meaning_list.append(high_meaning_list)

    page += 1

list_to_csv = []

for i in range(33):
    for n in range(25):
        data_to_csv = []
        data_to_csv.append(total_ranks_list[i][n])
        data_to_csv.append(total_majors_list[i][n])
        data_to_csv.append(total_early_career_pay_list[i][n])
        data_to_csv.append(total_mid_career_pay_list[i][n])
        data_to_csv.append(total_high_meaning_list[i][n])

        list_to_csv.append(data_to_csv)

df = pd.DataFrame(list_to_csv,
                  columns=['Rank', 'Major', 'Early Career Pay', 'Mid-Career Pay', 'High Meaning Pay'])

df.to_csv(r'highest_paying_jobs_updated.csv', index=False)