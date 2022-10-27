import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }


    url = 'https://www.laliga.com/en-GB/laliga-santander/standing'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    div = soup.find_all('div',class_='styled__ContainerAccordion-e89col-11 HquGF')

    return div

def slice_div(div):    

    tm = div[:20]
    hm = div[20:40]
    am = div[40:60]

    return tm,hm,am

def total_mataches(tm):
    tm_teams = []
    for g in tm:
        # print(f'div {g} is scraping')
        d = g.find_all('p')
        pp = []
        for i in d:
            pp.append(i.text)
        # print(pp)    
        position = pp[0]
        team = pp[2]
        points = pp[3]
        pls = pp[4]
        w = pp[5]
        d = pp[6]
        l = pp[7]
        gf = pp[8]
        fa = pp[9]
        gd = pp[10]
        # print(position,team,points,pls,w,d,l,gf,fa,gd)
        tm = {
            "position" : position,
            "team":team,
            'points': points,
            'pls' : pls,
            'w': w,
            'd': d,
            'l': l,
            'gf': gf,
            'fa': fa,
            'gd': gd
        }

        tm_teams.append(tm)
    return tm_teams        
 
def home_matches(hm):
    tm_teams = []
    for g in hm:
        # print(f'div {g} is scraping')
        d = g.find_all('p')
        pp = []
        for i in d:
            pp.append(i.text)
        # print(pp)    
        position = pp[0]
        team = pp[2]
        points = pp[3]
        pls = pp[4]
        w = pp[5]
        d = pp[6]
        l = pp[7]
        gf = pp[8]
        fa = pp[9]
        gd = pp[10]
        # print(position,team,points,pls,w,d,l,gf,fa,gd)
        tm = {
            "position" : position,
            "team":team,
            'points': points,
            'pls' : pls,
            'w': w,
            'd': d,
            'l': l,
            'gf': gf,
            'fa': fa,
            'gd': gd
        }

        tm_teams.append(tm)
    return tm_teams  

def any_matches(am):
    any_teams = []
    for g in am:
        # print(f'div {g} is scraping')
        d = g.find_all('p')
        pp = []
        for i in d:
            pp.append(i.text)
        # print(pp)    
        position = pp[0]
        team = pp[2]
        points = pp[3]
        pls = pp[4]
        w = pp[5]
        d = pp[6]
        l = pp[7]
        gf = pp[8]
        fa = pp[9]
        gd = pp[10]
        # print(position,team,points,pls,w,d,l,gf,fa,gd)
        tm = {
            "position" : position,
            "team":team,
            'points': points,
            'pls' : pls,
            'w': w,
            'd': d,
            'l': l,
            'gf': gf,
            'fa': fa,
            'gd': gd
        }

        any_teams.append(tm)
    return any_teams  



def show_and_save_data():
    totla_teams = []
    print("what you want tt hh aa tot")
    ttt = total_mataches(tm)
    hhh = home_matches(hm)
    aaa = any_matches(am)
    for i in ttt:
        totla_teams.append(i)
    for j in hhh:
        totla_teams.append(j)
    for k in aaa:
        totla_teams.append(k) 

    usr  =  input("enter toru choines :")
    if usr == 'tt':
        print(ttt)
        tt = ttt
        df = pd.DataFrame(tt)
        df.to_excel("ttt.xlsx", index=False) 
    elif usr == 'hh':
        print(hhh)
        hh = hhh
        df = pd.DataFrame(hh)
        df.to_excel("hhh.xlsx", index=False)
    elif usr == 'aa':
        print(aaa)
        aa = aaa
        df = pd.DataFrame(aa)
        df.to_excel("aaa.xlsx", index=False)  
    elif usr == 'tot':
        print(totla_teams)
        
        df = pd.DataFrame(totla_teams)
        df.to_excel("total_teams.xlsx", index=False)    
    else:
        print("invalid input")    


div = get_data()
tm,hm,am = slice_div(div)
show_and_save_data() 






