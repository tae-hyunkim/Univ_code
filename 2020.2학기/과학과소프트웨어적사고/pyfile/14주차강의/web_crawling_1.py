#
# 참조 : http://hleecaster.com/python-web-crawling-with-beautifulsoup/
# "11가지 프로젝트로 시작하는 생활프로그래밍", 이창현 저, 이지스퍼블리싱, 2020
#

D = True
#D = False

import os, re
import usecsv
import requests
import urllib.request as ur

from bs4 import BeautifulSoup as bs

try:
    '''
    # urlopen으로 Web사이트 정보 가져오기
    url = "https://quotes.toscrape.com"

    html = ur.urlopen(url)
    if D:
        print(">> html : ", html)

    # read() 를 통하여 받은 데이터 확인
    if D:
        #line = html.read()[:100]
        line = html.read()
        print(">> line : ",line)
    
    # BeautifulSoup로 parsing하기 쉬운 형태로 변환
    soup = bs(html.read(), 'html.parser')
    '''
    
    url = "https://quotes.toscrape.com"
    webpage = requests.get(url)
    if D:
        print("1) >> webpage : ", webpage)

    soup = bs(webpage.content, 'html.parser')
    
    if D:
        print("\n2) >> soup : ", soup)

    # 특정 tag에서 텍스트만 추출하기
    # tag에서 텍스트만 출력하기
    # span tag만 모아 quote에 저장

    quote = soup.find_all('span')

    '''
    if D:
        print("\n3) >> span tag의 첫번째 text를 출력")
    print(quote[0].text)
    '''
    if D:
        print("\n3) >> span tag의 text를 모두 출력")
        
    for i in quote:
        print(i.text)

    quote_1 = soup.find_all('div', {"class" : "quote"})
    if D:
        print("\n4) >> div tag 내 class = quote 인 tag를 모두 리턴")
        print("n5) >>  class = quote 인 tag의 text 값 출력")    

    for i in quote_1:
        print(i.text)

except Exception as e:
    print("\n>>> Warning : ", e)
