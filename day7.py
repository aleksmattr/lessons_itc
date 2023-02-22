
# n = int(input('введите число:'))
# if n % 1 == 0 and n % n == 0:


# a = int(input('введите число:'))
# fact = 1
# n = []
# for i  in range(1, a+1):
#     fact += i
#     n.append(fact)
# print(fact)
# print(n)


# s = ['Sultan', 'Asik', 'Mars', 'Sasha', 'ERJ', \
#      'Alibek', 'Kirill', 'Rustam', 'Janbolat', 'Vlad']

# print({key: value for key, value in enumerate(s)})

# --------------

# s = []
# for i in range(100):
#     if i % 2 == 0 and i % 3 == 0:
#         s.append(i)
#     else:
#         s.append(0)
# print(s)

# print([i for i in range(100) if i % 2 == 0 and i % 3 == 0])
# print([i if i % 2 == 0 and i % 3 == 0 else 0 for i in range(100)])


# ------------------

# a = 1 if 3 > 2 else 0
# print(a)

# text = 'asdhhkasjhdkjasdhkasd'
# s = [i for i in text]
# print(s)



# s = {i:j for i, j in enumerate([1, 2, 3, 4, 5, 6, 7, 8])}

# print(s)

# s = ['Sultan', 'Asik', 'Mars', 'Sasha', 'ERJ', \
#      'Alibek', 'Kirill', 'Rustam', 'Janbolat', 'Vlad']

# dict_users = {}
# for key, value,  in enumerate(s):
#     dict_users[key] = value
# print(dict_users)

# print([i for i in range(100) if i % 2 == 0 and i % 3 == 0])
# print([i if i % 2 == 0 and i % 3 == 0 else 0 for i in range(100)])


# a = int(input('Введите число:'))
# b = input('Введите действие:')
# c = int(input('Введите второе число:'))

# if b == '+':
#     print(a + c)
# elif b == '-':
#     print(a - c)
# elif b == '*':
#     print(a * c)
# elif b == '/':
#     if c == 0 or a == 0:
#         print('нельзя делить на 0')
#     else:
#         print(a / c)
# elif b == '**':
#     print(
# (a ** c)
# elif b == '%':
#     print(a % c)
# else:
#     print('неверное выбранное действие') 

# a = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
# b = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
# w = [0]
                                     
# for h in range(1,10, 3):
#     for m in range(1,10):
#         print(f'{h} * {m} = {h*m} \t {(h+1)} * {m} = {(h+1)*m} \t {(h+2)} * {m} = {(h+2)*m}')
    
#     print()



# import time
# import os

# for h in range(60):
#     for m in range(60):
#         for s in range(60):
#             print(f'{h} : {m} : {s}')
#             time.sleep(0.1)
#             os.system('clear')




# a = []
# while True:
#     if 5 == len(a):
#         break
#     n = int(input('>>'))
#     if n % 2 == 0:
#         a.append(n)
#     else:
#         print('please repeat')

# print(a)

# a = [1, 2,3, 3,3]
# print(len(a))
# ------------------------------------------------------------

# a = []
# for _ in range(5):
#     n = int(input('nomber enter:'))
#     while n % 2 != 0:
#         print('please repeat:')
#         n = int(input('>>'))
#     else:
#         a.append(n)
# print(a)

# -------------------------------------------------------

# number = []
# n = int(input('Enter:'))
# while len(number) < 5:
#     if n % 2 == 0:
#         number.append(n)
#     n = int(input('Enter number:'))
# print(number)