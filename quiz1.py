# -*- coding: utf-8 -*-
import random
pop = 6
one = 1
summ = 0
n = True
print u"Привет.Ты попал в игру угадайка."
print u"Введите число от 1 до 6"
print u"Я также загадал число от 1 до 6."
print u"У тебя есть 5 попыток угадывать загаданные числа"
print u"Каждый раз когда ты угадываешь ты можешь получить баллы."
print u"Если компьютер загад число 5. А вы указали на 1 единицу меньше. Вы получите 5 баллов. Ну а если"
print u"На 2 единицы меньше,то минус еще 1 балл. То есть 4 балла."

while n != False and pop > 1:
    n = random.randint(1, 6)
    number = int(input(u"Введите число: "))
    if number < 1:
        break
    elif number > 6:
        break
    if number < n:
        x = n - number
        abs(x)
    elif n < number:
        x = number - n
        abs(x)
    elif number == n:
        summ = summ + 6
        print u"Ваше количество баллов: ",summ
        print u"------------"
        print u"-В точку!!!-"
        print u"------------"
        pop = pop - one
        continue
    if x == 1:
        summ = summ + 5
        print u"Ваше количество баллов: ",summ
        pop = pop - one
        continue
    elif x == 2:
        summ = summ + 4
        print u"Ваше количество баллов: ",summ
        pop = pop - one
        continue
    elif x == 3:
        summ = summ + 3
        print u"Ваше количество баллов: ",summ
        pop = pop - one
        continue
    elif x == 4:
        summ = summ + 2
        print u"Ваше количество баллов: ",summ
        pop = pop - one
        continue
    elif x == 5:
        summ = summ + 1
        print u"Ваше количество баллов: ",summ
        pop = pop - one
        continue
if summ > 25:
    print u"Победа"
elif summ < 25:
    print u"Проиграли!"



