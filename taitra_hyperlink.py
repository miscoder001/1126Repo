from pyquery import PyQuery as pq

pyPage = pq(url="https://www.taitra.org.tw/", encoding="utf-8")
count=0
for a in pyPage.find('a').items():
    count += 1
    # 顯示 超連結的內容
    print(count, " " , a.html() )
    # 顯示 超連結的宣告html內容
    print(count, "", a.outer_html())
    #print(count, " ", a.text())
    #print(count ,  " 連結名稱:" , a.text() , "  連結目的地: " , a.attr('href'))

print("--------------- 這是分隔符號 -------------------")
# 單獨篩選出 新聞中心的超連結

newsTag = pyPage.find('a[title="新聞中心"]')
print(" 篩選出新聞中心: " ,newsTag.outer_html() )
print(" 超連結為: " , pyPage.find('a[title="新聞中心"]').attr('href'))

# 使用虛擬屬性 篩選
oddTag = pyPage.find('a:odd')
print( '編號奇數超連結總共有: ' , len(oddTag))
evenTag = pyPage.find('a:even')
print( '編號偶數超連結總共有: ' , len(evenTag))

print('最後一個超連結: ', pyPage.find("a:last").text())
print('第一個超連結: ', pyPage.find("a:first").text())
print('第一個超連結: ', pyPage.find("a:eq(231)").text())  # 實際是 232 python 從0開始算  0~231 實際上是第 232 linked