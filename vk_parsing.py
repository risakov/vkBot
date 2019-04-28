import requests
import time
import csv
from datetime import datetime

#function that just take a last post
def takeLastPost():
    token = "8e8d74f28e8d74f28e8d74f2618ee7358388e8d8e8d74f2d249bba3b1d4725d1db9525e"
    owner_id = '-159597286'
    version = 5.95

    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'owner_id': owner_id,
                                'count': 1,
                                'offset': 0
                            }
                            )
    data = response.json()["response"]["items"]
    return data

#function that allow to take a neccesary data and write it in a file
def file_writer(data):
    with open('sales4life.csv', 'w') as file:
        a_pen = csv.writer(file)
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except Exception:
                pass
            a_pen.writerow((post['text'], img_url, post['date']))

#function that read created file and write data in list
def file_reader():
    with open("sales4life.csv", 'r') as file:
        a_pen = csv.reader(file)
        listOfData = []
        for row in a_pen:
            listOfData.append(row)
        return listOfData

'''token = "8e8d74f28e8d74f28e8d74f2618ee7358388e8d8e8d74f2d249bba3b1d4725d1db9525e"
owner_id = '-159597286'
version = 5.95
response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'owner_id': owner_id,
                            'count': 1,
                            'offset': 0
                            }
                            )
data = response.json()
print(1)'''