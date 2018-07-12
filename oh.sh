#!/usr/bin/env bash
curl "https://openapi.naver.com/v1/search/news.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim" \
    -H "X-Naver-Client-Id: Hibrg723Mi3GaN01MmE_" \
    -H "X-Naver-Client-Secret: 3Fv7a7WfKW" -v

'http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=003&aid=0008700888'