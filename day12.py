# Модули в пайтоне
# os, sys, random, time, datetime, string, math
# os управляет операционной системой
 

# import os
# print(os.name)
# os.system('ls /')
# -------------------------------
# code = """
# import os
# os.system('Ls / > data.txt')
# """
# with open('virus.py', 'w') as f:
#     f.write(code)

# os.system('python3 virus.py')
# os.system('rm -rf virus.py')

# ---------------------------------------

# import sys
# if sys.argv[1] == 'run':
#     print('Running')
# elif sys.argv[1] == 'test':
#     print('Testing')

# ------------------------------------------


# from random import choice, randint, randrange

# wc = randint(1, 100)
# print(wc)

# print(randrange(1, 100, 2))

# names = ['always', 'asik', 'kirill']
# print(choice(names))
# names.remove(choice(names))
# print(names)

# from string import ascii_letters, printable, punctuation, digits
# # print(choice(ascii_letters))

# # a = []
# # while len(a)< 8:
# #     a.append(choice(ascii_letters))

# # print(''.join(a))


# # a = []
# # while len(a)< 8:
# #     a.append(choice(printable))

# # print(''.join(a))

# print(''.join(choice(ascii_letters+digits+punctuation) for _ in range(8)))


# ----------------
# import time
# import datetime

# today = datetime.datetime.today()
# print(today)


# import time
# from datetime import datetime
# today = datetime.today()
# print(today.strftime('%d %m %Y %H:%M'))


# import time
# from datetime import datetime

# s= datetime(year=1989, month=1, day=16, hour=6)
# today = datetime.today()
# print(today - s)

# ------------------------------------------------------------------------

# Задание 1
# import os
# a = os.system('ls /')
# print(a)

# from os import system
# print(system('ls /'))

# Задание 2
# import sys
# from sys import argv

# if argv[1] == 'Jombulat':
#     print('Hello Jombulat')
# elif argv[1] == 'Alibek':
#     print('Hello Alibek')
# elif argv[1] == 'Vladislav':
#     print('Hello Alibek')

# names = ['Rustam', 'Kirill', 'Adlet', 'Erzhan', 'Aleksandr', 'Aslanbek', 'Vladislav', 'Alibek', "Zhomart"]

# Задание 3

# import random
# from random import choice
# while True:
#     a = choice(range(1,11))
#     m = int(input('Угадайте число:'))
#     if a == m:
#         print(f'Вы угадали число загаданное компьютером {a}, Ваше число {m}')
#     else:
#         print(f'Вы не угадали число загаданное компьютером {a}, Ваше число {m}')

# Задание 4



