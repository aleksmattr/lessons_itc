
# def add(a,b):
#     return a+b

# print(add(1,2))


# def substruct(a,b):
#     return a-b

# print(substruct(1,2))



# def multiply(a,b):
#     return a*b

# print(multiply(1,2))


# def divide(a,b):
#     return a/b

# print(divide(1,2))


# задача 2
# def lenden(a):
#     word = 0
#     for i in a:
#         word += 1
#     return word, a

# print(lenden("jhgh"))

# задание 3

# def ololo(dict1, dict2):
#     for key, value in dict2.items():
#         dict1[key]=value
#     return dict1


# d = {'q': 123}
# a = {'a': 987}

# print(ololo(d, a))


# Задание 4

# from os import system
# def menu(food, drink):
#     file = open('/Users/aleksandrslepcov/Desktop/menu.txt', 'a')
#     file.write(f'\n {food}')
#     file.write(f'\n {drink}')
#     file.close()
    

# food = (input("choised food:>>>"))
# drink = (input("choised drink:>>>"))


# menu(food, drink)

# задание 5


# def underdog(a):
#     from os import system
#     system(f'touch {a}.txt')
    

# HHH = (input("имя файла:>>>"))
# underdog(HHH)


# Задание 6

# def add():
#     return print('Я вложенная функция')

# def substruct(d):
    
#     return print(f'Я главная функция{add()}')

# substruct(1)


# Задание 7

# def kanzas(a):
#     for key, value in a.items():

#         print(key, value)
        

# dict1 = {'under': 'dog', 'super': 'cat', 'triple': 'Kork'}
# a, b = kanzas(dict1)



# Задание 8 
lst = []
for i in range(100):
    if i % 2 == 0: # and i % 1 == 0:
        lst.append(i)
print(lst)







# функции

# def main(stop, start=0, step=1):
#     return list(range(start, stop, step))
# print(main(10))


# def selery(salary, percent=12):
#     print(salary * percent)

# selery(15000)
# selery(salary=15000, percent=15)




# def main(*students):
#     return sum(students) / len(students)
# a = main(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# print(a)


# def avg(**kwargs):
#     for i in kwargs.values():
#         print(i)

# avg(name='Sultan', age=30, language='python')




# a = (1,1,3,5,7,9,0,7)

# def avg(*args):
#     print(args)

# avg(*a)


# def avg(**kwargs):
#     for i in kwargs.values():
#         print(i)


# data = {
#     'name':'Sultan', 
#     'age':30, 
#     "language":'python'
# }

# avg(**data)
# avg(name='Sultan', age=30, language='python')


# def my_function(*args, **kwargs): 
#     for a in args: 
#         print(a, end=". ") 
  
#     print() 
  
#     for key, value in kwargs.items(): 
#         print("%s = %s" % (key, value), end=' ') 


# data = {
#     'name':'Sultan', 
#     'age':30, 
#     "language":'python'
# }
# a = (1,1,3,5,7,9,0,7)

# my_function(*a, **data)


# def add_numbers(*args): 
#     total = 0
#     for a in args: 
#         total += a 
#     return total 

# a = (1,1,3,5,7,9,0,7)
# b = (1,1,3,5,7,9,0,7)

# print(add_numbers(*a, *b))


# def anyArgs(arg1=1, *vartuple, **kwargs): 
#     print("Output is:")  
#     print(arg1) 
#     for var in vartuple: 
#         print(var)  


# anyArgs(12,12,3)



# def calculate(**kwargs): 
#     if 'operation' in kwargs: 
#         operation = kwargs['operation'] 
#         if operation == 'add': 
#             if 'num1' and 'num2' in kwargs: 
#                 return kwargs['num1'] + kwargs['num2']

#             else: 
#                 return "Cannot perform Addition. Missing arguments!" 

#         elif operation == 'sub': 
#             if 'num1' and 'num2' in kwargs: 
#                 return kwargs['num1'] - kwargs['num2'] 

#             else : 
#                 return "Cannot perform Subtraction. Missing arguments!" 

#         else: 
#             return "Invalid input."

# print(calculate(operation='addasd'))

