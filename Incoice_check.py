from bs4 import BeautifulSoup
import requests

url = "https://invoice.etax.nat.gov.tw/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
td=soup.select('.container-fluid')[0].select('.etw-tbiggest')
special_reward = td[0].getText()
first_reward = td[1].getText()
normal_reward = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] 

while (1):
  number = input("請輸入發票號碼:")
  if(number==special_reward):
    print("恭喜您中特別獎 1000萬!\n")
    continue
  if(number==first_reward):
    print("恭喜您中特獎 200萬!\n")
    continue
  for i in normal_reward:
    if (number==i):
      print("恭喜您中頭獎 20萬\n")
      break
    if (number[-7:]==i[-7:]):
      print("恭喜您中二獎 4萬\n")
      break
    if (number[-6:]==i[-6:]):
      print("恭喜您中三獎 1萬\n")
      break
    if (number[-5:]==i[-5:]):
      print("恭喜您中四獎 4千\n")
      break
    if (number[-4:]==i[-4:]):
      print("恭喜您中五獎 1千\n")
      break
    if (number[-3:]==i[-3:]):
      print("恭喜您中六獎 兩百\n")
      break
  else:
    print("未中獎，請再接再厲～\n")
