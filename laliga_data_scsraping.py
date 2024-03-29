import requests
from bs4 import BeautifulSoup
import pandas as pd


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

def extract_mataches_data(match_category):
    all_teams = []
    for t in match_category:
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

def save_data(data):
    total_matches_data = data[0]
    home_matches_data = data[1]
    away_matches_data = data[2]

    print('Dawolosd data into excel file....')
    print("1, for total_matches_data")
    print("2, for home_matches_data")
    print("3, for away_matches_data")
    user = input("Enter 1 or 2 or 3 ....")

    if user == '1':
        print("Save tota matches data ......")
        df = pd.DataFrame(total_matches_data)
        df.to_excel("total_matches_data.xlsx", index=False)
    elif user == '2':
        print("home_matches_data")
        df = pd.DataFrame(home_matches_data)
        df.to_excel("home_matches_data.xlsx", index=False)
    elif user == '3':
        print("away_matches_data")
        df = pd.DataFrame(away_matches_data)
        df.to_excel(" away_matches_data.xlsx", index=False)
    else:
        print("invalid input")


if __name__ == "__main__":
    url = 'https://www.laliga.com/en-GB/laliga-santander/standing'
    
    div = get_html(url)
    total_matches,home_matches,away_matches = slice_div(div)
    matches_category = [total_matches,home_matches,away_matches]
    
    all_matches_data = []
    for cat in matches_category:
        data = extract_mataches_data(cat)
        all_matches_data.append(data)

    # total_matches_data = all_matches_data[0]
    # home_matches_data = all_matches_data[1]
    # away_matches_data = all_matches_data[2]
    save_data(all_matches_data)


