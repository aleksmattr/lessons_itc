
# pr27
# dic = {'gino': 'striker', 'kuzy': 'striker', 'vasy': 'goltender', 'ovi': 'forward', 'sid': 'Center'}



# pr31
# dis = {}
# q = input('введите имя:')
# w = input('введите пароль:')
# e = input('введите имя:')
# r = input('введите пароль:')
# t = input('введите имя:')
# y = input('введите пароль:')

# dis.update({q : w})
# dis.update({e : r})
# dis.update({t : y})

# print(dis)
# print(dis.keys())



# pr020
# Set = {"add", "remove", "clear", "update", "differecce", "discard", 
# "intersection", "intersection_update", "pop"}
# dis = {"clear", "keys", "items", "get", "values", "update", "tuple", 
# "list", "set", "dict"}
# print(Set.intersection(dis))



# pr10
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({'напитки': ["coca-cola", "sprite", "fanta"]})
# print(menu)

# pr000
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({'besh': 130})
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)

# pr3
# farm = {'rmd', 'livp', 'manutd', 'mancity', 'psj'}
# farm.update(['bavaria'])
# print(farm.pop())
# print(farm)


# pr2
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# print(farm_2.difference(farm_1))

# pr1
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))


# Pr0
# dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)


# # Список № 2
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil',
#  'Chile', 'Colombia',
#   'Ecuador', 'Guyana', 
#   'Paraguay', 'Peru', 
#   'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

# print(south_american_countries.index('Argentina'))

# south_american_countries.pop(0)

# print(south_american_countries)




# int = 12.   
# float = 1.2 
# bool = True
# string = "True"

# Массивы
# tuple = ('asd')
# list = []
# set = {}
# dict = {}

# s = {1,1,2,2,2,2,45,6,77,7,7,7,7,1,1,1}
# print(s)

# list, set, dict = Изменяемые
# int, float, bool, string, tuple = Неизменяемые

# a = set()
# a.add(10)
# a.add('asd')
# a.add(1324)
# a.add(3)
# a.add(4234)
# a.add(53463)
# a.add(7)


# a.pop()
# a.pop()
# a.pop()

# print(a)

# a = 23
# b  = 32
# s = a + b
# print(id(b))
# print(id(s))




# a1 = [1,4,2,5,6]
# a2 = [1,4,14,5]

# a1 = set(a1)
# a2 = set(a2)

# a3 = a1.difference(a2)
# a4 = a1.intersection(a2)


# print(a4)

# a = {1,3,8, 4}
# b = {23, 4, 1}

# # print(a)
# a.intersection_update(b)
# # b = a
# # print(b)
# # print(a)
# # print(a)
# print(a.intersection(b))
# print(a)

# print()
# len()
# input()
# int()


# Ничего == None


# a = len('kjdshfkjdshfkj')

# print(a)


# a = [1,1,1,1,1, 2, 3, 4, 5, 6, 7]

# b = a.count(1)
# s = a.append('asdasd')
# print(s)
# print(a)
# print(b)


# a = [1,6,44,87,3,5,6,8]

# print(sorted(a))
# print(a)
# a.sort()
# print(a)

# print(a)
# print(a)

# a = {12,56,6,7,8,9}

# a.remove(12312)
# # a.clear()
# # a.pop()
# # a.discard(12)

# print(a)

# a.pop()
# a.pop()

# print(a)


# a = ['Alex', 18]
# print(a[0], a[1])

# list, set, dict = Изменяемые
# int, float, bool, string, tuple = Неизменяемые

# a = {
#     'name': 'Alex',
#     'age': '12',
#     'name': 'asd'
#     }
# print(a)



# users = {
#     'asik': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'kirill': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
# }

# users = [
#     ['asik', ['a@gmail.com', 'asdads', '7790454545']],
#     ['kirill', ['a@gmail.com', 'asdads', '+7790454545']],
# ]


# print(users['asik'])

# print(users[1][1])





# users = {
#     'asik': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'kirill': {
#         'email': 'a@gmail.com',
#         'password': 'asdads',
#         'phone': '+7790454545'
#     },
#     'erj': {''}
# }


# users.update({
#     'asdasd': 'asd'
# })

# users['kirill']['phone'] = '700000000000'

# print(users.keys())
# print(users)



# a = {
#     'Kirill': 18
# }

# a.update({
#     'erj': 19
# })

# a.update({
#     'asik': 231,
#     'qweqw':'qwe'
# })

# print(a.items())