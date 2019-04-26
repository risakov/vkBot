from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
from datetime import datetime

#login, password = data.loginAndPassword()
#vkSession = vk_api.VkApi(login, password)
#vkSession.auth()

token = "1030fbd1aa04badd72660e75dcddf9212386711adf8c721a0fe314890adebddb94331e345bd5c0e2ec2e5"
vkSession = vk_api.VkApi(token=token)
sessionApi = vkSession.get_api()
longpool = VkLongPoll(vkSession)

while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print("Сообщение пришло в " + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения: ", str(event.text))
