# Данные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для first_result: разница длин строк из списков first и second, если их длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для second_result: сравнение длин строк без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))    # [1, 2]
print(list(second_result))   # [False, False, True]
