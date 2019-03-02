# Получать исходный список визитов из файла
# Записать список визитов в файл при выходе
# Залить результат на github и прислать ссылку
# Написать для чего используются типы данных: json, xml, yaml
list_of_visits = [[1, 2], [3, 10], [11, 17]]


# with open('visits.txt', 'r') as doc:
#     for visit in doc:
#         list_of_visits.append(visit.rstrip().split())
#
# print(list_of_visits)
#
# list_of_visits.append([30, 31])
# print(list_of_visits)
# with open('visits.txt', 'w') as write_doc:
#     for visit in list_of_visits:
#         write_doc.write("{} {}\n".format(visit[0], visit[1]))
def write_list_of_visits(list_):
    with open('visits.txt', 'w') as  doc:
        for visit in list_:
            doc.write("{} {} \n".format(visit[0], visit[1]))
    return ("Это список записан в файл:{}".format(list_))


def read_list_of_visits(list_):
    with open('visits.txt') as doc:
        for visit in doc:
            list_.append(visit.rstrip().split())
    return list_


print(read_list_of_visits(list_of_visits))
print(write_list_of_visits(list_of_visits))
