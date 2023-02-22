
# a = [1, 3, 4, 6, 7 ,8]

# def length(a: list) -> int:
#     count = 0
#     for _ in a:
#         count += 1
#     return count
# s = length(a)
# print(s)
# print(len(a))

# def main(a, b):
#     return a + b
# print(main(30,12))
# s = main(12, 33)
# print(s)


# from random import choice
# from string import ascii_letters, digits
# import os
# import time

# def generate_password(n: int):
#     return ''.join(choice(ascii_letters+digits)for _ in range(n))


# def loading():
#     for i in range(1, 4):
#         os.system('clear')
#         print('Generating password' + '.' * i, i*33, '%')
#         time.sleep(0.5)




# loading()
# pas = generate_password(13)
# print(pas)


# def validate_login(login: str) -> bool:
#     for i in login:
#         print(i)
#         if i not in ascii_letters+digits:
#             return True


#     if not login.isdigit() and not login.isalpha(): # обрантое тру
#         return True
#     return False
    
# # def validate_login(login: str) -> bool:
# #     return True if not login.isdigit() and not login.isalpha() else False

# print(validate_login('asdasd123'))

# задание 1

# list = [1, 2, 3, 4, 5, 6, 'batman', 'superman']

# def reverse_list(list):
#     mid = len(list) // 2
#     list1 = list[:mid][::-1]
#     list2 = list[mid:][::-1]
#     return list1 + list2
# print(reverse_list(list)
# 
# задание 2

# def fibgen(n): 
#     a, b = 1, 1
#     for _ in range(1,n):
#         print(a, end=' ')
#         a, b = b, a + b
# fib_list = fibgen(10)


# задание 3

# def pervayaf(a, b):
#     return a * b

# def vtorayaf(a,b):
#     return a / b

# def glavn(a,b):
#     print(pervayaf(a,b))
#     print(vtorayaf(a,b))

# a = 5
# b = 6
# glavn(a,b)

# задание 4
# from os import system
# name = input('Введите имя файла:')
# def instal(name):
#     system(f'touch {name}.txt')
# instal(name)

# задание 5

# from random import choice

# def gen_number():
#     lst =[]
#     for _ in range(5):
#         a = choice(['1', '4', '5', '7', '9', '0'])
#         lst.append(a)
#     return f" 0444{''.join(lst)}"
   
# a = gen_number()
  
# print(f'{a}')
