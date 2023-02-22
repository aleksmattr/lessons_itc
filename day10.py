# Задание 1

# print("Вставте выражение из (+,-,/,*,**, //,%)")
# print("Для выключения калькулятора нажмите off")
# while True:
#     a = input('Введите выражение:')
#     if a == 'off':
#         print('Калькулятор выключен')
#         break
#     if a == '+' or a == '-' or a == '*' or a == '//' or a == '**' or a == '%' or a == '/':
#         n = input('Введите первое число 1:')    
#         m = input('Введите второе число 2:')
#         if not n.isdigit() or not m.isdigit():
#             print('Вы ввели ')
#             continue
#         b = int(n)
#         c = int(m)
#         if a in '-':
#             print(f'{b} {a} {c} = {b - c}')    
#         elif a in '+':
#             print(f'{b} {a} {c} = {b + c}')
#         elif a in '*':
#             print(f'{b} {a} {c} = {b * c}')
#         elif a in '/':
#             if b == 0 or c == 0:
#                 print('Нельзя делить на НОЛЬ (0)') 
#             else:
#                 print(f'{b} {a} {c} = {b / c}')
#         elif a in '//':
#             if b == 0 or c == 0:
#                 print('Нельзя делить на НОЛЬ (0)') 
#             else:
#                 print(f'{b} {a} {c} = {b / c}')
#         elif a in '%':
#             if b == 0 or c == 0:
#                 print('Нельзя делить на НОЛЬ (0)') 
#             else:
#                 print(f'{b} {a} {c} = {b / c}')
#         elif a in '**':
#             print(f'{b} {a} {c} = {b ** c}')
#     else:
#         print('Выбранное вами выражение не существует, попробуйте снова')

# Задание 2

# users = []
# print('Прошу зарегистрироватся')
# login = input('Ведите Login:')
# password = input('Введите Password:')
# users.append({'login': login, 'password':password})

# print('Войдите в свой аккаунт')
# login2 = input('Ведите Login:')
# password2 = input('Введите Password:')
# for i in users:
#     if i['login'] == login2 and i['password'] == password2:
#         print('ДОБРО ПОЖАЛОВАТЬ ')
#     else:
#         print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')

# Задание 3

# dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}
# for i, j in dict1.items():
#     if j % 5 == 0:
#         print(i, 'hi')
#     elif j % 3 == 0:
#         print(i, 'bay')

# Задание 4

# numb1 =[]
# numb2 = []
# for i in range(1000):
#     if i % 3 == 0:
#         numb1.append(i)
# for i in range(1000):
#     if i % 5 == 0:
#         numb2.append(i)
        
# print(f'сумма кратных 3 равна {sum(numb1)}')
# print(f'сумма кратных 5 равна {sum(numb2)}')
# _______________________________________________________

# print(f'сумма кратных 3 равна {sum(i for i in range(1000) if i % 3 == 0)}')
# print(f'сумма кратных 5 равна {sum(i for i in range(1000) if i % 5 == 0)}')
        

# Задание 5
# list1 = 4729461084

# import math
# n = 4729461084
# x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
# print(sum(x))

# str1 = str(4729461084)
# # initializing substring
# A = 1
# # create a result list
# result = []
# for i in range(0, len(str1), A):
#     # convert to int, after the slicing process
#     result.append(int(str1[i : i + A]))
  
# print("The resultant list : " + str(result))
# list2 = sum(list(map(list1)))
# print(list1)

# Задание 6
# data1 = input('Вставьте дату в формает ГГГГ-ММ-ДД ЧЧ:ММ:')
# data1 = (data1.replace('-', ' ').replace(':', ' ').split())
# data = {'Year':'' ,
# 'mounth': '',
#  'day': ' ',
#   'hour':' ',
#    'minutes' : ''}

# data.update({'Year': data1[0],'mounth': data1[1], 'day': data1[2], 'hour': data1[3], 'minutes' : data1[4]})

# print(data)

# Задание 7
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# for i in words:
#     if i[::-1] == i:
#         print(f'{i}  - слова полиндром')
#     else:
#         print(f'{i}  - слова неполиндром')

# Задание 8
