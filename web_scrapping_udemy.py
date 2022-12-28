import requests
from bs4 import BeautifulSoup
import time

print('Filtrá por skills')
familiar_skills = input('>')
print(f'Filtrando por {familiar_skills}')


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') 

def find_jobs():
    for index, job in enumerate(jobs):    
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            link = job.header.h2.a['href']
            if familiar_skills in skills: 
                with open(f'posts/{index}label.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()}')
                    f.write(f'Skills required: {skills.strip()}')
                    f.write(f'Link: {link}')  

                print('')
                
if __name__ == '__main__':
    while True: 
        find_jobs()
        time_wait = 10
        print(f'Se actualizará en {time_wait} minutos...')
        time.sleep(time_wait * 60)