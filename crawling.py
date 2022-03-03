# requests 불러오기

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# headers에 'User-Agent' 값 넣기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
}

# url에 주소 넣기
url = "https://www.transfermarkt.com/"
# requests.get()으로 요청하기
r = requests.get(url, headers=headers)

# status_code 응답확인하기
print(r.status_code)

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.p)
print(soup.find('p').get_text())
# a_list = soup.find_all('a')
# for i in a_list:
#     print(i.text)
