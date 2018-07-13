import requests
import json

search = "현대 자동차"

headers = {'Content-Type': 'application/json; charset=utf-8', 'X-Naver-Client-Id': 'RuFoLfsTtI8AaT_9bWNn',
           'X-Naver-Client-Secret': 'kpOxKkLdiK'}
URL = 'https://openapi.naver.com/v1/search/news.json?query=' + search + '&display=3&start=3&sort=sim'

for i in range(10):
    temp = (1 + i * 100)
    URL = 'https://openapi.naver.com/v1/search/news.json?query=' + search + '&display=100&start=' + str(
        temp) + '&sort=sim'
    res = requests.get(URL, headers=headers)
    var = json.loads(res.text)
    print(URL)
    with open('data' + str(i) + '.json', 'w', encoding="utf-8") as outfile:
        json.dump(var, outfile, ensure_ascii=False)
