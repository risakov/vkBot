from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time
from urllib import request
import sys
import vk_parsing
import dateutil.parser as dparser
f = open('date.txt', 'r+')
dateParse = f.readline()
f.truncate()
f.close()
def posting(dateParse):
    myUrl = "https://new.broadcast.vkforms.ru/api/v1/user-list/663462?token=api_61099_QpGpiIef1uuqHHKhWwH5i4PA"
    token = "1030fbd1aa04badd72660e75dcddf9212386711adf8c721a0fe314890adebddb94331e345bd5c0e2ec2e5"
    vkSession = vk_api.VkApi(token=token)
    sessionApi = vkSession.get_api()
    longPool = VkLongPoll(vkSession)
    urlOfImage = ""
    owner_id = -159597286
    dateMain = 0;
    while True:
        # get IDs of subscribers in a list
        try:
            req = request.Request(myUrl)
            answer = request.urlopen(req)
            answer = answer.readlines()
            listOfIds = []
            for line in answer:
                listOfIds.append(int(line))

        except Exception:
            print("Error occured during web request!")
            print(sys.exc_info()[1])
        try:
            data = vk_parsing.takeLastPost()
            vk_parsing.file_writer(data)
            # creating new list with data of the last post
            parses = vk_parsing.file_reader()
            print(parses)

            # Format of string
            dateDefault = time.ctime(int(parses["date"]) + 10800)
            dateParse1 = dparser.parse(dateDefault)
            print(dateParse1)
            dateParse2 = dparser.parse(dateParse)
            print(dateParse2)
            if dateParse1 > dateParse2:
                for i in range(len(listOfIds)):
                    vkSession.method('messages.send',
                                    {'user_id': listOfIds[i],
                                    "random_id": 0,
                                    "message": parses["text"],
                                    "attachment": "photo" + str(owner_id) + "_" + parses["id1"] + ',' +
                                                  "photo" + str(owner_id) + "_" + parses["id2"] + ',' +
                                                  "photo" + str(owner_id) + "_" + parses["id3"]
                                    })
                    time.sleep(0.2)
                f = open('date.txt', 'w')
                f.write(dateDefault)
                f.close()

                dateParse = dateDefault
                time.sleep(30)
                continue
            else:
                time.sleep(30)
                continue

            '''allDates = []
            allDates.append(dateParse)
            allDates.append(dateParse1)
            allDates.sort()
            trueDate = allDates[len(allDates) - 1]'''
            # reaprse to unix

            # global reParse = int(trueDate.timestamp())
            # print(reParse)
            # print("photo" + str(owner_id) + "_" + parses["id"])
        except Exception:
            print('Posts exception.')
            print(sys.exc_info()[1])

        '''
        vkSession.method('messages.send',
                         {'user_id': 122434565,
                          "random_id": 0,
                          "message": parses["text"],
                          "attachment": "photo" + str(owner_id) + "_" + parses["id1"] + ',' +
                                        "photo" + str(owner_id) + "_" + parses["id2"] + ',' +
                                        "photo" + str(owner_id) + "_" + parses["id3"]
                          })
        time.sleep(60)'''
posting(dateParse)


