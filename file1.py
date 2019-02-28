import math
import random
import re
import random
import sys


# print(1)
# print(123 + 456)
# print(1.5 * 4)
# print(2 ** 100)
# # print(len(str(2 ** 1000000)))
#
# print(math.pi)
#
# print(math.sqrt(5))
# print(random.random())
# print(random.choice([1, 2, 3, 45, 5443, 5]))
#
# a = "span"
# print(len(a))
# print(a[0])
# print(a[1])
# s = "work hard"
# # print(s[- 3])
# # print(s[1:])
# a = "Stas you are lazy"
# print(a + " " + s)
# print((a + " " + s) * 3)* 3)
# a = "example"
# print(("z" + a[1:]))
# print(a.find("m"))
# print(a.replace("ex", "joke"))
# line = " aaaaa bbbbb ccc bbb"
# line.split("a")
# print(line)
# a = 1
# print(dir(a))
# a = "ak\nkl\t"
# print(a)
# line = """gsagasagsaga""""""safasfsafsafasfsaffsafs""" """sfaafasfasfsafasfsafas"""
# line2 = """i""" """am""" """Stas"""
# print(line+" sa   "+line2)
# match = re.match("Hello[\t]*(.*)world[\n]", "Hello    python world")
# match.group(0)
# match = re.match("/(.*)/(.*)/(.*)", "/usr/home/lumberjack")
# print(match.groups())
# a = re.match(",[\t]*(.*)/[\t]*(.*),(.*)", ", ааа/ bbb,ccc",)
# print(a.group())

# L = [1, 'sfgas', 1.23]
# print(len(L))
# a = [1, 2, 3, 55132, 5325, 98]
# print(a + L)

# a = [1, 2.3, "122", """fsafsafs""", """fsafs"""]
# # print(a)
# # a.pop(0)
# # print(a)
# # a.append("обьект")
# # print(a)
# # b = [1]
# # a = b + a
# # print(a)
# # print(len(a))
# print(a[-2:-1])
# print(a[0:2])
# print(len(a))
# a1 = "12345"
# print(a1[0:2])
# print(a1[-2:-1])
# print(len(a1))

# a = [1, 2.3, "xyz"]
# a.insert(2, "ins")
# print(a)
# a.remove(1)
# print(a)

# a = [1, 2, 3]
# a.sort()
# print(a)
# a.reverse()
# print(a)

#

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [6, 7, 8]]
# col = [row[0] for row in a]
# print(col)
# print(a[1])
# col = [row[2] for row in a if row[2] % 2 != 0]
#
# print(col)
# diag = [a[i][j] for i in [0] for j in [0, 1, 2] if a[i][j] % 2 == 0]
# print(diag)
#
# line = "spam"
# doubles = [c * 2 for c in line[-2:-1]]
# print(doubles)

#
# G = (sum(row) for row in a)
# print(next(G))
# print(next(G))

#
# Попробуй напиши программу вычисления дескриминанта квадратного уравнения, если дескриминант отрицательный то комплексное число юзай
# print("Введите коэффициенты для квадратного уравнения")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# discr = b ** 2 - 4 * a * c;
# print("Дискриминант D = %.2f" % discr)
# if discr > 0:
#     import math

#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# elif discr<0:
#     import cmath
#     x1 = (-b + cmath.sqrt(discr)) / 2 * a
#     x2 = (-b - cmath.sqrt(discr)) / 2 * a
#     print("x1 = %.2f \nx2 = %.2f" % (x1.imag, x2.imag))
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# a1 = [1, 2, 3]
# b = [[1, 2, 3],
#      [6]]
# c = a1 + b
# print(list(map(sum, b)))
# print({sum(row) for row in a})
# print({i: sum(a[i]) for i in range(2)})
# c = 3
# D = {1: "Man", "2": 7, c: [1, 2, 3]}
# print(D[3])
# D[1] += " Who sold the World"
# print(D)
# print(D[c])
# g=[1,2,3]
# print(g[1:])
# g[1]="insert"
# print(g)
# print(D[1],D["2"])
#  = {1: "spam"}
# a[1]=a[1]+a"s"
# print(a)
# a = "spam1"
# b = []
# k = [ord(c) for c in a]
# b.append(k)
# print(b)
# f= open('data.txt')
# help(f.seek)
# a = float(input("Введите первое чиcло"))
# b = float(input("Введите второе число"))
# c = str(input("Введите:+ - / *"))
#
# if type(a) == type(float) or type(b) == type(float):
#     print("Введено верно")
# else:
#     print("Неверный ввод")
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "/":
#     print(a / b)
# elif c == "*":
#     print(a * b)
# else:
#     print("Неизвестная операция")


# def square(a):
#     import math
#     ploshad = (a * a)
#     perimetr = 4 * a
#     diagonal = (math.pow(a, 2) + math.pow(a, 2))
#     tuple1 = (ploshad, diagonal, perimetr)
#
#     return tuple1
#
#
# a = float(input("Введите сторону"))
# result = square(a)
# print(result)
# uii= """"""
# def year(a):
#     if (a % 4 == 0) or (a % 100 == 0) and (a % 400 == 0):
#         return True
#     else:
#         return False
#
#
# a = int(input("Введите год"))
# s = year(a)
# if (s == True):
#     print("Високосный")
# else:
#     print("Обычный")
#     """"""
# Пользоваатель вводит строку из нескольких слов, желательно 5+
# в переменную А вводит символ
# в переменную Б вводит ещё один символ
# Найти самое большое слово в ней
# и заменить там символ переменной А на символ переменной Б
# Line = str(input("Введите строку"))
# A = str(input())
# B = str(input())
# Line.strip()
# count = 0
# C = ""
# Line_New = Line.split(" ")
# print(Line_New)
#
# for Detector in range(0, len(Line_New)):
#     if count < len(Line_New[Detector]):
#         count = len(Line_New[Detector])
#         C = Line_New[Detector]
#
# C = C.replace(A, B)
# print(C + " Наибольшее слово")

# есть список в котором числа от 10 до 100
# сгенерировать на фоне этого строку, тоесть перевести числа в символы

# list_1 = []
# number_elements = int(input("Введите количество элементов списка"))
# # заполнение списка
# for index in range(0, number_elements):
#     element = random.randint(10, 100)
#     list_1.insert(index, element)
#
# print(list_1)
# list_2 = []
# for A in list_1:
#     list_2.append(chr(A))
#
# print(list_2)
# Line = " ".join(list_2)
# print(Line)

# пользователь вводит строку из нескольких слов
# а так же 2 числа
# a,b
# при этом a>0, b < len(user_string)
# поменять местами слова с индексом a и b


# Line = input("Введите строку")
# A = int(input())
# B = int(input())
# Flag = False
# while (Flag == False):
#     if (A < 0) or (B > len(Line)):
#         A = int(input("Введите число больше 0"))
#         B = int(input("Введите число меньше длины строки"))
#         Flag = False
#     else:
#         Flag = True
#
# Line = Line.split(" ")
# if (A > len(Line)) or (B > len(Line)):
#     print("Выход индекса за границы")
#     sys.exit()
# else:
#     First_Word = Line[A]
#     Second_Word = Line[B]
#     Line[A] = Second_Word
#     Line[B] = First_Word
#     Line_New = " ".join(Line)
#     print(Line_New)
#

# пользователь вводит строку, посчитать количество вхождений каждой буквы
# # и сформировать массив в котором хранится количество каждой буквы
# # при этом лишние проверки делаться не должны
# # тоесть
# # если строка
# # пппппп
# # то на выходе
# # [6] и подсчёт идет только один раз
# #a = input()
# print(" ".join("%s - %s" % (i, a.count(i)) for i in sorted(set(a))))
# print(set(a))
# В строке заменить пробелы или несколько пробелов символом *
# Line = input("Введите строку")
# s = "{0},:Введенная строка {1},:Измененная строка" .format(Line, Line.replace(" ", "*"))
# print(s)
# Выбрать из строки числа
# Line = input("Введите строку")
# print("{0},".format([c for c in Line.split() if c.isdigit()]))
# Найти слово по его номеру
# Line = input("Введите строку")
# number_Word = int(input("Введите номер слова"))
# print(" ".join("{0}".format([c for c in Line.split(" ")[number_Word] if number_Word in range(len(Line.split(" ")))])))
# def Sum(old_parametr1, old_parametr2, length):
#     if len(old_parametr1) > len(old_parametr2) or len(old_parametr2) > len(old_parametr1):
#         raise Exception("Несоответсвие длины списков")
#     if length == None:
#         raise IndexError
#     if isinstance(old_parametr1, list) and isinstance(old_parametr2, list):
#         old_list = (old_parametr1,
#                     old_parametr2)
#     new_list = []
#     for i in range(0, length):
#         summa = old_list[0][i] + old_list[1][i]
#         new_list.append(summa)
#     new_parametr = new_list
#     return new_parametr
#
#
# def inc(x):
#     c = x + 1
#     return (c)
#
#
# def Len(element):
#     count = 0
#     for iteration in element:
#         count += 1
#     return count
#
#
# a = [1, 2, 3]
# b = [5, 6, 7]
# sfafsa = {"name": 1, 2: 3, 3: 5}
# print(Sum(a, b, 3))
# print(Len(sfafsa))
# 