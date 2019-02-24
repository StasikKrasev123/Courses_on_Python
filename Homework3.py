# Зачем такое разнообразие типов данных?
# Можно ли было бы обойтись одним?
# Поразмышляйте, 2-4 предложения

# 1
# В Python множество типов данных числа строки логический тип ,последовательности(списки, множества,кортежи) и отображения(словари).Все типы предназначены для выполнения
# разных операции с данными их обработке.Числа чтобы считать разные математические и экономические задачи, строки для работы с языковым разнообразием,также внутренние типы
# для более удобного упорядочивания числовых и строковых данных.

# 2
# Придумайте 5 примеров данных, которые удобно было бы хранить
# в словарях или с использованием словарей.
# Информация о населении
dictionary1 = {
    "name": "Tom",
    "age": 14,
    "nationality": "Hungarian"
}
# Информация о работниках
dictionary2 = {
    "worker_name": "Andy",
    "age": 24,
    "speciality": "locksmith"
}
# Информация о солдатах
dictionary3 = {
    "solder": "shooter",
    "army": "american",
    "batalion": 1
}
# Информация о рыцыарях
dictionary4 = {
    "Sir Jane": {"name": "Jane", "weapon": "sword", "status": "dead"},
    "Sir Jonh": {"name": "Jonh", "weapon": "hallbeard", "status": "dead"},
    "Sir Tom": {"name": "Tom", "weapon": "sword", "status": "alive"}
}

print(dictionary4["Sir Jane"]["name"])

#3
# Добавьте в программу ещё 5 стран (любых, по вашему
# усмотрению, достоверность данных большой роли не играет)
# • Добавьте новое свойство «стоимость проживания в сутки в
# валюте страны»
# • Пользуясь множествами, найдите список стран, которые:
# тёплые и есть море или находятся в шенгене, и нам хватит
# денег прожить там месяц.
name = input("Введите название страны")

sea = input("Есть ли у страны море?")
sea_check = False
if sea == "да" or sea == "Да":
    sea_check = True
else:
    sea_check = False

schengen = input("Есть ли у страны Шенген?")
schengen_check = False
if sea == "да" or sea == "Да":
    schengen_check = True
else:
    schengen_check = False

currency_for_living_in_day = int(input("Введите цену проживания за день в стране?"))
if not type(currency_for_living_in_day) == int:
    raise Exception("Неверный формат ввода")

temperature = int(input("Введите среднюю температуру в стране?"))
if not type(temperature) == int:
    raise Exception("Неверный формат ввода")

country_add = dict()
country_add["name"] = name
country_add["sea"] = sea_check
country_add["schengen"] = schengen_check
country_add["currency_for_livind_in_day"] = currency_for_living_in_day
country_add["temperature"] = temperature

countries = [
    {'name': "Thailand", "sea": True, "schengen": False, "currency_for_livind_in_day": 1400, "temperature": 34},
    {'name': "England", "sea": True, "schengen": True, "currency_for_livind_in_day": 2000, "temperature": 45},
    {'name': "Russia", "sea": False, "schengen": False, "currency_for_livind_in_day": 1000, "temperature": 67},
    {'name': "USA", "sea": True, "schengen": True, "currency_for_livind_in_day": 6000, "temperature": 16},
    {'name': "France", "sea": False, "schengen": False, "currency_for_livind_in_day": 1111, "temperature": 34}
]
countries.append(country_add)
print(countries)

currency_amount = 700000
temperature_limit = 25
our_countries = set()

for country in countries:
    if (country["sea"]) and country["schengen"] and (
            currency_amount > (country["currency_for_livind_in_day"] * 30)) and (country["temperature"] > 30):
        print("Страны подходящие для поездки:{} ".format(country["name"]))

#4
# Напишите, список значений какого типа вернёт конструкция:
# list(countries.items())
# где countries - словарь из кода программы

#вернут в списке все значения из словаря в формате списка
