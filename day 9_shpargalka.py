# int = 12.   
# float = 1.2 
# bool = True
# string = "True"

# Массивы
# tuple = ('asd')
# list = []
# set = {}
# dict = {}

# list, set, dict = Изменяемые
# int, float, bool, string, tuple = Неизменяемые

# Ничего == None

# print(a > x) # True
# print(a < x) # False


# print(1, a + x) #это плюс
# print(2, a - x) #это минус
# print(3, a * x) #это умножение
# print(4, a / x) #это деление с остатками  = 12.9
# print(5, a // x) #это деление без остатков с округлением в меньшую = 12
# print(6, a % x) #это деление по модули = 9
# print(7, a ** x) #это степень = 123^10

# int = 1, 234, 4
# float = 1.4, 5.6, 8.88, 6.0
# bool = True, False

# a = 'hello'

# s = a.replace(' ', '') #заменяет все вхожддения 1 аргумента на 2 аргумент

# s = "hello i'm pythonmen n  n n n  n "

# s.title() # делает заглавной каждый первый символ
# s.upper() # вся враза заглавной
# s.lower() # все строчные
# s.capitalize() #Делает заглавной первый символ
# s.count('n') # #принимает один аргумент и возвращает (считает) количество
# s.sort() # сортирует в list по алфавиту и по цифрам 
# print(sorted(a)) #сортирует в ответе не меняя list
# list_1.extend(a)  #добавляет int или str в set или dict или list (изменяемые)
# a.append(b) #добавляет int или str в set или dict или list (изменяемые)
# a.add(10) #добавляет int или str (неизменяемы) в set или dict или list (изменяемые)
# s.remove(1569) # удаляет int str
# s.pop(0) #удаляет по индексу
# a.reverse() #меняет порядок <->
# a.isdigit() #возвращает True если все данные цифры
# a.isalpha() #возвращает True если все данные буквы
# '|'.join(a) #вставляет между буквами нужный вам символ
# len(a) # при помощи len() считает количество букв
# a.split() #при помощи split() из букв составляет слово от пробела до пробела
# print(len(b))  #c помощью split(), Len() считает только слова
# a.startswith('F') #ищет в начале слова  установленную букву, выдает (true false)
# range(0, 100) # диапазон, от 0 до 100
# type(a) # узнает класс 
# y = sum(list_1) #cуммирует цифры int float (неизменяемы) 
# a[0] #показать из листа по индексу
# a[::-1] #показать с конца
# a.discard(12) #отказаться в set или dict или list (изменяемые) от указанной  int или float ...
# a.clear() #очистить set или dict или list (изменяемые) от данных
# a.update({}) # обновить (не удаляя старые вносит новые) set или dict или list (изменяемые) от данных
# break #остановить цикл for while
# keys #ключ
# value #числитель
# intersection оставляет схожие в set dict удаляя уникальные
# difference удаляет схожие из set dict оставляя уникальные
# print(id(s)) #узнать id
# enumerate #перечисляет количесвто значений
# items #выводит keys and value

# all


# len()
# print()
# input()
# range()
# min()
# max()
# # (int(), str(), ...)
# type()
# id()
# sorted()
# reversed()
# exit()
# open()



# import #импортирует библиотеку
# OS 
# system
# Time
# max
# map



# a = ['asdasdad', 'asd', 'dsa'] or [1, 2, 3, 4, 5, 6, 7]
# print(a.index('asd'))  or print(a.index(7)) #выдает индекс выбранного числа или слова или буквы


# ---------------------------------------------------------------------------------------------------------
# Примеры

# a = int(input('Введите ваш возрас:')) # пример работы if 
# if a >= 18:
#     print('Совершеннолетний')
# elif a <= 4:
#     print('Ребенок')
# else:
#     print('несовершенолетний')



# ПРИМЕР калькулятора
# print("Вставте выражение из (+,-,/,*,**, //,%)")
# print("Для выключения калькулятора нажмите off")
# while True:
#     a = input('Введите выражение:')
#     if a == 'off':
#         print('Калькулятор выключен')
#         break
#     if a in '+-**//%' and not a == '': #== '+' or a == '-' or a == '*' or a == '//' or a == '**' or a == '%' or a == '/':
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



# ПРИМЕР цикла For задаешь ограничение в цикле
# a = 7
# for i in range(5):
#     a  = a * 7
#     print(a)


# ПРИМЕР ЦИКЛА while бескончено
# i = 0
# a = []
# while i <= 9:
#     i += 1
#     a.append(i)
# print(a)



#ПРИМЕР ЦИКЛА for и while перевода в одну строку
# s = []
# for i in range(100):
#     if i % 2 == 0 and i % 3 == 0:
#         s.append(i)
#     # else:
#     #     s.append(0)
# print(s)

# print([i for i in range(100) if i % 2 == 0 and i % 3 == 0])
# # print([i if i % 2 == 0 and i % 3 == 0 else 0 for i in range(100)])




#ПРИМЕР СОЗДАНИЯ ЛОГИНА И ПАРОЛЯ УСЛОЖНЕННЫЙ С ПРОВЕРКОЙ  В ФАЙЛЕ
# file = open('users.txt', 'r')
# text = file.read().split()
# login = input('Enter login: ')

# while True:
#     if login in text:
#         print('Логин уже существует, пожалуйста, авторизуйтесь!')  
#         password = input('Enter password:')
#         break
#     else:
#         password_1 = input('Enter password: ')
#         password_2 = input('Enter again password: ')
#         if password_1 == password_2:
#             file = open('users.txt', 'a')
#             file.write('\n')
#             file.write('\n')
#             file.write(f'login: {login}, password: {password_1}')
#             break
#         else:
#             print('Пароль не совпал')


# ПРИМЕР 
# intersection оставляет схожие в set dict удаляя уникальные
# difference удаляет схожие из set dict оставляя уникальные
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))
# print(farm_1.difference(farm_2))



#ПРИМЕР СОЗДАНИЯ СЕКУНДОМЕРА
# import time
# import os

# for h in range(60):
#     for m in range(60):
#         for s in range(60):
#             print(f'{h} : {m} : {s}')
#             time.sleep(0.1)
#             os.system('clear')


# ПРИМЕР СОЗДАНИЯ ФАЙЛА txt и ввести текст вносить цифры
# file = open('werw.txt', 'a')
# text = 'Hello, world'
# s = '\n'
# for i in range(10):
#     s += str(i)
# file.write(s)
# file.close()


#ПРИМЕР СОЗДАНИЯ ПОИСКА ПО ЧТЕНИЮ ФАЙЛА
# file = open('files.txt', 'r')
# s = 0
# text = file.read().split('\n')
# for i in text:
#     if 'day' in i: #(варианты поиска)
#         s += 1


#ПРИМЕР ОТКРЫТИЯ ФАЙЛА  тхт ЗАПИСЬ В ФАЙЛ С НУЛЯ
# with open('user.txt', 'w') as file:
#     a = input ('Введите логин:')
#     b = input ('Введите пароль:')
#     file.write(f" Логин: {a} Пароль: {b}")



#  print(all([True]))
# print(any([True, False, False, False]))


# while 2 == 4: print(eval(input('>>')))

# list = [1,4,6,8,9,10, True, [], ()]
# list.append()
# set = {1,1,4,5}
# set.add()
# dict = {'1':2}
# dict.update()

# tuple = (123, 12, 23)
# n = 123
# try:
#     tuple.index(n)
#     tuple[123]
# except (ValueError, IndexError) as e:
#     print(f'{n} not in tuple', e)

# except NameError:
#     print(f'Name is not defined')
# else:
#     print(tuple.index(n))
# finally:
#     print('Finished')

# print('asdjlajksd')



# list = []
# list.append(2)
# list.append(4)
# print(list)


# a = ['sfs', 'sdff', 'sdff']
# s= list(map(len, a))
# print(s)