import requests
from bs4 import BeautifulSoup
import csv

url_main = "http://books.toscrape.com/"
url_travel = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
header = 1

def extract_page(url):
   page = requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')
   return soup


def one_category_all_books_urls(url):
    list_url_category_books =[]
    soup = extract_page(url)
    for link in soup.select(('.product_pod a')):
        list_url_category_books.append(url_main + "catalogue/" + ((link.get('href').strip('../../../'))))
    return list_url_category_books

      
        
#list the titles
list_title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
"number_available", "product_description" ,"category", "review_rating", "image_url"]

    
    
    
def scrap_one_book_description(url_book):
        soup = extract_page(url_book)

        #create variables for the descriptions
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
        #list the desriptions
        list_description = [product_page_url, upc, book_title, price_including_tax, price_excluding_tax,
        number_available, product_description , category, review_rating, image_url]
        return list_description


def transfer_data_by_category(a, b):
    with open('data.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([header])
        for t, d in zip(a, b):
            writer.writerow([t, d])
            csv_file.close
    


for urlbook in one_category_all_books_urls(url_travel):
    scrap_book_description = scrap_one_book_description(urlbook)
    transfer_data_by_category(list_title, scrap_book_description)
    header += 1
    
