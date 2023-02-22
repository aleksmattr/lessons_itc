
from os import system


file = open('test.txt', 'a')
text = 'Hello, world'
# s = '\n'
# for i in range(10):
#     s += str(i)
file.write(text)
file.close()




# ls / >> files.txt
# ls > files.txt записать в файле


# file = open('files.txt', 'r')
# s = 0
# text = file.read().split('\n')
# for i in text:
#     if i.startswith('day'): #(варианты поиска)
#         s += 1


# file = open('files.txt', 'r')
# s = 0
# text = file.read().split('\n')
# for i in text:
#     if 'day' in i: #(варианты поиска)
#         s += 1


 # file = open('files.txt', 'r')
# s = 0
# text = file.read().split('\n')
# for i in text:   
#     # if i.find('day') >= 0:(варианты поиска)
#     #     s += 1


# file = open('files.txt', 'r')
# s = 0
# text = file.read().split('\n')
# for i in text:
#     # if i[0:3] == 'day':(варианты поиска)
#     #     s += 1

# print(s)

# print(file.read())


# with open('files.txt', 'w') as d:
#     d.write('asd')

# with open('files.txt', 'r') as d:
#     text = d.read().splitlines()
#     for i in text:
#         print(i)


# from os import system as s
# s('ls / > problem_1.txt')


# with open("Problem_1.txt", "r") as file:
#     all_d = file.read()
#     print(all_d)


# with open('user.txt', 'w') as file:
#     a = input ('Введите логин:')
#     b = input ('Введите пароль:')
#     file.write(f" Логин: {a} Пароль: {b}")



# file = open('user.txt', 'r')
# text = file.read().split('\n')
# for i in text:
#     if 'w' in i:
#         print('В тексте есть W')
#     else:
#         print('В тексте нет W')

# with open('python.txt', 'w') as file:
#     file.write("""Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.
# """)

# wird = []
# with open("python.txt", "r") as file:
#     for i in file.read().split():
#         if 't' in i or 'T' in i:
#             wird.append(i)
# print(wird)





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



