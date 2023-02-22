# задание1

# while True:
#     b = input("""
# Выберите действие
# +
# -
# *
# **
# //
#  %
# /
# 8: Выключить Калькулятор
# >>> """)
#     if b == '8':
#         break
#     a = int(input('введите цифру:'))
#     c = int(input('введите цифру:'))

#     if b == '+':
#         print('Результат = ',a + c)
#     elif b == '-':
#         print('Результат = ',a - c)
#     elif b == '*':
#         print('Результат = ',a * c)
#     elif b == '/':
#         if c == 0 or a == 0:
#             print('нельзя делить на 0')
#         else:
#             print('Результат = ',a / c)
#     elif b == '**':
#         print('Результат = ', a ** c)
#     elif b == '%':
#         print('Результат = ', a % c)
#     elif b == '//':
#         print ('Результат = ', a // c)
#     else:
#         print('неверное выбранное действие')



# Вторая задача
# users = [ ]
# a=input('Login:')
# b=input('Password:')
# users.append(f'{a,b}')
# print(users)

# print('Пожалуйста войдите в свой аккаунт')
# c=input('Login:')
# d=input('Password:')

# if c == a and d == b:
#     print('Добро пожаловать')
# else:
#     print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')







#задача3
# dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}

# # for i, j in dict1.items():
# #     if j % 3 == 0:
# #         print(f'{i} = Hi')
# #     elif j % 5 == 0:
# #         print(f'{i} = Bye')

# for i, j in dict1.items():
#     if j % 5 == 0:
#         print(i, 'Bay')
#     elif j % 3 ==0:
#         print(i, 'Hi')




#zadacha4
# list = []
# diapazon = int(input('ot 0 do >>  '))
# result = 0
# for i in range(diapazon):
#     if i % 3 == 0 or i % 5 == 0:
#         list.append(i)

# for j in range(len(list)):
#     result += j

# print(result)




# #задача 5
# n = list(map(int, input('>> ')))
# res_num = 0
# for i in n:
#     res_num += i
# print(res_num)


#zadacha6

# vvod = input('vvedite datu v formate yyyy-mm-dd hh:mm   ')
# dct = {}

# for line in vvod:
#     date, time = vvod.split()

# for i in date:
#     year, month, day = date.split('-')
# for j in time:
#     hour, minute = time.split(':')

# dct = {
#     'god' : year,
#     'mesyac' : month,
#     'den' : day,
#     'chas' : hour,
#     'minuty' : minute
# }

# print(date, time, year, month, day)
# print(dct)







# #задача 7
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# for i in words:
#     if i[::-1] == i:
#         print(f'{i} - полиндром')
#     else:
#         print(f'{i} - не полиндром')




# задание 8

# a = input("Введите строку: ")
# b = a.split()
# c = max(len(word) for word in b)
# d = [word for word in b if len(word) == c]
# print("Самые длинные слова:", d)




# zadacha 9
# n = int(input('Number: '))
# for a in range(2,n + 1 ):
#     for i in range(2,a):
#         if (a%i==0):
#             break
#     else:
#             print(a)





# zadacha 10
# n = input(">> ")
# n1 = []
# a = set()

# for i in n:
#     if i in a and i not in n1:
#         n1.append(i) 
#     else:
#         a.add(i)  

# print("Уникальные числа: ", n1)






#задача 11
# str = input('Введите строку: ')
# char = input('Введите символ: ')

# print(str.count(char))






# zadacha 12

# a = int(input("Number1:"))
# b = int(input("Number2:"))

# c=max(a,b)

# while True:
#     if c % a == 0 and c % b == 0:
#         print(f"Наименьшее общее кратное: {c}")
#         break
#     c += 1






# задача 13
# n = input("Введите числа ").split()
# n1 = []
# a = set()

# for i in n:
#     if i not in a and n.count(i) == 1:
#         a.add(i)
#         n1.append(int(i))

# print("Уникальные числа: ", n1)




# zadacha 14
# a = input('Введите строку:')
# b = set()

# for i in a.lower():
#     if i.isalpha() and i.lower() in "abcdefghijklmnopqrstuvwxyz":
#         b.add(i)

# if len(b) == 26:
#     print("Содержит все англиские буквы")
# else:
#     print("Содержит не все англиские буквы")





# # #zadacha15
# a = input('vvodi cherez probel  ')
# b = input('vvodi cherez probel  ')

# lst1 = a.split()
# lst2 = b.split()

# lst3 = list(set(lst1).intersection(lst2))
# print(lst1)
# print(lst2)
# print('peresechenie spiskov', lst3)