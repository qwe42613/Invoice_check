from bs4 import BeautifulSoup

import requests

url = "https://invoice.etax.nat.gov.tw/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
td=soup.select('.container-fluid')[0].select('.etw-tbiggest')
special_reward = td[0].getText()
first_reward = td[1].getText()
print(first_reward)
