import requests
from pyquery import PyQuery as pq


pyPage = pq(url="http://192.168.1.83/demo.html")
h2 = pyPage.find('h2')
print( 'text: ', h2.text() )
print( 'html:', h2.html() )
#pyFile = pq(filename="c:/aaa/bbb/index.html")
#pyFile = pq(filename="c:\\aaa\\bbb\\index.html")

#透過 id: p1 尋找
pDiv = pyPage.find("#p1")  # 請找出 頁面中是否有 id 宣告為 p1 的 tag
print('pDiv 型態: ' , type(pDiv) )
print( 'pDIV text: ', pDiv.text())
print( 'pDIV html: ', pDiv.html())

