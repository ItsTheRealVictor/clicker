from bs4 import BeautifulSoup
import requests


URL = r'https://jobs.intel.com/page/show/search-results#q=engineering%20intern&t=Jobs&sort=relevancy&layout=table'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

titles = soup.find_all(id='AllResults')


print('done')
