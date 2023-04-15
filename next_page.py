import requests
from bs4 import BeautifulSoup
import csv

url_main = "http://books.toscrape.com/"
url_travel = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
url_fantasy = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"

header = 1

def extract_page(url):
   page = requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')
   return soup


def next_page(url):
    soup = extract_page(url)
    nextpage = soup.select('.next a')
    for link in nextpage:
        url_next_page = link.get('href')
    return url_next_page





def one_category_all_books_urls(url):
    list_url_category_books =[]
    soup = extract_page(url)
    for link in soup.select(('.product_pod .image_container a')):
        list_url_category_books.append(url_main + "catalogue/" + ((link.get('href').strip('../../../'))))
        
        
        
        
    return list_url_category_books





    


urlnextpage = next_page(url_fantasy)
urlnextpage
if urlnextpage == []:
    print("yes")
