#-*- encoding: utf8 -*-

from pyquery import PyQuery as pq
#pyquery 並不會依照 網頁內的設定而決定文字編碼  而是"必須" 在指令中宣告
pyPage = pq(url="http://192.168.1.83/demo.html", encoding="utf-8")
h1s = pyPage.find('h1')
print( type(h1s))
#print( h1.text())

# h1 內有 7 各 H1 的組合 是否可以透過 len() 計算數量
print( len( h1s ))  # h1s 是一個蒐集了七個 html tag 的 pyQuery 物件 ( 七個物件並非 pyQuery )
# for h1 in h1s:
#     ph1 = pq(h1)    # 將每一個 lxml 物件轉換成 pyquery 物件再透過 pyquery function 存取
#     print(type(ph1))
#     print( ph1.text())

h1array = pyPage.find('h1')
for t in h1array.items():   # 透過 呼叫 items() 可以將每一個 lxml 元件轉換成 pyQuery 物件後回傳 [存入 t]
    print( t.text())

for t2 in pyPage.find('h1').items():
    print(t2.text())


