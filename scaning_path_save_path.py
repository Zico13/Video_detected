import yadisk
import os
from threading import Timer
import requests
from bs4 import BeautifulSoup as bs



id = "225715a2b5c54bd1869461334e486091"
pas = "24ae9c3e085b4f4cb876cd7bb1721eac"
token = "AgAAAAAcXZXeAAXkHd0nDq7LAEGPoc61Lmrg2wY"


def scan_yandex(id, pas, token):
    y = yadisk.YaDisk(id, pas, token)
    if y.check_token():
        lst = []
        for i in y.listdir('Security_folder'):
            lst.append(i['name'])
        return lst
    else:
        print("Токен не действителен")


path = "/home/zico/PycharmProjects/untitled/photo/"


def scan_dir(path):
    lst = []
    catalogue = os.listdir(path)
    for i in catalogue:
        lst.append(i)
    return lst


def yandex_upload(id_number, password, token, down_list, upload_list):
    y = yadisk.YaDisk(id_number, password, token)
    for i in down_list:
        if i not in upload_list:
            y.upload('/home/zico/PycharmProjects/untitled/photo/{}'.format(i), '/Security_folder/{}'.format(i))
            print("Идет загрузка файла ", i)
        else:
            print("Данный файл уже есть на диске")
    print("Загрузка завершена")


def proxy_parse():
    url = 'https://us-proxy.org/'
    result = ''
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        divs = soup.find_all('td')
        ip = divs[::8]
        port = divs[1::8]
        for i in range(100):
            f = open('/home/zico/PycharmProjects/untitled/proxy/proxy.txt', 'a')
            f.write(str(ip[i]).strip("<td></td>") + ':' + str(port[i]).strip("<td></td>") + '\n')
        f.close()



proxy_parse()


