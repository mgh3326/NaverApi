import json
from bs4 import BeautifulSoup
import re
import ast
from json_tricks import dumps
from collections import OrderedDict
import requests
import pickle
from random import randint
from time import sleep


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


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
oh = [('title', ""), ('content', "")]
for i in range(10):
    item = []
    with open('경기도_문제/data' + str(i) + '.json', 'r', encoding='utf-8') as f:
        array = json.load(f)
        for j in range(100):
            url = array['items'][j]['link']
            html = requests.get(url, headers=headers).text
            if "naver" in url:
                soup = BeautifulSoup(html, 'html.parser')
                print(j)
                print(url)
                content = soup.find('div', attrs={'id': 'articleBodyContents'})
                if content == None:
                    content = soup.find('div', attrs={'id': 'newsEndContents'})
                    if content == None:
                        continue
                title = soup.find('h3', attrs={'id': 'articleTitle'})
                if title == None:
                    title = soup.find('h4', attrs={'class': 'title'})
                    if title == None:
                        continue
                # clean_text(title.text)
                mydict = dict(oh)

                mydict.update({'title': clean_text(title.text)
                                  , 'content': clean_text(content.text)
                               })

                item.append(mydict)
                sleep(randint(3, 5))
    with open('output' + str(i) + '.json', 'w', encoding="utf-8") as outfile:
        json.dump({'item': item}, outfile, ensure_ascii=False)
