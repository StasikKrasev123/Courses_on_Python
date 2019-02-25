# Сделать интерактивное приложение
# • Ждёт от вас ввод, строку
# • ‘v’ - просит ввести новый визит (начало, затем конец)
# • ‘p’ - просит ввести дату следующего визита, говорит, сколько дней вы можете провести в шенгене
# • ‘e’ - выход
# • Выводит текущий список визитов
# • Вывод сообщение о нарушения условий пребывания
# • Ожидается, что повторяющиеся или громоздкий код вы попробуете вынести в функции
# • На зачёт с отличием:
# • ‘r’ - просит ввести начало и конец визита, удаляет визит
# • Вывод ошибки, если визиты пересекаются

import sys

SCHENGEN_LIMIT = 180

print("Это приложение шенгенский калькулятор")

# Допустим я не знаю вывести список в файл и сохранять введенные визиты пусть это будет предполагаем введенный список визитов
list_of_visit = [[1, 2], [3, 10], [11, 21], [22, 30]]


def total_time(begin, end):
    total_time_in_country = end - begin + 1
    return total_time_in_country


def dates_input_begin():
    print("Введите дату начала поездки")
    begin_of_visit = int(input("Дата начала поездки?"))
    return (begin_of_visit)


def dates_input_end():
    print("Введите дату конца поездки")
    end_of_visit = int(input("Дата конца поездки"))
    return end_of_visit


def create_visit(dates):
    visits = []
    visits.append(dates)
    return visits


def create_dates(begin, end):
    dates = [begin, end]
    return dates


def new_visit():
    result = create_visit(create_dates(dates_input_begin(), dates_input_end()))
    print("Число начала поездки:{},Число конца поездки:{}".format(result[0][0], result[0][1]))


def limit_days():
    print("Введите дату следующего визита")
    next_date = int(input("Дата следующего визита?"))
    condition = input("Были ли вы в поездке до этого введите да или нет?")
    if condition == "да" or condition == "Да" or condition == "ДА":
        total = total_time(dates_input_begin(), dates_input_end())
        schengen_time = SCHENGEN_LIMIT - total
        result = [next_date, schengen_time]
        print(
            "Дата следующего визита:{},Оставшееся время в шенгенской зоне:{},Примерная дата выезда из ЕС в планируемом визите:{}".format(
                result[0], result[1], (result[0] + result[1])))
    elif condition == "нет" or condition == "Нет" or condition == "НЕТ":
        print("Дата следующего визита:{},Оставшееся время в шенгенской зоне:{}".format(next_date, SCHENGEN_LIMIT))
    else:
        sys.exit("Не введено условие")


def print_list_of_visits():
    list_of_visit.append(create_dates(dates_input_begin(), dates_input_end()))
    print(list_of_visit)


def delete_visit_in_list_of_visits():
    result = create_dates(dates_input_begin(), dates_input_end())
    for visit in list_of_visit:
        if result == visit:
            list_of_visit.remove(visit)


def program_close():
    sys.exit("Вы вышли из программы")


def menu(operation):
    print("Вы ввели операцию номер:{}".format(operation))
    if operation == 1:
        new_visit()
    elif operation == 2:
        limit_days()
    elif operation == 3:
        print_list_of_visits()
    elif operation == 4:
        delete_visit_in_list_of_visits()
    elif operation == 5:
        program_close()


operation = int(input("Введите номер операции?"))
menu(operation)
