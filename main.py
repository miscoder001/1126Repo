
import requests
#import pyquery
from pyquery import PyQuery as pq

# 送出 web request
response =  requests.get("https://books.toscrape.com/")
# 將 回應內容 送交 pyquery 處理
pyPage = pq( response.content )
# 請務必確認 回傳的物件屬於 pyquery 物件
print( type(pyPage ))
print("網頁內容")
print("=======================================================")
print(pyPage.html())
print("--------- 擷取 title 標籤(tag, element元素)")
title = pyPage.find('title')
print('title回傳屬於', type(title))
print('網頁標題是: ', title.text())

