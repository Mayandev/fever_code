import json
import urllib.request
import requests
from requests import RequestException
import csv

list = []




def get_data(page):
    # 参数
    data = {
        'm': "Api",
        'c': "Xiaohuiavatar",
        'a': "xiaohui_list",
        'p': page
    }

    # url
    url = 'https://api.iamsaonian.com/index.php'
    try:
        response = requests.get(url, data)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page_detail(html):
    data = json.loads(html)['data']['list'];
    print(data)
    for item in data:
        id = item.get('id')
        name = item.get('name')
        logo = item.get('icon')
        
        row_data = {'id': id, 'name': name, 'logo': id + '.' + format}
        list.append(row_data)
        print(id + '---下载完毕')


def main():
    # 总共274页
    for page in range(273):
        data = get_data(page + 1)
        parse_page_detail(data)

    with open('logo.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 设置表头
        fieldnames = ['id', 'name', 'logo']
        # 获得 DictWriter对象,使用，号分隔，便于云数据库导入
        dict_writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        # 第一次写入数据先写入表头
        dict_writer.writeheader()
        dict_writer.writerows(list)


if __name__ == '__main__':
    main()
