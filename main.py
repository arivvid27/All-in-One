#imports
import os
import webbrowser
from time import sleep
from PyDictionary import PyDictionary
from random import randint
import pygame
import keyboard


#defines
def sleep_minutes(minutes):
    sleep(minutes * 60)


def sleep_hours(hours):
    sleep(hours * 3600)

def clear():
	try:
		os.system('cls')
	except:
		try:
			os.system('clear')
		except:
			os.system("printf '\033c'")

#setup
pygame.mixer.init(44100, -16, 2, 2048)
dictionary = PyDictionary()

#variables
math_score = int()

#MAIN CODE
print(
    'any thing in : [] is what you have to type to do that particular action.')
while True:
    user = input('''~~~~OPTIONS~~~~
1. Do some [math]
2. Use the [dictionary]
3. [browse] the web
4. Use the [calculator]
5. Set a [timer]
6. [quit] this program
>>> ''')

    if (user == 'math'):
        print('Ok! I will quiz you on math.')
        math_problems = int(input('How many problems do you want? > '))
        math_operator = input('What operation do you want for all of your problems? [add][subtract][multiply][divide] > ')
        for i in range(math_problems):
            print('We will start now.')
            if (math_operator == 'add'):
                math_num1_a = randint(0, 100)
                math_num2_a = randint(0, 100)
                global math_user_a
                math_user_a = float(input(f'{math_num1_a} + {math_num2_a} = '))
                if (math_user_a == (math_num1_a + math_num2_a)):
                    print('Nice!')
                    math_score += 1
                elif (math_user_a != (math_num1_a + math_num2_a)):
                    print('Aw...')
                    print(f'The correct answer was {math_num1_a + math_num2_a}')
                    if (math_score == 0):
                        pass
                    elif (math_score != 0):
                        math_score -= 1
            elif (math_operator == 'subtract'):
                math_num1_s = randint(0, 100)
                math_num2_s = randint(0, 100)
                global math_user_s
                math_user_s = float(input(f'{math_num1_s} - {math_num2_s} = '))
                if (math_user_s == (math_num1_s - math_num2_s)):
                    print('Nice!')
                    math_score += 1
                elif (math_user_s != (math_num1_s - math_num2_s)):
                    print('Aw...')
                    print(f'The correct answer was {math_num1_s - math_num2_s}')
                    if (math_score == 0):
                        pass
                    elif (math_score != 0):
                        math_score -= 1
            elif (math_operator == 'multiply'):
                math_num1_m = randint(0, 100)
                math_num2_m = randint(0, 100)
                global math_user_m
                math_user_m = float(input(f'{math_num1_m} x {math_num2_m} = '))
                if (math_user_m == (math_num1_m * math_num2_m)):
                    print('Nice!')
                    math_score += 1
                elif (math_user_m != (math_num1_m * math_num2_m)):
                    print('Aw...')
                    print(f'The correct answer was {math_num1_m * math_num2_m}')
                    if (math_score == 0):
                        pass
                    elif (math_score != 0):
                        math_score -= 1
            elif (math_operator == 'divide'):
                math_num1_d = randint(0, 100)
                math_num2_d = randint(0, 100)
                global math_user_d
                math_user_d = float(input(f'{math_num1_d} % {math_num2_d} = '))
                if (math_user_d == (math_num1_d / math_num2_d)):
                    print('Nice!')
                    math_score += 1
                elif (math_user_d != (math_num1_d / math_num2_d)):
                    print('Aw...')
                    print(f'The correct answer was {math_num1_a / math_num2_a}')
                    if (math_score == 0):
                        pass
                    elif (math_score != 0):
                        math_score -= 1
            else:
                print('I don\'t know that')
        print(f'You got {math_score} out of {math_problems} right.')
        user
    elif (user == 'dictionary'):
        user_dict = input('Ok! Enter what word you want to know about. >>> ')
        print(dictionary.meaning(user_dict))
    elif (user == 'browse'):
        user_browse = input('Ok! enter website name with domain. >>> ')
        webbrowser.open(user_browse, new=0, autoraise=True)
    elif (user == 'calculator'):
        global calc_operator
        calc_operator = input('''~~~~OPERATION~~~~
[add]
[subtract]
[multiply]
[divide]
[power] of
[modulo]
>>> ''')
        if (calc_operator == 'add'):
            add1 = int(input('Give me first number > '))
            add2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(add1 + add2)
        elif (calc_operator == 'subtract'):
            sub1 = int(input('Give me first number > '))
            sub2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(sub1 - sub2)
        elif (calc_operator == 'multiply'):
            mul1 = int(input('Give me first number > '))
            mul2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(mul1 * mul2)
        elif (calc_operator == 'divide'):
            div1 = int(input('Give me first number > '))
            div2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(div1 / div2)
        elif (calc_operator == 'power'):
            pow1 = int(input('Give me first number > '))
            pow2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(pow1**pow2)
        elif (calc_operator == 'modulo'):
            mod1 = int(input('Give me first number > '))
            mod2 = int(input('Give me second number > '))
            print('Ok! Here is your answer:')
            print(mod1 % mod2)
        else:
            print('I don\'t know that')
    elif (user == 'timer'):
        ho = int(input("Enter how long (in Hours) > "))
        mi = int(input("Enter how long (in Minutes) > "))
        se = int(input("Enter how long (in Seconds) > "))
        sleep_hours(ho)
        sleep_minutes(mi)
        sleep(se)
        pygame.mixer.music.load(
            'C:/Users/arivvid27/Downloads/BOMB_SIREN-BOMB_SIREN-247265934.wav')
        while True:
            pygame.mixer.music.play()
            print('Press "x" to silence the alarm')
            keyboard.wait('x')
            clear()
            pygame.mixer.music.pause()
            break
    elif (user == 'quit'):
        break
    else:
        print('I don\'t know that')
print('**YOU HAVE QUITTED THIS PROGRAM**')
sleep(3)
exit(120)
