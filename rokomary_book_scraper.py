# Rokomari scraping...

import requests
from bs4 import BeautifulSoup
import pandas as pd


# list of all book links
def get_books_links(url, headers):
    booklist = []

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    book = soup.find_all("div", class_="book-list-wrapper")

    # get all book image link
    atag = [x.find("a") for x in book]
    img_src = [x.find("img") for x in atag]
    src_list = [img["data-src"] for img in img_src]

    for i in book:
        for link in i.find_all("a", href=True):
            booklist.append(baseurl + link["href"])

    return booklist, src_list


# list books_data dict
def extract_book_data(links):
    all_books_details = []

    links = links[0::2]

    for i in links:
        r = requests.get(i, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find("h1").text
        price = soup.find("span", class_="sell-price").text
        try:
            author = soup.find("p", class_="details-book-info__content-author").text
            author = author[3:]
        except:
            author = "Not define"

        try:
            rating = soup.find("div", class_="details-book-info__content-rating").text
        except:
            rating = "No reviews"

        book = {
            "title": title,
            "price": price,
        }
        all_books_details.append(book)
    return all_books_details


if __name__ == "__main__":
    # main url of roklmari book website
    baseurl = "https://www.rokomari.com/"
    name = input("Enter book name ")
    url = f"https://www.rokomari.com/search?term={name}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    links, src_list = get_books_links(url, headers)
    all_books_details = extract_book_data(links)

    df = pd.DataFrame(all_books_details)
    df["src"] = src_list
    all_books = df.to_dict(orient="record")
    print(all_books)
    # save to csv file
    # df.to_csv("rop.csv", index=False)
