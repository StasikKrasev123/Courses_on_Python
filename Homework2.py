# •Реализуйте шенгенский калькулятор начиная от кода с
# переменными
residence_limit = 90  # 45, 60
schengen_constraint = 180
total_time_in_es = 0
# Мы тратим в день
cost_per_day = 15
list_of_visit_eu = [[1, 10], [11, 12], [18, 22], [21, 25], [26, 30]]
for visit in list_of_visit_eu:
    for i in range(1, len(list_of_visit_eu)):
        if visit[0] < list_of_visit_eu[i][0] < visit[1]:
            total_time_in_es = total_time_in_es - (visit[1] - list_of_visit_eu[i][0])
    limit = total_time_in_es + visit[1] - visit[0] + 1

    if visit[0] > visit[1]:
        raise Exception("Ошибка даты")
    if limit > schengen_constraint:
        raise Exception("Лимит на выезд превышен")
    if visit[1] - visit[0] + 1 > residence_limit:
        raise Exception("Лимит пребывания превышен")
    total_time_in_es += visit[1] - visit[0] + 1

# assert total_time_in_es == 10 + 5 + 5 + 5

if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС дней:', total_time_in_es)
