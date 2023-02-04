import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.laliga.com/en-GB/laliga-santander/standing'

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    html = soup.find_all(
        'div', class_='styled__ContainerAccordion-e89col-11 HquGF')

    return html








