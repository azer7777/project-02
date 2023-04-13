import requests
from bs4 import BeautifulSoup
import csv

url_main = "http://books.toscrape.com/"


def extract_page(url):
   page = requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')
   return soup


def one_category_all_books_urls(url_category):
    url_category_books =[]
    soup = extract_page(url_category)
    for link in soup.select(('.product_pod a')):
        url_category_books.append(url_main + "catalogue/" + ((link.get('href').strip('../../../'))))


    
def scrap_one_book(url_book):
        
        soup = extract_page(url_book)

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
        return (title, description)





def transfer_data_by_category('file_name_category'):
    with open('file_name_category', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for t, d in zip(title, description):
            writer.writerow([t, d])

    