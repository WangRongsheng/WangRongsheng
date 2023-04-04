import datetime
import requests
import bs4

def get_data():
    # 获取csdn粉丝
    url = 'https://blog.csdn.net/u014297502'
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    }
    
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    # 'origin': 'https://blog.csdn.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'
    }

    html_file = requests.get(url, headers=headers)
    obj_soup = bs4.BeautifulSoup(html_file.text, 'html.parser')

    result = []
    names = obj_soup.select('div .user-profile-statistics-name')
    numbers = obj_soup.select('div .user-profile-statistics-num')
    
    for i in range(len(numbers)):
        result.append("{}: {}".format(names[i].text, numbers[i].text))
    
    s = result[3]
    s = s.replace("粉丝: ", "").replace(",", "").strip()
    print(s)
    content = '[![CSDN](https://img.shields.io/badge/CSDN-'+str(s)+'%20%E5%85%B3%E6%B3%A8-red)](https://blog.csdn.net/u014297502) \n'
    
    # 读入模板
    with open('README-temp.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # 在第五行插入一行
    lines.insert(4, content)
    # 将修改后的内容保存为新文件
    with open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    html_file.close()
    
if __name__ == '__main__':
    get_data()
