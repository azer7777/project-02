import requests
from bs4 import BeautifulSoup
import pandas
import lxml
url = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
class_name = "table table-striped"
product_information = soup.find_all("table", class_=class_name)
fd_book = pandas.read_html(url)
fd_book.remove([0])

    