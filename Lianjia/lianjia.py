import requests
url = 'http://cd.fang.lianjia.com/loupan/'
res = requests.get(url)
###encoding with utf-8
res.encoding = 'utf-8'
print res.text
file_object = open('res.html', 'w')
file_object.write(res.text)
