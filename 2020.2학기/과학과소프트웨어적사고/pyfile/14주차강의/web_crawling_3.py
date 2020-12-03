#
# 참조 : http://hleecaster.com/python-web-crawling-with-beautifulsoup/
# "11가지 프로젝트로 시작하는 생활프로그래밍", 이창현 저, 이지스퍼블리싱, 2020
#

D = True
D_1 = False

import os, re
import usecsv
import requests
import urllib.request as ur

from bs4 import BeautifulSoup as bs

try:
    os.chdir(r'C:\과소사\과소사-강의예제\web_crawling')

    news = "https://news.daum.net/"

    webpage = requests.get(news)
    if D:
        print("\n1) >> webpage : ", webpage)

    soup = bs(webpage.content, 'html.parser')
    if D:
       print("\n2) >> soup : ", soup)

    # 기사 제목 추출하기
    # find_all로 <div> 내용 추출 
    # class 속성이 ‘item_issue’인 div 안에 존재
    if D:
        print("\n4) >> 기사 제목 추출하기")

    headline = soup.find_all('div', {"class" : "item_issue"})

    for i in headline:
        print(i.text, "\n")

    # find_all로 <a> tag 추출하기
    if D:
        print("\n5) >>  find_all로 <a> tag 추출하기 : ")

    for i in soup.find_all('a')[:5]:
        print(i.get('href'))

    # 원하는 영역에서 하이퍼링크 모두 추출하기
    # 인덱스를 지정 후 get 사용 가능
    # 추출한 hyperlink들을 file f에 저장 
    if D:
        print("\n6) >> 원하는 영역에서 하이퍼링크 모두 추출하여 file로 저장")

    # 한글 처리시 error 발생가능. UNICODE로 처리
    # -1 은  buffer
    f = open('links.txt', 'w', -1, "utf-8")

    for i in headline:
        print(i.find_all('a')[0].get('href'))
        f.write(i.find_all('a')[0].get('href')+'\n')

    f.close()

    # 기사 제목 출력 후 연결된 링크를 통하여 기사 본문 URL 정보 얻은 후 file에 저장
    if D:
        print("\n7) >> 기사 제목 출력 후 연결된 링크를 통하여 기사 본문 URL 정보 얻은 후 \
file에 저장")

    f_1 = open('article_total.txt', 'a', -1, "utf-8")
    
    for i in headline:
        if D:
            print("\n7-1) >> 상위기사 제목 : ")
        print(i.text, "\n")
        f_1.write(i.text)

        new_link = i.find_all('a')[0].get('href')
        link_webpage = requests.get(new_link)
        if D:
            print("\n7-2) >> new_link : ", new_link)
            print("\n7-3) >> link_webpage : ", link_webpage)

        soup_link = bs(link_webpage.content, 'html.parser')
        for j in soup_link.find_all('p'):
            print(j.text, "\n")
            f_1.write(j.text)

    f_1.close()

    # Portal Site에서 기사 crawling 하기
    # 기사 제목과 내용 한번에 추출하여 file에 저장 
    if D:
        print("\n8) >> Portal Site에서 기사내용 crawling 하기")
        print("\n        기사 제목과 내용 한번에 추출하여 file에 저장 ")

    article_link = 'http://go.seoul.co.kr/news/newsView.php?id=20201109014005'

    article = requests.get(article_link)
    if D:
        print("\n9) >> article : ", article)

    soup_article = bs(article.content, 'html.parser')
    if D:
       print("\n10) >> soup_article : ", soup_article)
       print("\n11) >> 전체기사 내용")

    f_2 = open('article_New.txt', 'w', -1, "utf-8") 
    
    for i in soup_article.find_all('p'):
        print(i.text)
        f_2.write(i.text)

    f_2.close()


except Exception as e:
    print("\n>>> Warning : ", e)

