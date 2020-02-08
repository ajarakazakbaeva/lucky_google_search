#!/usr/bin/env python3
import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
linkelems = soup.select('.kCrYT a')
#print(linkelems)
numopen = min(5, len(linkelems))
print(numopen)

for i in range(numopen):
    webbrowser.open('http://google.com'+linkelems[i].get('href'))

