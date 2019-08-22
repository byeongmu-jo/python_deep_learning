import requests
from bs4 import BeautifulSoup

def get_subjects():
    subjects = []
    req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=1&sidoCode=&dltSIDO=&sName=')
    html = req.text
    sope = BeautifulSoup(html, 'html.parser')
    dive =  sope.findAll('li', {"class": "PlaceItem clickArea"})

    for div in dive:
        links = div.findAll('li')
        for link in links:
                subject = link.text
                subjects.append(subject)
    return subjects


url = 'https://www.tomntoms.com/store/storeList_frame.php?page=1&sidoCode=&dltSIDO=&sName='
req = requests.get(url)
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})

c = []
for i in range(0,42):
    a = 'https://www.tomntoms.com/store/storeList_frame.php?page=1&sidoCode=&dltSIDO=&sName='


req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=1&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})

b = []
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=2&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=3&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=4&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=5&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=6&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=7&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=8&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=8&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=9&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=10&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=11&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=12&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=13&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=14&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=15&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)


req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=16&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=17&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=18&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)


req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=19&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=20&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=21&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=22&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=23&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=24&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=25&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=26&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=27&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=28&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=29&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=30&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=31&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=32&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=33&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=34&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=35&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)


req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=36&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive =  sope.findAll('dd', {"class": "addr"})
for i in range(0,10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=37&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=38&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=39&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=40&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=41&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=42&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

req = requests.get('https://www.tomntoms.com/store/storeList_frame.php?page=43&sidoCode=&dltSIDO=&sName=')
html = req.text
sope = BeautifulSoup(html, 'html.parser')
dive = sope.findAll('dd', {"class": "addr"})
for i in range(0, 10):
    a = dive[i].get_text(strip=True)
    b.append(a)

import panads as pd
c = DataFrame(b)
f = []
g = []
for i in range(0,431):
    e = str(c[0][i])
    f = e.index('\t')
    h = e[0:f]
    g.append(h)

k = DataFrame(g)
k.columns = ['tomtom']

k.to_csv("D:/Workspace/python_deep_learning/tom.csv")

import pandas as pd
import numpy

pd.read_csv("D:/Workspace/python_deep_learning/tom.csv")





