from bs4 import BeautifulSoup
import requests

url = 'http://islom.uz/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
m = soup.find_all('b')

print(m)
