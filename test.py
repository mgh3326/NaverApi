import json

with open('data.json', 'r', encoding='utf-8') as f:
    array = json.load(f)
search = "경기도"
print(array)
for i in range(10,20):
    temp = (1 + i * 100)
    URL = 'https://openapi.naver.com/v1/search/news.json?query=' + search + '&display=3&start=' + str(temp) + '&sort=sim'
    print(URL)
