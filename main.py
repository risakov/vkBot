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

'''def if_size(dict_of_sizes, all_sizes):
def append_sizes_ids(big_list, dict_of_sizes, all_sizes):
    is_euro = all_sizes.find("eur")
    if is_euro != -1:
        for i in range(len(big_list)):'''
def posting(date_parse):
    url_all = "https://new.broadcast.vkforms.ru/api/v1/user-list/669775?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_mens = "https://new.broadcast.vkforms.ru/api/v1/user-list/670237?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_women = "https://new.broadcast.vkforms.ru/api/v1/user-list/670243?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_38 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672557?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_39 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672559?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_40 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672560?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_41 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672562?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_42 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672563?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_43 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672565?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_44 = "https://new.broadcast.vkforms.ru/api/v1/user-list/673046?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_45 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672568?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_46 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672570?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_47 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672571?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_38_5 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672558?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_40_5 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672561?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_42_5 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672564?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_44_5 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672567?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"
    url_45_5 = "https://new.broadcast.vkforms.ru/api/v1/user-list/672569?token=api_61703_PdiCU9DOuCu4FP6blzwMPrN7"



    token = "5e2c18d79669d159425b1f8a66b92211fe94455333858f017cfc50c4db367eadfb7c2e95a260550fc9938"
    vk_session = vk_api.VkApi(token=token)
    owner_id = -180051651

    while True:
        big_list_of_ids = []
        is_woman = 0
        is_men = 0
        dict_of_sizes = {"38": 0, "39": 0, "40": 0, "41": 0, "42": 0, "43": 0, "44": 0, "45": 0, "46": 0, "47": 0,
                         "38.5": 0, "40.5": 0, "41.5": 0, "42.5": 0, "44.5": 0, "45.5": 0}
        try:
            #list_of_ids_all = url_parsing(url_all)
            list_of_ids_women = url_parsing(url_women)
            list_of_ids_mens = url_parsing(url_mens)
            list_of_ids_38 = url_parsing(url_38)
            list_of_ids_39 = url_parsing(url_39)
            list_of_ids_40 = url_parsing(url_40)
            list_of_ids_41 = url_parsing(url_41)
            list_of_ids_42 = url_parsing(url_42)
            list_of_ids_43 = url_parsing(url_43)
            list_of_ids_44 = url_parsing(url_44)
            list_of_ids_45 = url_parsing(url_45)
            list_of_ids_46 = url_parsing(url_46)
            list_of_ids_47 = url_parsing(url_47)
            list_of_ids_38_5 = url_parsing(url_38_5)
            list_of_ids_40_5 = url_parsing(url_40_5)
            list_of_ids_42_5 = url_parsing(url_42_5)
            list_of_ids_44_5 = url_parsing(url_44_5)
            list_of_ids_45_5 = url_parsing(url_45_5)
        except Exception:
            print("Error occured during web request!")
            print(sys.exc_info()[1])
        try:
            data = vk_parsing.take_last_post()
            vk_parsing.file_writer(data)
            # creating new list with data of the last post
            parses = vk_parsing.file_reader()

            str_for_search = parses["text"].lower()
            all_sizes = vk_parsing.find_ln(str_for_search.find("размер"), str_for_search).lower()
            print(all_sizes)
            is_found = str_for_search.find("жен")
            if is_found != -1:
                big_list_of_ids.extend(list_of_ids_women)
            else:
                big_list_of_ids.extend(list_of_ids_mens)

                is_eur = all_sizes.find("eu")
                is_uk = all_sizes.find("uk")
                is_rus = all_sizes.find("rus")
                is_us = all_sizes.find("us")

                if is_us != -1:
                    is_38 = all_sizes.find("5.5")
                    if is_38 != -1:
                        big_list_of_ids.extend(list_of_ids_38)

                    is_38_5 = all_sizes.find("6")
                    if is_38_5 != -1:
                        big_list_of_ids.extend(list_of_ids_38_5)

                    is_39 = all_sizes.find("6.5")
                    if is_39 != -1:
                        big_list_of_ids.extend(list_of_ids_39)

                    is_40 = all_sizes.find("7")
                    if is_40 != -1:
                        big_list_of_ids.extend(list_of_ids_40)

                    is_40_5 = all_sizes.find("7.5")
                    if is_40_5 != -1:
                        big_list_of_ids.extend(list_of_ids_40_5)

                    is_41 = all_sizes.find("8")
                    if is_41 != -1:
                        big_list_of_ids.extend(list_of_ids_41)

                    is_42 = all_sizes.find("8.5")
                    if is_42 != -1:
                        big_list_of_ids.extend(list_of_ids_42)

                    is_42_5 = all_sizes.find("9")
                    if is_42_5 != -1:
                        big_list_of_ids.extend(list_of_ids_42_5)

                    is_43 = all_sizes.find("9.5")
                    if is_43 != -1:
                        big_list_of_ids.extend(list_of_ids_43)

                    is_44 = all_sizes.find("10")
                    if is_44 != -1:
                        big_list_of_ids.extend(list_of_ids_44)

                    is_44_5 = all_sizes.find("10.5")
                    if is_44_5 != -1:
                        big_list_of_ids.extend(list_of_ids_44_5)

                    is_45 = all_sizes.find("11")
                    if is_45 != -1:
                        big_list_of_ids.extend(list_of_ids_45)

                    is_45_5 = all_sizes.find("11.5")
                    if is_45_5 != -1:
                        big_list_of_ids.extend(list_of_ids_45_5)

                    is_46 = all_sizes.find("12")
                    if is_46 != -1:
                        big_list_of_ids.extend(list_of_ids_46)

                    is_47 = all_sizes.find("12.5")
                    if is_47 != -1:
                        big_list_of_ids.extend(list_of_ids_47)

                if is_uk != -1:
                    is_38 = all_sizes.find("5")
                    if is_38 != -1:
                        big_list_of_ids.extend(list_of_ids_38)

                    is_38_5 = all_sizes.find("5")
                    if is_38_5 != -1:
                        big_list_of_ids.extend(list_of_ids_38_5)

                    is_39 = all_sizes.find("5.5")
                    if is_39 != -1:
                        big_list_of_ids.extend(list_of_ids_39)

                    is_40 = all_sizes.find("6")
                    if is_40 != -1:
                        big_list_of_ids.extend(list_of_ids_40)

                    is_40_5 = all_sizes.find("6.5")
                    if is_40_5 != -1:
                        big_list_of_ids.extend(list_of_ids_40_5)

                    is_41 = all_sizes.find("7")
                    if is_41 != -1:
                        big_list_of_ids.extend(list_of_ids_41)

                    is_42 = all_sizes.find("7.5")
                    if is_42 != -1:
                        big_list_of_ids.extend(list_of_ids_42)

                    is_42_5 = all_sizes.find("8")
                    if is_42_5 != -1:
                        big_list_of_ids.extend(list_of_ids_42_5)

                    is_43 = all_sizes.find("8.5")
                    if is_43 != -1:
                        big_list_of_ids.extend(list_of_ids_43)

                    is_44 = all_sizes.find("9")
                    if is_44 != -1:
                        big_list_of_ids.extend(list_of_ids_44)

                    is_44_5 = all_sizes.find("9.5")
                    if is_44_5 != -1:
                        big_list_of_ids.extend(list_of_ids_44_5)

                    is_45 = all_sizes.find("10")
                    if is_45 != -1:
                        big_list_of_ids.extend(list_of_ids_45)

                    is_45_5 = all_sizes.find("10.5")
                    if is_45_5 != -1:
                        big_list_of_ids.extend(list_of_ids_45_5)

                    is_46 = all_sizes.find("11")
                    if is_46 != -1:
                        big_list_of_ids.extend(list_of_ids_46)

                    is_47 = all_sizes.find("11.5")
                    if is_47 != -1:
                        big_list_of_ids.extend(list_of_ids_47)


                if is_eur != -1:
                    is_38 = all_sizes.find("38")
                    if is_38 != -1:
                        big_list_of_ids.extend(list_of_ids_38)

                    is_39 = all_sizes.find("39")
                    if is_39 != -1:
                        big_list_of_ids.extend(list_of_ids_38)

                    is_40 = all_sizes.find("40")
                    if is_40 != -1:
                        big_list_of_ids.extend(list_of_ids_40)

                    is_41 = all_sizes.find("41")
                    if is_41 != -1:
                        big_list_of_ids.extend(list_of_ids_41)

                    is_42 = all_sizes.find("42")
                    if is_42 != -1:
                        big_list_of_ids.extend(list_of_ids_42)

                    is_43 = all_sizes.find("43")
                    if is_43 != -1:
                        big_list_of_ids.extend(list_of_ids_43)

                    is_44 = all_sizes.find("44")
                    if is_44 != -1:
                        big_list_of_ids.extend(list_of_ids_44)

                    is_45 = all_sizes.find("45")
                    if is_45 != -1:
                        big_list_of_ids.extend(list_of_ids_45)

                    is_46 = all_sizes.find("46")
                    if is_46 != -1:
                        big_list_of_ids.extend(list_of_ids_46)

                    is_47 = all_sizes.find("47")
                    if is_47 != -1:
                        big_list_of_ids.extend(list_of_ids_47)

                    is_38_5 = all_sizes.find("38.5")
                    if is_38_5 != -1:
                        big_list_of_ids.extend(list_of_ids_38_5)

                    is_40_5 = all_sizes.find("40.5")
                    if is_40_5 != -1:
                        big_list_of_ids.extend(list_of_ids_40_5)

                    is_42_5 = all_sizes.find("42.5")
                    if is_42_5 != -1:
                        big_list_of_ids.extend(list_of_ids_42_5)

                    is_44_5 = all_sizes.find("44.5")
                    if is_44_5 != -1:
                        big_list_of_ids.extend(list_of_ids_44_5)

                    is_45_5 = all_sizes.find("45.5")
                    if is_45_5 != -1:
                        big_list_of_ids.extend(list_of_ids_45_5)


                if is_rus != -1:
                    is_38 = all_sizes.find("37")
                    if is_38 != -1:
                        big_list_of_ids.extend(list_of_ids_38)

                    is_38_5 = all_sizes.find("37.5")
                    if is_38_5 != -1:
                        big_list_of_ids.extend(list_of_ids_38_5)

                    is_39 = all_sizes.find("38.5")
                    if is_39 != -1:
                        big_list_of_ids.extend(list_of_ids_39)

                    is_40 = all_sizes.find("39")
                    if is_40 != -1:
                        big_list_of_ids.extend(list_of_ids_40)

                    is_40_5 = all_sizes.find("39.5")
                    if is_40_5 != -1:
                        big_list_of_ids.extend(list_of_ids_40_5)

                    is_41 = all_sizes.find("40")
                    if is_41 != -1:
                        big_list_of_ids.extend(list_of_ids_41)

                    is_42 = all_sizes.find("41")
                    if is_42 != -1:
                        big_list_of_ids.extend(list_of_ids_42)

                    is_42_5 = all_sizes.find("41.5")
                    if is_42_5 != -1:
                        big_list_of_ids.extend(list_of_ids_42_5)

                    is_43 = all_sizes.find("42")
                    if is_43 != -1:
                        big_list_of_ids.extend(list_of_ids_43)

                    is_44 = all_sizes.find("43")
                    if is_44 != -1:
                        big_list_of_ids.extend(list_of_ids_44)

                    is_44_5 = all_sizes.find("43.5")
                    if is_44_5 != -1:
                        big_list_of_ids.extend(list_of_ids_44_5)

                    is_45 = all_sizes.find("44")
                    if is_45 != -1:
                        big_list_of_ids.extend(list_of_ids_45)

                    is_45_5 = all_sizes.find("44.5")
                    if is_45_5 != -1:
                        big_list_of_ids.extend(list_of_ids_45_5)

                    is_46 = all_sizes.find("45")
                    if is_46 != -1:
                        big_list_of_ids.extend(list_of_ids_46)

                    is_47 = all_sizes.find("46")
                    if is_47 != -1:
                        big_list_of_ids.extend(list_of_ids_47)

            print(parses)

            # Format of string
            default_date = time.ctime(int(parses["date"]) + 10800)
            date_parse1 = dparser.parse(default_date)
            print(date_parse1)
            date_parse2 = dparser.parse(date_parse)
            print(date_parse2)

            #big_list_of_ids = list_of_ids_all

            if date_parse1 > date_parse2:
                big_list_of_ids = set(big_list_of_ids)
                big_list_of_ids = list(big_list_of_ids)
                print(big_list_of_ids)
                message_send(vk_session, big_list_of_ids, parses, owner_id)
                rewrite_data(default_date)
                date_parse = default_date
                time.sleep(60)
            else:
                time.sleep(60)
                continue
        except Exception:
            print('Posts exception.')
            print(sys.exc_info()[1])


posting(date_parse)


