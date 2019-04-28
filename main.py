from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time
from urllib import request
import sys
import vk_parsing
import dateutil.parser as dparser

myUrl = "https://new.broadcast.vkforms.ru/api/v1/user-list/663462?token=159597286_6ef46a6973002ef5c37a58850f1acbe89e3077e2cccf35ca61b6ea1a48cc252d_122434565A5748831A159597286"
token = "1030fbd1aa04badd72660e75dcddf9212386711adf8c721a0fe314890adebddb94331e345bd5c0e2ec2e5"
vkSession = vk_api.VkApi(token=token)
sessionApi = vkSession.get_api()
longpool = VkLongPoll(vkSession)


while True:
    #get IDs of subscribers in a list
    try:
        req = request.Request(myUrl)
        otvet = request.urlopen(req)
        otvet = otvet.readlines()
        listOfIds = []
        for line in otvet:
            listOfIds.append(int(line))
        for line in listOfIds:
            print(line)

    except Exception:
        print("Error occured during web request!")
        print(sys.exc_info()[1])
    try:
        data = vk_parsing.takeLastPost()
        vk_parsing.file_writer(data)

        #creating new list with data of the last post
        parses = vk_parsing.file_reader()
        print(parses)
        text = parses[0][0]
        urlOfImage = parses[0][1]

        #Format of string
        dateDefault = time.ctime(int(parses[0][2]))

        #Parse to datetime
        dateParse = dparser.parse(dateDefault)
        dates = []
        dates.append(dateParse)
        dates.sort()

        #reaprse to unix
        reParse = str(int(dates[len(dates)-1].timestamp()))
        print(reParse)
    except Exception:
        print('Posts exception.')

    #proccessing of the event
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            #print("Сообщение пришло в " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            #print("Текст сообщения: ", str(event.text))
            id = event.user_id
            text = event.text
            response = event.text.lower()
            if event.from_user:
                if(response == "1"):
                    vkSession.method('messages.send', {'user_id': id, "random_id": 0,"message": urlOfImage})