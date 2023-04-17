import requests
from bs4 import BeautifulSoup
import csv
import os
import urllib3


url_main = "http://books.toscrape.com/"


#list the titles
list_title = ["product_page_url",  "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
"number_available", "product_description" ,"category", "review_rating", "image_url"]
header = 1



def extract_page(url):
   page = requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')
   return soup

def all_categories_urls(url_main):    
    list_url_categories =[]
    soup = extract_page(url_main)
    for link in soup.select(('.nav ul a')):
        list_url_categories.append(url_main + ((link.get('href').replace('../../../', ''))))
    return list_url_categories



def check_next_page(url):
    soup = extract_page(url)
    nextpage = soup.select('.next a')
    return nextpage



def next_page(url, indexurl):   
    nextpage = check_next_page(url)
    for link in nextpage:
        next_page = link.get('href')
    url_next_page = indexurl.replace("index.html", "") + next_page     
    return url_next_page



def one_category_all_books_urls(url, indexurl):
    list_url_category_books =[]
    soup = extract_page(url)
    for link in soup.select(('.product_pod .image_container a')):
        list_url_category_books.append(url_main + "catalogue/" + ((link.get('href').replace('../../../', ''))))
        
    while check_next_page(url) != []:
          nextpageurl = next_page(url, indexurl)
          soup = extract_page(nextpageurl)
          for link in soup.select(('.product_pod .image_container a')):
              list_url_category_books.append(url_main + "catalogue/" + ((link.get('href').replace('../../../', ''))))
          url = nextpageurl
                                                         
    return list_url_category_books


  
    
def scrap_one_book_description(url_book):
        soup = extract_page(url_book)

        #create variables for the descriptions
        product_page_url = url_book
        upc = (soup.find_all("td")[0]).text
        book_title = soup.h1.string
        price_including_tax = (soup.find_all("td")[2]).text
        price_excluding_tax = (soup.find_all("td")[3]).text
        number_available = (soup.find_all("td")[5]).text
        product_description = ((soup.find_all("p")[3]).text)
        category = (soup.find_all("a")[3]).text
        review_rating = soup.find('p', class_='star-rating').get('class')[1] + ' stars'
        image = (soup.find_all("img")[0])
        image_url = "books.toscrape.com"+image.get('src')
        #list the desriptions
        list_description = [product_page_url, upc, book_title, price_including_tax, price_excluding_tax,
        number_available, product_description , category, review_rating, image_url]
    
        return list_description



def category_name(url_book):
        soup = extract_page(url_book)
        categoryName = ((soup.find_all("a")[3]).text)+".csv"

        return categoryName




def create_path(file_name):
    folder_name = 'books_info'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    path = os.path.join(folder_name, file_name)
    return path


def transfer_data_by_category(path, a, b):
    with open(path, 'a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([header])
        for t, d in zip(a, b):
            writer.writerow([t, d])
            
    

for urlCategory in all_categories_urls(url_main):
    for urlBook in one_category_all_books_urls(urlCategory, urlCategory):
        scrap_book_description = scrap_one_book_description(urlBook)
        file_name = category_name(urlBook)
        path = create_path(file_name)
        transfer_data_by_category(path, list_title, scrap_book_description)
        header += 1
    header = 1



