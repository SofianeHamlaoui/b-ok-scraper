# Sofiane Hamlaoui
# Bismillah <3

import os
import requests
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve

# Setting headers
headers = ['User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0']
books = []
download_path = "/home/sofiane/Downloads/BOOOKZ/"


def logo():
    os.system('clear')
    print("""\033[0;31m
  ______  _ _ _       _                 _       _____                                
 |___  / | (_) |     | |               | |     / ____|                               
    / /  | |_| |__   | |__   ___   ___ | | __ | (___   ___ _ __ __ _ _ __   ___ _ __ 
   / /   | | | '_ \  | '_ \ / _ \ / _ \| |/ /  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  / /__  | | | |_) | | |_) | (_) | (_) |   <   ____) | (__| | | (_| | |_) |  __/ |   
 /_____| |_|_|_.__/  |_.__/ \___/ \___/|_|\_\ |_____/ \___|_|  \__,_| .__/ \___|_|   
                                                                     | |              
                                        \033[1;33mSofiane Hamlaoui © 2020\033[0m\033[0;31m      |_|
                                                                    \033[0m""")

def download():
    q = input("\n\033[0;35mWhich one do you want to download ? (direct Book link) : \033[0m")
    for book in books:
        if book[1] == q:
            urlretrieve(q, f'{download_path}/{book[0]}.{book[2]}')
            print("\033[0;32m-[✓]- Book Downloaded -[✓]-\033[0m")
            return
    print("\n\033[91m -[X]- Wrong url -[X]- \033[0m")
    download()

def search():
    logo()
    q = input("\033[0;35mWhat Are you looking for ? : \033[0m")
    url = "https://b-ok.cc/s/" + q
    req = Request(url)
    req.add_header(headers[0],headers[1]) 
    content = urlopen(req).read()
    soup = BeautifulSoup(content, 'html.parser')
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
        nbx = nb.replace("(", "").replace(")", "")
    print("\n\033[1;33mThere Are " + nbx + " Books about " + q + " :\033[0m\n")
for tr in soup.find_all('td'):
    for td in tr.find_all('h3'):
        for ts in td.find_all('a'):
            title = ts.get_text()
        for ts in td.find_all('a', attrs={'href': re.compile("^/book/")}):
            ref = (ts.get('href'))
            link = "https://b-ok.cc" + ref
        print("\033[0;32m" + title + "\033[0m : \n")
        print("\033[0;36mBook link : \033[0m " + link)
        reqdir = requests.get(link, headers)
        soup = BeautifulSoup(reqdir.content, 'html.parser')
        for dirlink in soup.findAll('a', attrs={'href': re.compile("^/dl/")}):
            linko = (dirlink.get('href'))
            dirlinko = "https://b-ok.cc" + linko
        print("\033[0;31mDirect Book link : \033[0m " + dirlinko)
        print("====================")
