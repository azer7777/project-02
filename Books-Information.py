import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/"
url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')

urls =[]

for link in soup.select(('.product_pod a')):
    urls.append(link.get('href'))

urls


def scrap_one_book(url_book):
    url_book = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
    page = requests.get(url_book)
    soup = BeautifulSoup(page.content, 'html.parser')


    title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
    "number_available", "product_description" ,"category", "review_rating", "image_url"]

    product_page_url = url_book
    upc = (soup.find_all("td")[0]).text
    book_title = soup.h1.string
    price_including_tax = (soup.find_all("td")[2]).text
    price_excluding_tax = (soup.find_all("td")[3]).text
    number_available = (soup.find_all("td")[5]).text
    product_description = (soup.find_all("p")[3]).text
    category = (soup.find_all("a")[3]).text
    review_rating = soup.find('p', class_='star-rating').get('class')[1] + ' stars'
    image = (soup.find_all("img")[0])
    image_url = "books.toscrape.com"+image.get('src')

    description = [product_page_url, upc, book_title, price_including_tax, price_excluding_tax,
    number_available, product_description , category, review_rating, image_url]

    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for t, d in zip(title, description):
            writer.writerow([t, d])

    