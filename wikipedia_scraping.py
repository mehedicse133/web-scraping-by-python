import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agernt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}


url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
def get_page(url):   
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

def extract_data(soup):
    table = soup.find('table',class_='wikitable sortable jquery-tablesorter')
    
    print(table)


def save_data(data):
    pass

def main():  
    soup = get_page(url)
   
    data = extract_data(soup)
    save_data(data)


if __name__=="__main__":
    main()