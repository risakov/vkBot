import vk_api
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
    myUrl = "https://new.broadcast.vkforms.ru/api/v1/user-list/669775?token=180051651_3a73d716bffe3eb086d9547eec11e50c41db7adfee50646705ce039b5ed0fcf2_122434565A5748831A180051651"
    token = "5e2c18d79669d159425b1f8a66b92211fe94455333858f017cfc50c4db367eadfb7c2e95a260550fc9938"
    vkSession = vk_api.VkApi(token=token)
    owner_id = -180051651
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


