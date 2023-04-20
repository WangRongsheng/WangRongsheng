import requests
import xlrd
import xlwt
from lxml import etree
from lxml import html
from xlutils.copy import copy
import xml.etree.ElementTree as ET

# 爬取CSDN博客的所有博客文章链接
 
# 第1页: https://blog.csdn.net/cnds123321/article/list/1
# 第2页: https://blog.csdn.net/cnds123321/article/list/2
# 第3页: https://blog.csdn.net/cnds123321/article/list/3
# 故可以得出公式: url="https://blog.csdn.net/"+author_name+"/article/list/"+page_index
# author_name指的是博主的名字,page_index指的是页码当前是第几页

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
# 博主名字
author_name = 'u014297502'

# 博主博文页数
page_num = 1

# 循环每页
for index in range(1, page_num + 1):
    # 拼接URL
    page_url = "https://blog.csdn.net/" + author_name + "/article/list/" + str(index)
    # 发送请求,获取响应
    response = requests.get(page_url, headers=header).content
    # 将HTML源码字符串转换尘土HTML对象
    page_html = etree.HTML(response)
    # 博客文章的标题
    title_list = html.fromstring(response.decode()).xpath(
        "//div[@class='article-item-box csdn-tracking-statistics']/h4/a/text()")
    # 处理换行问题
    csdn_article_title_list = []
    for i in range(0, len(title_list)):
        csdn_article_title_list.append(title_list[i].strip())
    while "" in csdn_article_title_list:
        csdn_article_title_list.remove("")
    # 博客文章的类型
    csdn_article_type_list = page_html.xpath("//div[@class='article-item-box csdn-tracking-statistics']/h4/a/span")
    # 博客文章的链接
    csdn_article_link_list = page_html.xpath("//div[@class='article-item-box csdn-tracking-statistics']//h4//a/@href")
    # 博客文章的发表日期
    csdn_article_publishDate_list = page_html.xpath(
        "//div[@class='info-box d-flex align-content-center']/p/span[@class='date']")
    # 博客文章的阅读数
    csdn_article_readerCount_list = page_html.xpath(
        "//div[@class='info-box d-flex align-content-center']/p[last()-2]/span/span[@class='num']")
    # 博客文章的评论数
    csdn_article_commentCount_list = page_html.xpath(
        "//div[@class='info-box d-flex align-content-center']/p[last()]/span/span[@class='num']")
    # 将数据保存到excel表格中
    print(title_list[0:10])
    #print(csdn_article_link_list[0:10])
    
    # 读取XML文件
    tree = ET.parse('feed.xml')
    # 获取XML文件的根节点
    root = tree.getroot()
    news = []
    # 获取item节点下的所有子节点title
    for title in root.findall('.//item/title'):
        news.append(title.text)
    
    # 读入模板
    with open('README-temp.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # 在第五行插入一行
    lines.insert(28, '|最新动态|最新博文| \n |:-|:-|')
    lines.insert(30, '|1.'+str(news[0])+'|1.['+str(title_list[1]).replace("\n", "").replace(" ", "")+']('+str(csdn_article_link_list[0])+')|\n')
    lines.insert(31, '|2.'+str(news[1])+'|2.['+str(title_list[3]).replace("\n", "").replace(" ", "")+']('+str(csdn_article_link_list[1])+')|\n')
    lines.insert(32, '|3.'+str(news[2])+'|3.['+str(title_list[5]).replace("\n", "").replace(" ", "")+']('+str(csdn_article_link_list[2])+')|\n')
    lines.insert(33, '|4.'+str(news[3])+'|4.['+str(title_list[7]).replace("\n", "").replace(" ", "")+']('+str(csdn_article_link_list[3])+')|\n')
    lines.insert(34, '|5.'+str(news[4])+'|5.['+str(title_list[9]).replace("\n", "").replace(" ", "")+']('+str(csdn_article_link_list[4])+')|\n')
    # 将修改后的内容保存为新文件
    with open('README-2.md', 'w', encoding='utf-8') as f:
        f.writelines(lines)
