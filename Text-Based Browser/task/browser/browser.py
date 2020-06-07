import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore


# write your code here
init(autoreset=True)
history = deque()
prefix = 'https://'
url = input('>')

if (url == 'back') and (len(history) > 0):
    url = history.popleft()
elif prefix not in url:
    url = prefix + url

if '.' in url:
    if not os.path.exists(sys.argv[1]):
        os.makedirs(sys.argv[1])

    r = requests.get(url)
    if r:
        text_soup = ""
        for tag in BeautifulSoup(r.content, 'html.parser').find_all(["p", "a", "ul", "ol", "li"]):
            text_soup += tag.text
            print(Fore.BLUE + tag.text, end='') if tag.name == 'a' else print(tag.text, end='')

        history.append(text_soup)
        with open(sys.argv[1] + '/' + url.split('/')[-1].replace('.', '_'), 'w') as file:
            file.write(text_soup)
