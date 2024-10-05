first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях без zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))  # Выведет разницы длин, если длины строк не равны
print(list(second_result))  # Выведет True/False в зависимости от равенства длин
