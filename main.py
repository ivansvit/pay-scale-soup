from bs4 import BeautifulSoup
import requests
import pandas as pd

URL_PAYSCALE = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/'

page = 1

# Declare lists with all the data from all the pages
total_jobs = []
total_early_career_pay_list = []
total_mid_career_pay_list = []
total_high_meaning_list = []

while page <= 34:

    response = requests.get(url=f"{URL_PAYSCALE}{page}")
    web_page_data = response.text

    soup = BeautifulSoup(web_page_data, 'html.parser')
    majors = soup.find_all(name='td', class_='csr-col--school-name')
    early_career_pays = soup.find_all(name='td', class_='csr-col--right')

    # Lists for each page to add to the total lists
    majors_list = []
    early_career_pay_list = []
    mid_career_pay_list = []
    high_meaning_list = []

    for job in majors:
        majors_list.append(job.getText().split(':')[1])

    for pay in early_career_pays:
        if pay.getText().split(':')[0] == 'Early Career Pay':
            early_career_pay_list.append(pay.getText().split(':')[1])
        elif pay.getText().split(':')[0] == 'Mid-Career Pay':
            mid_career_pay_list.append(pay.getText().split(':')[1])
        elif pay.getText().split(':')[0] == '% High Meaning':
            high_meaning_list.append(pay.getText().split(':')[1])



print(len(total_majors_list))
print(len(total_early_career_pay_list))
print(len(total_mid_career_pay_list))
print(len(total_high_meaning_list))


