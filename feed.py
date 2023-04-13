import requests
from bs4 import BeautifulSoup
import feedgenerator
import codecs

url = "https://www.wangrs.co/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
latest_news = soup.find('h1', id='-最新讯息').find_next_sibling()

# 创建feed对象
feed = feedgenerator.Rss201rev2Feed(
    title='最新讯息',  # feed标题
    link=url,  # feed主页链接
    description='讯息时间',  # feed描述
)

for li in latest_news.find_all('li'):
    content = li.text.replace("🎉", "").replace("🥈", "").split()
    news = " ".join(content[1:])
    time = content[0].replace(":", "")
    #print(time)
    #print(news)
    item_title = news
    item_link = url
    item_desc = time
    feed.add_item(title=item_title, link=item_link, description=item_desc)

# 将feed输出为XML格式，并保存到文件
feed_str = feed.writeString('utf-8')
with codecs.open('feed.xml', 'w', 'utf-8') as f:
    f.write(feed_str)