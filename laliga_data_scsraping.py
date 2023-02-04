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

def slice_div(div):
    total_matches = div[:20]
    home_matches = div[20:40]
    away_matches= div[40:60]
    return total_matches, home_matches, away_matches


def extract_total_mataches_data(total_matches):
    all_teams = []
    for t in total_matches:
        # print(f'div {g} is scraping')
        all_p = t.find_all('p')
        scores = []
        for i in all_p:
            scores.append(i.text)
        position = scores[0]
        team = scores[2]
        points = scores[3]
        pls = scores[4]
        w = scores[5]
        d = scores[6]
        l = scores[7]
        gf = scores[8]
        fa = scores[9]
        gd = scores[10]
    
        team = {
            "position": position,
            "team": team,
            'points': points,
            'pld': pls,
            'W': w,
            'D': d,
            'L': l,
            'GF': gf,
            'GA': fa,
            'GD': gd
        }

        all_teams.append(team)
    return all_teams



if __name__ == "__main__":
    div = get_html(url)
    total_matches,home_matches,away_matches = slice_div(div)
    print(extract_total_mataches_data(total_matches))


