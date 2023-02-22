
# pr9
# b = list(range(-100 , 100+1))
# v = []
# for i in b:
#     if i % 13 == 0 and i  % 2 == 0:
#         i = i * i
#         print(i, end= ' ')
# v.extend(b[::7])
# for a in v:
#     if a % 2 == 0:
#         print(a, end= ', ')
# a.



# a = [-100 + x for x in range(200)]

# for i in a:
#   if i % 13 == 0 and i % 2 == 0:
#     print(i ** 2, end=' ')
# if i % 7 == 0 and i % 2 != 0:
#     print(i, end=' ''\n')

# a1 = 0
# for i in a:
#   if i % 13 == 0 and i % 2 == 0:
#     a1+=1
    
# a2 = 0
# for i in a:
#   if i % 7 == 0 and i % 2 != 0:
#     a2+=1

# print("Чисел подходящих под 1-ое условие: {}".format(a1))
# print("Чисел подходящих под 2-ое условие: {}".format(a2))



# b = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
# v=[]
# v.extend(b[::7])
# print(v)

# b = 56
# if b % 2 ==0:
#     print(b)

        # for a in i:
        #     if a.index(i) % 2 == 0:
        #         print(i)

# i = 0
# for b == range(-100, 100):
#     if b % 2 == 0:
#         print(b)
#     else:
#         print('asd')


# pr8
# a = 169
# print(a)
# if a % 2 == 0 and a >= 1:
#     print('Число является положительным и четным')
# else:
#     print('Число не выполнило условие')
# if a % 31 == 0:
#     print('Число делится на 31')
# else:
#     print('число говно')
# if a >= 100 and a % 17 == 0:
#     print('число делится больше 100 и делится на 17')
# else:
#     if a >= 150 and a == 13**2:
#         print('число делится больше 150и делится на 1')
#     else:
#         print('nety')

# for i in range(100,1000):
#     if 99<i<1000:
#         if i*-1<0 and i%2==0:
#             if i%31==0:
#                 if i>100 and i%17==0:
#                     print(i)
#                 elif i>150 and i==169:
#                     print(i)
#                 else:
#                     print('Такого числа не существует')
#                     break


# a = 13**2
# b = 312
# if a == b:
#     print(b, 'sdfs')
# else:
#     print(b, 'норма')

# pr6 - 7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names:
#     if names.index(i) % 2 == 0 :
#         print(i)



# pr3
# a = 7
# for i in range(5):
#     a  = a * 7
#     print(a)


# # pr5
# # i = 0
# # a = []
# # while i <= 9:
# #     i += 1
# #     a.append(i)
# # print(a)


# n = 10
# n = n* 2+1

# for i in range(1, n):
#     if i < n // 2:
#         print(i, end=' ')
#     if i > n // 2:
#         print(n - i, end=' ')

# print()





# pr4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# b = 0
# for i in languages:
#     print(b, i)
#     b += 1

# pr2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# lang1 = 'php'
# for i in languages:
#     if i == lang1:
#         print(i)
#         break


# # pr1
# lang1 = 'ruby'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

# for i in languages:
#     if i == lang1:
#         print('this languages is in listi')
#         break


# --------------------------------------------------------------------------------------------
# for 
# while

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# b = 0 

# for i in a:
#     if i ==5:
#         print('break')
#         break
#     b += i
#     print(i)

# print(b)


# b = list(range(-100 , 101))
# print(b)
# if b % 13 == 0:
#     print(b)



# a  = [1, 2, 3, 4, 5, 6, 7, 99, 8, 9]
# mx = a[0]
# for i in a:
#     if i >= mx:
#         mx = i
# print(mx)

# n = 0
# for i in range(10+1):
#     if i == 5:
#         continue
#     n += i
# print(n)

a = {'key': 'value', 'name': 'alex'}
for i in a:
    if i == 'name':
        print(a[i])
    print(i, a[i])

# i = 0 
# while i <= 10:
#     print(i, 'hello world')
#     i += 1

# password1 = input('Enter password1:')
# password2 = input('Enter password2:')
# i = 0
# while password1 != password2:
#     i += 1
#     if i == 5:
#         print('Повторите попытку через 10 мин')
#         break

#     print('повторите еще раз')
#     print(f'у вас осталось попыток: {5-i}')
#     password1 = input('Enter password1:')
#     password2 = input('Enter password2:')
# else:
#     print('successfuly')













