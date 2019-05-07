import vk_api
import time
from urllib import request
import sys
import vk_parsing
import dateutil.parser as dparser
f = open('date.txt', 'r+')
date_parse = f.readline()
f.truncate()
f.close()


def rewrite_data(default_date):
    file_data = open('date.txt', 'w')
    file_data.write(default_date)
    file_data.close()


def url_parsing(url):
    try:
        req = request.Request(url)
        answer = request.urlopen(req)
        answer = answer.readlines()
        list_of_ids = []
        for line in answer:
            list_of_ids.append(int(line))
        return list_of_ids
    except Exception:
        print("Error occured during web request!")
        print(sys.exc_info()[1])


def message_send(vk_session, list_of_ids, parses, owner_id):
    for i in range(len(list_of_ids)):
        vk_session.method('messages.send',
                          {'user_id': list_of_ids[i],
                           "random_id": 0,
                           "message": parses["text"],
                           "attachment": "photo" + str(owner_id) + "_" + parses["id1"] + ',' +
                                         "photo" + str(owner_id) + "_" + parses["id2"] + ',' +
                                         "photo" + str(owner_id) + "_" + parses["id3"]
                           })
        time.sleep(0.2)



def posting(date_parse):
    url_all = "https://new.broadcast.vkforms.ru/api/v1/user-list/669775?token=180051651_" \
                 "3a73d716bffe3eb086d9547eec11e50c41db7adfee50646705ce039b5ed0fcf2_122434565A5748831A180051651"
    url_mens = "https://new.broadcast.vkforms.ru/api/v1/user-list/670237?token=180051651_" \
                  "b30bb78fac79bd4b44ceff60ab08e410a17205c1aa5ad5a498095c2a9a57b776_122434565A5748831A180051651"
    url_women = "https://new.broadcast.vkforms.ru/api/v1/user-list/670243?token=180051651_" \
                "b30bb78fac79bd4b44ceff60ab08e410a17205c1aa5ad5a498095c2a9a57b776_122434565A5748831A180051651"

    token = "5e2c18d79669d159425b1f8a66b92211fe94455333858f017cfc50c4db367eadfb7c2e95a260550fc9938"
    vk_session = vk_api.VkApi(token=token)
    owner_id = -180051651

    while True:
        is_woman = 0
        is_men = 0
        # get IDs of subscribers in a list
        try:
            list_of_ids_all = url_parsing(url_all)
            list_of_ids_women = url_parsing(url_women)
            list_of_ids_mens = url_parsing(url_mens)

        except Exception:
            print("Error occured during web request!")
            print(sys.exc_info()[1])
        try:
            data = vk_parsing.take_last_post()
            vk_parsing.file_writer(data)
            # creating new list with data of the last post
            parses = vk_parsing.file_reader()

            str_for_search = parses["text"]
            is_found = str_for_search.find("(жен.)")
            if is_found != -1:
                is_woman = 1
            else:
                is_men = 1
            print(parses)

            # Format of string
            default_date = time.ctime(int(parses["date"]))
            date_parse1 = dparser.parse(default_date)
            print(date_parse1)
            date_parse2 = dparser.parse(date_parse)
            print(date_parse2)
            big_list_of_ids = []
            #big_list_of_ids = list_of_ids_all

            if date_parse1 > date_parse2:
                if (is_men):
                    big_list_of_ids.extend(list_of_ids_mens)
                if (is_woman):
                    big_list_of_ids.extend(list_of_ids_women)
                big_list_of_ids = set(big_list_of_ids)
                big_list_of_ids = list(big_list_of_ids)
                message_send(vk_session, big_list_of_ids, parses, owner_id)
                rewrite_data(default_date)
                date_parse = default_date
                time.sleep(30)
            else:
                time.sleep(30)
                continue
        except Exception:
            print('Posts exception.')
            print(sys.exc_info()[1])


posting(date_parse)


