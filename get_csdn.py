import requests
from bs4 import BeautifulSoup
import json
import random

# 获取csdn粉丝
url = 'https://blog.csdn.net/u014297502'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

res = requests.get(url, headers=headers)
content = res.text
soup = BeautifulSoup(content, "html.parser")
allCount = soup.select(".user-profile-statistics-num")
# 访问量
#fangwenCount = allCount[0].string
# 粉丝数
fensiNum = allCount[3].string
fensiNum = str(fensiNum).replace(",", "").strip()
# 排名
#paiming = allCount[2].string
# 关注数目
#guanzhu = allCount[3].string
'''
authorInfomation = {}
authorInfomation["fangwenCount"]=fangwenCount
authorInfomation["fensiNum"]=fensiNum
authorInfomation["paiming"]=paiming
authorInfomation["guanzhu"]=guanzhu
print(authorInfomation)
json.dump(authorInfomation,open('authorInfomation.json','w'))
'''
content = f'[![CSDN](https://img.shields.io/badge/CSDN-{fensiNum}%20%E5%85%B3%E6%B3%A8-red)](https://blog.csdn.net/u014297502)\n'
# 读入模板
with open('README-2.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
# 在第五行插入一行
lines.insert(6, content)
# 将修改后的内容保存为新文件
with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
