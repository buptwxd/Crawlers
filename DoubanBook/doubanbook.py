
import requests
from bs4 import BeautifulSoup
    
url = 'https://book.douban.com/subject_search?search_text=%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B&cat=1001'
res = requests.get(url,verify=False)
print type(res)
print res.status_code
  
res.encoding = 'utf-8'
# print res.text  
soup = BeautifulSoup(res.text, "lxml")
for item in soup.select('.subject-item'):
    #print item.select('.rating_nums')[0].text
    #print item.select('a')
    print item.select('a')[1]['title'].strip()
    print item.select('.pub')[0].text.strip()
    if item.select('.rating_nums'):
        print item.select('.rating_nums')[0].text.strip()
    
    
#模拟的情况
#登录book.douban.com，输入关键字：网络编程
#依次将打印书名
#           出版社信息
#           豆瓣评分
