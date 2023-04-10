import requests
from bs4 import BeautifulSoup
import csv
import pandas
url = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
upc = soup.find_all("td")[0]
upc.text

title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
"number_available", "product_description" ,"category", "review_rating", "image_url"]
product_page_url = url
book_title = soup.h1.string
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(title)

    