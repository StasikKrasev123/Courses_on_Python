# • 1Выводить текущий курс евро к рублю (считаем, что он не меняется)
# • 2Вывести стоимость проживания не только в евро, но и в рублях
# • 3Допустим у нас есть бюджет на поездку, выяснить, не выходим ли мы за него, вывести предупреждение
# • 4Предположим, что каждый из нас начал вести список расходов. Вывести сумму, которую потратил
# каждый и сколько осталось в общем бюджете.

# 1
print("Текущий курс белорусского рубля к евро:", 2.44)

# 2
number_of_living_days = int(input("Введите количество дней проживания"))
price_for_living_euro = float(input("Введите цену в евро за день"))

general_price_for_living_euro = number_of_living_days * \
                                price_for_living_euro

print("Цена за проживание в евро", general_price_for_living_euro)

general_price_for_living_rub = general_price_for_living_euro * \
                               2.44

print("Цена за проживание в рублях", general_price_for_living_rub)

# 3
our_budget = float(input("Введите сумму бюджета"))

price_for_living = float(input("Введите цена за проживание"))
price_for_road = float(input("Введите цену за перелёт или переезд"))
price_for_food = float(input("Введите цену за еду"))

cost = price_for_living + \
       price_for_food + \
       price_for_road
if cost > our_budget:
    print("Мы не вписываемся в бюджет")
else:
    print("Всё хорошо")

# 4
expenses_for_living_for_first_human = float(input("Введите затраты на проживание для первого человека"))
expenses_for_road_for_first_human = float(input("Введите затраты на перелёт или переезд для первого человека"))
expenses_for_food_for_first_human = float(input("Введите затраты на еду для первого человека"))
list_of_expenses_for_first_human = [expenses_for_living_for_first_human, expenses_for_road_for_first_human,
                                    expenses_for_food_for_first_human]

expenses_for_living_for_second_human = float(input("Введите затраты на проживание для второго человека"))
expenses_for_road_for_second_human = float(input("Введите затраты на перелёт или переезд для второго человека"))
expenses_for_food_for_second_human = float(input("Введите затраты на еду для второго человека"))
list_of_expenses_for_second_human = [expenses_for_living_for_second_human, expenses_for_road_for_second_human,
                                     expenses_for_food_for_second_human]

print("Затраты для первого человека", sum(list_of_expenses_for_first_human))
print("Затраты для второго человека", sum(list_of_expenses_for_second_human))

original_budget = float(input("Введите первоначальный бюджет"))

print("{0}:Первоначальный бюджет, {1}:Остаток от бюджета".format(original_budget, original_budget -
                                                                 (sum(list_of_expenses_for_first_human) + sum(
                                                                     list_of_expenses_for_second_human))))
# Макс поставь оценку после проверки
# Оценка = ?
