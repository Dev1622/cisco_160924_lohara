import requests
from bs4 import BeautifulSoup
url = 'https://www.bbc.com/'
news_res = requests.get(url)
soup = BeautifulSoup(news_res.content, 'html.parser')
headings = soup.find_all('h2')
with open('news_headings.txt','w',encoding='UTF-8') as news_file:
    for heading in headings:
        news_file.write(heading.text +'\n')

print('BBC news gathered')

