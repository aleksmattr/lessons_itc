
# # pts
# users = []
# log = input('Введите логин:')
# if log.isdigit() != True and log.isalpha() != True:
#     pwd = input('Введите пароль:')
#     pwd2 = input('Подтвердите пароль:')
#     if pwd == pwd2:
#         a = (log, pwd)
#         users.append(a)
#         print(users)
#     else:
#         print('вы не подтвердили пароль')
# else:
#     print('ваш логин должен состоят из букв и цифр')
    

# # a = "124"
# print(a.isdigit())

# b = 'sfsf'
# print(b.isalpha())

# pt5
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
# a = int(input('Выберите индекс:'))
# print(list_1[a::])

# # prt4
# points = 0
# print('сколько океанов в мире')
# print('1 вариант - 1, 2 вариант - 4, 3 - вариант ни одного')
# a = int(input('Выберите вариант:'))
# if a == 2:
#     points += 1
#     print(points)
# print('сколько конт')
# print('1 вариант - 1, 2 вариант - 4, 3 - вариант ни одного')
# a = int(input('Выберите вариант:'))
# if a == 1:
#     points += 1
# print('сколько рек')
# print('1 вариант - 1, 2 вариант - 4, 3 - вариант ни одного')
# a = int(input('Выберите вариант:'))
# if a == 3:
#     points += 1
# print(points)
# if points >= 3:
#     print('Вы прошли тест')
# elif points == 1 or points == 2:
#     print('вы провалили тест попробуйте след раз')
# else:
#     print('вы не от ветили ни на один вопрос')


# pr3t

# products = ['Яблоко', 'Груша', 'Арбуз', 'Банан', 'Мандарин']
# print(products)
# a = int(input('Выберите индекс товара:'))
# a = a - 1

# if 0 <= a <= 4:
#     products.pop(a)
#     print(products)
# else:
#     print('не верный индекс')



# # pr2t
# list_1 = []
# a = int(input('Число 1:'))
# b = int(input('Число 2:'))
# c = int(input('Число 3:'))
# d = int(input('Число 4:'))
# e = int(input('Число 5:'))
# list_1.append(a)
# list_1.append(b)
# list_1.append(c)
# list_1.append(d)
# list_1.append(e)

# list_1.sort()

# q = len(list_1)
# y = sum(list_1)
# t = y / q

# print('Самое маленькое числоб', list_1[0], 'Самое большое число', list_1[-1], 'Среднеарефметическое число', t)




#p1t

# list_1 = []
# list_2 = []
# a = int(input('Число 1:'))
# if a % 2 == 0:
#     list_1.append(a)
# else:
#     list_2.append(a)
# b = int(input('Число 2:'))
# if b % 2 == 0:
#     list_1.append(b)
# else:
#     list_2.append(b)
# c = int(input('Число 3:'))
# if c % 2 == 0:
#     list_1.append(c)
# else:
#     list_2.append(c)
# d = int(input('Число 4:'))
# if d % 2 == 0:
#     list_1.append(d)
# else:
#     list_2.append(d)
# e = int(input('Число 5:'))
# if e % 2 == 0:
#     list_1.append(e)
# else:
#     list_2.append(e)
# print(list_1)
# print(list_2)


# problem7

# list_1 = []
# list_1.append(input('imya: '))
# list_1.append('1989')
# list_1.append('pyton')
# # a = ', '
# # print(a.join(list_1))
# print(list)




# problem4
# list_1 = [123, 1231, 1231]
# list_2 = [312, 312, 312]

# list_1.extend(list_2)

# print(list_1)

# problem3
# list = ['petr','aleks','dana']
# a = '99'
# print(a.join(list))


# problem 2
# list = []
# list.append(1)
# list.append('Hello')
# list.append(True)
# d = (1, 'world', 2, 3, 5)
# list.append(d)
# c = 1,5
# list.append(c)

# print(list)


# problem1
# a = (1, 2, 3)

# print(a[0])
# print(a[1])
# print(a[2])

# problem 0 
# list_1 = []
# a = (1, 2, 3, 4, 5)
# list_1.extend(a)

# print(list_1)

a = [1,2,3,3,4,5,7,8]
print(a.index(7))


# a = (1, 2,'sdfkjhsdkjf',True,  4, 5, 5, 5, 5, 5, 5)
# # print(a[2])
# b = []
# print(type(a))
# # print(type(b))
# # b = []
# b.extend(a)
# print(b)


# s1 = [1569,2,3,4, 8, 1, 4, 5, 4, 4, 5, 8, 4, 5, 4, 5]

# # s1.reverse()
# # print(s1)

# print(s1.count(4)) ищет количество четверок


# s1 = [1569,2,3,4, 4, 5, 4, 5, 4, 5, 4, 5]
# s2 = [15, 4, 5, 4, 5, 4, 5, 12]
# s1.append(s2) добавляет s2 в s1
# s1 += s2 добавляет в данные
# s1.extend(s2) добавляет данные лист
# s1.sort(reverse=True)
# print(s1)


# s = [1569,2,3,4,5,5,5, 4, 5, 4, 5, 4, 5, 4, 5]
# s.append(True)
# s.remove(1569)
# s.pop(0)
# print(s)


# s = [3, 4, 2, 4, 5, 5, 5, 4]
# s.append(66)
# s.append(True)
# s.append([123,123])
# print(s)

# a = [2, 3, 4, 5, 6, 7, 8, 1]
# a.reverse()

# print(a)