import requests
from bs4 import BeautifulSoup
import csv
url = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
class_name = "write_review"
title = soup.find-all("h1")

book_title = soup.h1.string
title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
"number_available", "product_description" ,"category", "review_rating", "image_url"]
product_page_url = soup.find("a", id_=class_name )
product_page_url

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(title)

    