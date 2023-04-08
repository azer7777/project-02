import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
class_name = "table table-striped"
product_information = soup.find_all("table" , class_=class_name)