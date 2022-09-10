import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

headers = {
    "User-Agernt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}


def get_pages(num_pages):
    all_urls = []
    for page in range(num_pages):
        url = f"https://quotes.toscrape.com/page/{page}/"
        all_urls.append(url)

    return all_urls


def extract_data(all_urls):
    for url in all_urls:
        re = requests.get(url, headers=headers).text
        soup = BeautifulSoup(re, "lxml")
        books = soup.find_all("div", class_="quote")
        for book in books:
            title = book.find("span", class_="text").text
            author = book.find("small", class_="author").text
            tag = [i.text for i in book.find_all("a", class_="tag")]
            book = {"title": title, "author": author, "tags": tag}
            all_books_data.append(book)


if __name__ == "__main__":

    all_books_data = []

    all_urls = get_pages(5)
    extract_data(all_urls)
    y = json.dumps(all_books_data)
    with open("books.json", "w") as f:
        f.write(y)

    # df = pd.DataFrame(all_books_data)
    # df.to_json("data.json")
