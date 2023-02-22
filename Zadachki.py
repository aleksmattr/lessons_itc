# import random
# from random import choice
# import time
# print("""ЗДРАВСТВУЙТЕ ДАВАЙТЕ ПОИГРАЕМ В Камень, Ножницы, Бумага
# ОТ ВАС ТРЕБУЕТСЯ ВЫЙГРАТЬ У КОМПЬЮТЕРА""")

# for s in range(3):
#     time.sleep(1)


# for s in range(1, 6):
#     print(f'И ТАК НАЧНЕМ ОТСЧЕТ до ПЯТИ:{s1}')
#     time.sleep(1)

# rock = '''
#     ______
# ---'   ____)
#       (______)
#       (_____)
#       (____)
# ---._(____)
# '''

# paper = '''
#     ________
# ---'   _____)_______
#           __________)
#           ___________)
#          __________)
# ---.____________)
# '''

# scissors = '''
#     ___    
# ---'   _)__________  
#         ___________)
#         ____________        
#          ___________)
#       (__)
# ---._(__)
# '''
# while True:
#     print('')
#     comp = choice(rock, scissors, paper]
#     user = input('выберите цыфру присвоенного варианта ответа камень(rock)=0, ножницы(scissors)=1, бумага(paper)3, выключить напишите стоп:')
#     if comp == 'камень' and user == 'камень':
#         print(f'НИЧЬЯ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'камень' and user == 'бумага':
#         print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'камень' and user == 'ножницы':
#         print(f'ВЫ ПРОИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'бумага' and user == 'бумага':
#         print(f'НИЧЬЯ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'бумага' and user == 'камень':
#         print(f'ВЫ ПРОИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'бумага' and user == 'ножницы':
#         print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'ножницы' and user == 'бумага':
#         print(f'ВЫ ПРОИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'ножницы' and user == 'камень':
#         print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ Компьютер выбрал {comp}, а вы {user}')
#     elif comp == 'ножницы' and user == 'ножницы':
#         print(f'НИЧЬЯ Компьютер выбрал {comp}, а вы {user}')
#     elif user == 'стоп':
#         print(f'ИГРА ОСТАНОВЛЕНА')
#         break
#     else:
#         print('Вы не правильно написали')
#         continue







# import random

# rock = '''
#     ______
# ---'   ____)
#       (______)
#       (_____)
#       (____)
# ---._(____)
# '''

# paper = '''
#     ________
# ---'   _____)_______
#           __________)
#           ___________)
#          __________)
# ---.____________)
# '''

# scissors = '''
#     ___    
# ---'   _)__________  
#         ___________)
#        (____________       
#          ___________)
#       (__)
# ---._(__)
# '''

# game_images = [rock, paper, scissors]
# while True:
#     user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice >= 3 or user_choice < 0: 
#         print("You typed an invalid number, you lose!") 
#         continue
#     elif user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")



# from random import choice
# from time import sleep

# print()
# print("""HELLO MY FRIEND, LET'S TO PLAY: 
# ROCK, SCISSORS, PAPER!
# YOU MUST TO WIN ME""")
# print('_____________________________________')

# for s in reversed(range(1, 4)):
#     print(f'Lets go  ...{s}')
#     sleep(1)

# while True:
    
#     comp = choice(['rock', 'scissors', 'paper'])
#     user = input('ROCK, SCISSORS, PAPER, if you want to stop just send me STOP: ').lower()

#     if comp == user:
#         print(f'DRAW. i choice {comp} and you {user}\n')

#     elif comp == 'rock' and user == 'paper':
#         print(f'CONGRATULATION YOU WIN!!! i choice {comp}, you {user}\n')

#     elif comp == 'rock' and user == 'scissors':
#         print(f'YOU LOSE... i choise {comp}, you {user}\n')

#     elif comp == 'paper' and user == 'rock':
#         print(f'YOU LOSE... i choise {comp}, you {user}\n')

#     elif comp == 'paper' and user == 'scissors':
#         print(f'CONGRATULATION YOU WIN!!! i choice {comp}, you {user}\n')

#     elif comp == 'scissors' and user == 'paper':
#         print(f'YOU LOSE... i choise {comp}, you {user}\n')

#     elif comp == 'scissors' and user == 'rock':
#         print(f'CONGRATULATION YOU WIN!!! i choice {comp}, you {user}\n')

#     elif user == 'stop':
#         print(f'GAME OVER')
#         break

#     else:
#         print('You typed an invalid name, you lose!\n')
#         continue





from random import choice
from time import sleep



def gameRSP():

    comp = choice(['камень', 'ножницы', 'бумага'])
    user = input('Камень, Ножницы, Бумага или стоп: ').lower()

    if comp == user:
        print(f'НИЧЬЯ. Компьютер выбрал {comp} и вы {user}\n')

    elif comp == 'камень' and user == 'бумага':
        print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ!!! Компьютер выбрал {comp}, а вы {user}\n')

    elif comp == 'камень' and user == 'ножницы':
        print(f'ВЫ ПРОИГРАЛИ... Компьютер выбрал {comp}, а вы {user}\n')

    elif comp == 'бумага' and user == 'камень':
        print(f'ВЫ ПРОИГРАЛИ... Компьютер выбрал {comp}, а вы {user}\n')

    elif comp == 'бумага' and user == 'ножницы':
        print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ!!! Компьютер выбрал {comp}, а вы {user}\n')

    elif comp == 'ножницы' and user == 'бумага':
        print(f'ВЫ ПРОИГРАЛИ... Компьютер выбрал {comp}, а вы {user}\n')

    elif comp == 'ножницы' and user == 'камень':
        print(f'ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ!!! Компьютер выбрал {comp}, а вы {user}\n')

    elif user == 'стоп':
        print(f'ИГРА ОСТАНОВЛЕНА')
    else:
        print('Команды не существует!\n')



print()
print("""ЗДРАВСТВУЙТЕ ДАВАЙТЕ ПОИГРАЕМ В ИГРУ: 
КАМЕНЬ, НОЖНИЦЫ, БУМАГА!
ОТ ВАС ТРЕБУЕТСЯ ВЫЙГРАТЬ КОМПЬЮТЕР""")
print('_____________________________________')

for s in reversed(range(1, 4)):
    print(f'ИГРА НАЧНЁТСЯ ЧЕРЕЗ ...{s}')
    sleep(1)





while True:
    try:
        gameRSP()
    except UnicodeDecodeError:
        print('не предвиденная ошибка')