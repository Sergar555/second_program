# a = int(input('Введите первое число  '))
# b = int(input('Введите второе число  '))
# if not(a%2) and not(b%2):
#    print("Оба числа четные")
# else:
#    print("Есть нечетные числа")

# wind_speed = int(input("Скорость ветра равна  "))
# if wind_speed < 5:
#     print("Ветер слабый")
# elif 5 <= wind_speed <= 10:
#     print("Ветер умеренный")
# elif 10 < wind_speed <= 18:
#     print("Ветер сильный")
# elif wind_speed > 18:
#     print("Ураганный ветер")

# login_list = [
#     'root',
#     'username1'
# ]
#
# password_list = {
#     'root': '1q2w3e4r',
#     'username1': 'qwerty123'
# }


# username = input('Введите логин:\n')
# if username not in login_list:
#     print("Такого пользователя не существует")
# else:
#     userpassword = input('Введите пароль:\n')
#     if userpassword == password_list[username]:
#         print("Добро пожаловать!")
#     else:
#         print("Вы вводите неверный пароль")

# A = int(input('Введите три целых числа (каждое с новой строки):\n'))
# B = int(input())
# C = int(input())
# if A < 45 and B >= 45 and C >= 45 or \
#    B < 45 and A >= 45 and C >= 45 or \
#    C < 45 and B >= 45 and A >= 45:
#     print('Условие истинно')
# else:
#     print('Условие не выполнено')

# A = int(input('Введите двузначное число:\n'))
# if (A//10 == 5) or (A%10 == 5):
#     print('Это число содержит 5-ки')
# else:
#     print('Это число не содержит 5-ки')

# A = input('Введите произвольный набор символов \n')
# A = list(A)
# B = len(list(set(A)))
# A = len(A)
# print(A == B)

# A = input('Введите 8-ми значный палиндром \n')
# A = list(A)
# B = A.copy()
# A.reverse()
# print(A == B)

# A = input('Введите 8-ми значный палиндром \n')
# B = A[::-1]
# print(A == B)

# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
#
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#    max_index = 0
#    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#    max_value = row[max_index]  # для максимального значения тоже самое
#    for index_col in range(len(row)):
#       if row[index_col] < min_value:
#          min_value = row[index_col]
#          min_index = index_col
#       if row[index_col] > max_value:
#          max_value = row[index_col]
#          max_index = index_col
#    min_value_rows.append(min_value)
#    min_index_rows.append(min_index)
#    max_value_rows.append(max_value)
#    max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i,value in enumerate(list_):
#     if value < 0:
#        print("Отрицательное число: ", value)
#        index_negative = i  # перезаписываем значение индекса
#        print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#        print("Положительное число: ", value)
#     print("---")
#     print("Конец цикла")
#     print()
#     print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
#
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# print(type(text))
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
#
# print(count)
#
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# X = input('Введите число для проверки гипотезы Сиракуз \n')
# X = int(X)
# while X != 1:
#     print(X)
#     if X % 2 == 0:
#         X = X / 2
#     elif X % 2 != 0:
#         X = (X * 3 + 1) / 2
# print(X)
# print('Проверка завершена, гипотеза верна')

# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     print(r)
#     for ph in range(heads + 1):  # количество фазанов
#         print("   ", ph)
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             print("Превышено")
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
#         print("Не превышено")

# def print_2_add_2():
#     print(2 + 2)
#
#
# def char_frequency(text):
#     text = text.lower()
#     text = text.replace(" ", "")
#     text = text.replace("\n", "")
#     print(text)
#     print(type(text))
#     count = {}  # для подсчета символов и их количества
#     for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#     print(count)
#
#     for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
#
# def number_divisor(number, deviser = 2):
#     if deviser == 2:
#         print('Проверяем число на четность')
#         if number % deviser == 0:
#             print('Число четное')
#         else:
#             print('Число нечетное')
#     else:
#         print(f'Проверяем является ли {deviser} делителем {number}')
#         if number % deviser == 0:
#             print(f'{deviser} делителем {number}')
#         else:
#             print(f'{deviser} не является делителем {number}')
#
#
# def ladder(n):
#     for i in range(n,0,-1):
#         print('*'*i)
#
# def amount_divisors_of_number(number):
#     count = 0
#     for i in range(number,0,-1):
#         if number % i == 0:
#             print(i)
#             count +=1
#     return count
#
#
# x = 3
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# # hello_world_func = get_my_func()  # получить функцию в качестве результата
# #
# # print(type(hello_world_func))  # <class 'function'>
# # hello_world_func()  # Hello
#
# def multiplier(**factors):
#     product_of_numbers = 1
#     for i in factors:
#         product_of_numbers *= factors[i]
#
#     return product_of_numbers
#
#
#
#
# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
# def factorial(n):
#     if n == 1:
#        return 1
#     x = n * factorial(n-1)
#     print(x)
#     return x
#
# factorial(4)
#
# def sum_recur (n):
#     if n == 1:
#         return 1
#     return n + sum_recur(n-1)

# print(sum_recur(4))


# def reverse_str(string):
#    print(string)
#    if len(string) == 0:
#        return ''
#    else:
#        x = string[-1] + reverse_str(string[:-1])
#        print(x)
#        return x

# reverse_str('Даша')

# def rec_fibb(n):
#    if n == 1:
#        print('n=1')
#        return 1
#    if n == 2:
#        print('n=2')
#        return 1
#    x = rec_fibb(n - 2) + rec_fibb(n - 1)
#    print(x)
#    return x
#
# rec_fibb(6)

# def sum_of_natural_numbers (numbers):
#     if numbers//10 == 0:
#         return numbers%10
#     return (numbers%10)+sum_of_natural_numbers (numbers//10)
#
# print(sum_of_natural_numbers (1111111111))

# def count(start=20000000,step=100):
#     counter = start
#     yield counter
#     counter += step
#     print(counter)
# a = count()
# print(next(a))
# print(next(a))

# def fib():
#     a = 0
#     yield a
#     b = 1
#     yield b
#     while True:
#         a, b = b, a + b
#         yield b
# f = fib()
# for i in range(10):
#     print(next(f))

# def decorator_function(wrapped_func):
#     print('Входим в декоратор')
#
#     def wrapper():
#         print('Выходим из декоратора')
#
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
#
# hello_world()
#
# hello_world()

# def number_of_calls(function):
#     n = 0
#     def wrapper():
#         nonlocal n
#         x = function()
#         n += 1
#         print(n)
#         return x
#     return wrapper
#
# @ number_of_calls
# def func():
#     print ("Ля-ля-ля!")
#
# func()
# func()

# def local_base(function):
#     dictionary = {}
#     def wrapper(n):
#         nonlocal dictionary
#         if n in dictionary:
#             print('взял из словаря')
#             print(dictionary)
#         else:
#             x = function(n)
#             dictionary[n] = x
#             print(dictionary)
#         return dictionary[n]
#     return wrapper
#
# @ local_base
# def f(n):
#    return n * 123456789
#
# print(f (1))
#
# print(f (1))
#
# print(f (2))

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# text = input('Введите текст для анализа \n')
# text = list((text.replace(' ','')).lower())
# print(text)

# text = """The Zen of Python
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# """
# text = text.replace("\n", " ")
# print(text)
# text = set(text)
# print(text)
# print(len(text))

# x = 110
# print(type(x))
#
# if type(x) == int and (100<=x<=999) and x%2==0 and x%3==0:
#     print("Бинго!")

# M = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(M)

# L = [not ((int(input('Введите четное или нечетное целое число \n')))%2) for i in range(2)]
# print(L)
# print(not all(L) and any(L))

# A = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# B = [i for i in range(10,0,-1)]
# # 10 9 8 7 6 5 4 3 2 1
# L = [a*b for a,b in zip(A,B)]
# print(L)

# text = "aaabbccccdaa"
# list_letters = []
# list_numbers = []
# list_letters.append(text[0])
# list_numbers.append(1)
# for i in range(1, len(text)):
#     if text[i] == text[i-1]:
#         list_numbers[-1] += 1
#     else:
#         list_letters.append(text[i])
#         list_numbers.append(1)
#
# # for a in zip(list_letters,map(str,list_numbers)):
# #     print(a)
#
# N = [a+b for a,b in zip(list_letters,map(str,list_numbers))]

# new_text = "".join(N)
# print(new_text)


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

# L = [4, 1, 2, 1, 2, 5, 6, 1]
# print(min_list(L))

# def number_e(n=1, step=100):
#      while True:
#         e_n = (1 + 1 / n) ** n
#         n += step
#         yield e_n
#
# e_n = number_e()
#
# # for i in e_n:
# #     print(i)
# for i in range(5):
#     print(next(e_n))

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещен")
#     return wrapper
#
# @is_auth
# @has_access
#
# def from_db():
#     print("some data from database")
#
# from_db()

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower,L)))

# def even_numbers(x):
#     return not x%2
# L = [-2, -1, 0, 1, -3, 2, -3]
#
# print(list(filter(even_numbers, L)))

data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]
# data.sort(key=lambda x: x[0]/(x[1]/100)**2, reverse=True)
# print(data)

new_data = sorted(data, key=lambda x: x[0]/(x[1]/100)**2)
print(new_data)

print(max(data, key=lambda x: x[0]/(x[1]/100)**2))
