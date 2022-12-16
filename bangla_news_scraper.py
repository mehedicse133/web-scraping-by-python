import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

# Jugantor Scraper
def jugantor():
    url = "https://www.jugantor.com/"

    allnews = []

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    first_news = soup.find(
        "div",
        class_="card top_lead_card top_lead_card_type-2 border border-0 d-none d-sm-none d-md-block d-lg-block d-xl-block",
    )

    title =first_news.text.strip()
    link = first_news.find("a")
    link= link.get("href")

    news = {"title": title, "link": link}
    allnews.append(news)


    second = soup.find_all(
    "div", class_="col d-none d-sm-none d-md-none d-lg-block d-xl-block")
    second = [i.find("a") for i in second]
    # links = [i["href"] for i in second]
    for t in second:
        link = t["href"]
        title = t.text.strip()
        news = {"title": title, "link": link}
        allnews.append(news)
    

    third = soup.find_all("div", class_="card top_lead_card d-md-none d-lg-none d-xl-none")
    link = [i.find("a", href=True) for i in third]
    for i in link:
        link = i["href"]
        title = i.text.strip()
        news = {"title": title, "link": link}
        allnews.append(news)


    fourth = soup.find_all("div", class_="d-table-cell align-middle pr-2")
    link = [i.find("a", href=True) for i in fourth]
    for i in link[0:30]:
        link = i["href"]
        title = i.text.strip()
        news = {"title": title, "link": link}
        allnews.append(news)
    print(allnews[:10])
    return allnews    

# ManabZamin Scraper
def mzamin():
    baseurl = "https://mzamin.com/"
    url = "https://mzamin.com/paper.php"

    linkdetains = []
    all_title = []
    r =requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    dvi = soup.find_all("div", class_="col")
    titele = soup.find_all("h5", class_="card-title fw-bold")


    link = [title.find("a") for title in titele]
    for i in link[0:40]:
        all_title.append(i.text)
    link = [i["href"] for i in link]
    for i in link[0:40]:
        link = f"{baseurl}{i}"
        linkdetains.append(link)


    mz = {"title": all_title, "link": linkdetains}
    df = pd.DataFrame(mz)
    allnewses = df.to_dict(orient="record")
    print(allnewses)
    
    return allnewses


if __name__ == '__main__':
    jugantor()
    mzamin()   


