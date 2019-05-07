import requests
import csv


#function that just take a last post
def take_last_post():
    token = "8e8d74f28e8d74f28e8d74f2618ee7358388e8d8e8d74f2d249bba3b1d4725d1db9525e"
    owner_id = '-180051651'
    version = 5.95

    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'owner_id': owner_id,
                                'count': 2,
                                'offset': 0,
                            }
                            )
    data = response.json()["response"]["items"]
    return data


#function that allow to take a neccesary data and write it in a file
def file_writer(data):
    with open('sales4life.csv', 'w') as file:
        a_pen = csv.writer(file)
        #if post not pinned - except
        #else this post is needed
        try:
            if (data[0]['is_pinned']):
                try:
                    if data[1]['attachments'][0]['type']:
                        try:
                            media_id1 = data[1]['attachments'][0]['photo']['id']
                        except Exception:
                            media_id1 = " "
                        try:
                            media_id2 = data[1]['attachments'][1]['photo']['id']
                        except Exception:
                            media_id2 = " "
                        try:
                            media_id3 = data[1]['attachments'][2]['photo']['id']
                        except Exception:
                            media_id3 = " "
                    a_pen.writerow((data[1]['text'], media_id1, media_id2, media_id3, data[1]['date']))
                except Exception:
                    a_pen.writerow((data[1]['text'], " ", " ", " ", data[1]['date']))
                    pass
        except Exception:
            try:
                if data[0]['attachments'][0]['type']:
                    try:
                        media_id1 = data[0]['attachments'][0]['photo']['id']
                    except Exception:
                        media_id1 = " "
                    try:
                        media_id2 = data[0]['attachments'][1]['photo']['id']
                    except Exception:
                        media_id2 = " "
                    try:
                        media_id3 = data[0]['attachments'][2]['photo']['id']
                    except Exception:
                        media_id3 = " "
                    a_pen.writerow((data[0]['text'], media_id1, media_id2, media_id3, data[0]['date']))
            except Exception:
                a_pen.writerow((data[0]['text'], " ", " ", " ", data[0]['date']))
                pass


#function that read a created file and write data in the list
def file_reader():
    with open("sales4life.csv", 'r') as file:
        a_pen = csv.reader(file)
        list_of_data = []
        for row in a_pen:
            list_of_data.append(row)

        dict_of_data = {}
        dict_of_data["text"] = list_of_data[0][0]
        dict_of_data["id1"] = list_of_data[0][1]
        dict_of_data["id2"] = list_of_data[0][2]
        dict_of_data["id3"] = list_of_data[0][3]
        dict_of_data["date"] = list_of_data[0][4]
        return dict_of_data
