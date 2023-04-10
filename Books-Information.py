import requests
from bs4 import BeautifulSoup
import csv
import pandas
import lxml
url = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
class_name = "write_review"
title = soup.find-all("h1")


title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
"number_available", "product_description" ,"category", "review_rating", "image_url"]
fd_book = pandas.read_html(url)
fd_book[0]
product_page_url = url
book_title = soup.h1.string
universal_product_code_upc = fd_book[1]
universal_product_code_upc
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(title)

    