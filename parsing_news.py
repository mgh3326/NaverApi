import json
from bs4 import BeautifulSoup
import re
import ast
from json_tricks import dumps
from collections import OrderedDict
import requests
import pickle


def jsonDefault(OrderedDict):
    return OrderedDict.__dict__


class SampleClass(object):
    def __init__(self, *args, **kwargs): pass

    def __repr__(self):
        return json.dumps(self, default=jsonDefault, indent=4)

    def add_record_as_data(self, _record):
        self.__dict__.update(_record.__dict__)

    def add_record_as_attr(self, _record):
        self.record = _record


class News:
    mode = ""
    mid = ""
    sid = ""
    oid = ""
    aid = ""
    mTitle = ""
    mDate = ""
    mLink = ""
    mOriginalLink = ""
    mDescription = ""
    mContent = ""

    def __str__(self):
        return 'Person {mTitle: %s, mContent: %s}' % (self.mTitle, self.mContent)


def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)

    return cleaned_text


for i in range(2):
    with open('경기도_골칫거리/data' + str(i) + '.json', 'r', encoding='utf-8') as f:
        array = json.load(f)
    print(array)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = array['items'][0]['link']
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', attrs={'id': 'articleBodyContents'})

title = soup.find('h3', attrs={'id': 'articleTitle'})
print(title.text)
print(content.text)
news = News()
news.mTitle = title
news.mContent = content

with open('person.pickle', 'wb') as f:
    pickle.dump(news, f)  # 파일로 저장함
print(news)  # Person {name: 홍길동, age: 23}
