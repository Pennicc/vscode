# 以下是一个简单的 Python 爬虫程序，它使用 requests 库和 BeautifulSoup 库获取网页内容和解析 HTML 页面：

import requests
from bs4 import BeautifulSoup

# 目标网页 URL
#url = 'https://www.example.com/'
url = 'https://www.yinfans.me/'
# 发送 GET 请求并获取网页内容
response = requests.get(url)
content = response.content

# 解析 HTML 页面
soup = BeautifulSoup(content, 'html.parser')

# 输出页面标题
title = soup.title.string
print('网页标题：', title)

# 此程序获取了指定 URL 的网页内容，并使用 BeautifulSoup 解析 HTML 页面。
# 然后，它输出了网页的标题。你可以通过扩展这个程序，使用正则表达式或其他技术从页面中提取感兴趣的数据。