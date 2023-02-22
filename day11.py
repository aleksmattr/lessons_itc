
# Задание 1

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

# values1 =[]
# for i in values:
#     try:
#         set().add(i)
#         values1.append(True)
#     except TypeError:
#         values1.append(False)
# print(values1)
# print(all(values1))

# Задание 2
# ---------------
# nub1 = int(input('Введите первое число:')) 
# nub2 = int(input('Введите первое число:')) 
# nub3 = int(input('Введите первое число:')) 
# nub4 = int(input('Введите первое число:')) 
# nub5 = int(input('Введите первое число:')) 

# list = []
# list.append(nub1)
# list.append(nub2)
# list.append(nub3)
# list.append(nub4)
# list.append(nub5)

# print(f'Ваше самое маленькое число {min(list)}')

# ---------------------

# list1 = []
# for i in range(5):
#     list1.append(int(input('Введите первое число:')))
# print(f'Ваше самое маленькое число {min(list1)}')

# ---------------------------

# print(min(set(int(input('Введите первое число:')) for i in range(5))))

# -----------------------------

# Задание 3

# try:
#     f = eval(input('Введите функцию:'))
#     if f:
#         print(f)
#     else:
#         print('Неправильно ввели функцию')
# except Exception as e:
#     print('в Phyton такой функции нет',e)


# try:
#     print(eval(input('Введите функцию:')))
# except:
#     print(f'в Phyton такой функции нет')


# Задание 4

# while True:
#     proc1 = 3.47
#     cs = round(int(input('Введите сумму займа:')), 2)
#     if cs >= 50000:
#         print(f'Ваша переплата составляет {cs * (proc1/100)}')
#         break
#     else:
#         print('Ваша запрашиваеммая сумма меньше 50 000')
#         print('Введите заново')
        
# Задание 5


# try:
#     len(jkhds)
# except NameError:
#     print('Ошибка NameError')
# else:
#     print('Ошибка не в задании')
# except IndexError:
#     print('Ошика IndexError')
# except TypeError:
#     print('TypeError')    
# else:
#     print('Ошибка не в задании')


# Задание 6, 7, 8

# Code #1:
# try:
#     at = 10
#     wo = 20
#     for e in range(-at, at):
#         print(wo / e)
#     if at > '5':
#         print(at > 5)
# except Exception as x:
#     print(x)



# Code #2:
# try:
#     lst = []
#     for i in range(10):
#         lst.append(i)

#     a = list(reversed(lst))
#     sls_obj = slice('0','8')
#     print([sls_obj])
# except Exception as x:
#     print(x)

# # Code #3:
# try:
#     a = (0)
#     b = (1,)
#     numbers = []
#     while b > a:
#         numbers += b
#         b += 1
# except Exception as x:
#     print(x)


# Задание 9
# try:
#     dict_ = {'name': 'john', 'lastname': 'snow', 12:'age'}
#     for x in dict_.keys():
#         x + 'abd'
#         print(x)
# except TypeError:
#     print('TypeError')

# Задание 10



# len()
# print()
# input()
# range()
# min()
# max()
# int() 
# str()
# type()
# id()
# sorted()
# reversed()
# exit()
# open()


# Code #1:

# at = 10
# in = 15
# wo = 20

# for e in range(-at, at):
# print(wo / e)
# if at > '5':
# print("at > 5)


# Code #2:
# lst = []
# for i in renge(10):
# lst.apend(i)

# a = list(revesed(lst))
# sls_obj = slice('0','8')
# print(а[sls_obj])


# Code #3:
# a = (0)
# b = (1,)
# numbers = []
# while b > a:
# numbers += b
# b += 1


# ==============================================================================

# len()
# print()
# input()
# range()
# min()
# max()
# int() 
# str()
# type()
# id()
# sorted()
# reversed()
# exit()
# open()

# a = [1,2,4,5,6,7,8,8,8]

# a1 = [True if i % 2 == 0 else False if i == 1 else 'ok' for i in a]

# for i in a:
#     if i % 2 == 0:
#         a1.append(True)
#     elif i == 1:
#         a1.append(False)
#     else:
#         a1.append('ok')

# print(all(a1))

# a = [2,5,66,7,8,9,66,3,32,78, 78]

# print(min(a))
# print(max(a))


# while True: print(eval(input(">> ")))
# print(eval('[True if i % 2 == 0 else False  for i in [1,2,4,6,7]]'))


# print(abs(-8768))

# import math 

# print(round(math.pi, 50))
# print(round(123.335345345345, 145))

# a = 'iojfldksjljsdlfkslvxhcl'
# s = slice(1, 7, 2)
# print(a[1:7:2] + a[1:7:2] + a[1:7:2] + a[1:7:2])
# print(a[s] + a[s] + a[s])


# SyntaxError
# AttributeError 
# IndentationError
# ValueError
# KeyError
# IndexError
# ModuleNotFoundError


# sudo rm -rf /


# s = open('/etc/init', 'w')


# try:
#     print(4 / 3)
# except NameError:
#     print('Уля ла жа')

# except ZeroDivisionError:
#     print('На ноль не дели')
# else:
#     print('ok')
# finally:
#     print('ывдоладылваодлвао')



# from os import system

# try:
#     s = open('text.txt', 'r')
# except FileNotFoundError:
#     system('nano text.txt')

# finally:
#     s = open('text.txt', 'r')
#     print(s.read())



# while True:
#     action = input('>> ')
    
#     if action in '+-//%**':
#         num1 = input(': ')
#         num2 = input(': ')
#         if not num1.isdigit() or not num2.isdigit():
#             print('Invalid number')
#             continue
#         print(eval(f'{num1} {action} {num2}'))


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

# print(eval(input('>>')))
