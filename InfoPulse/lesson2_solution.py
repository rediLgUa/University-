# -*- coding: utf-8 -*-
task1string = input("Введите слово(string, строку) = ")
if task1string.isdecimal():
    print("Вы ввели числовое значение")
else:
    print("Вы ввели строчное значение")

print("кол-во пробелов = ",task1string.count(" ")) #fixed - without Type reworking.
print("кол-во символов '.' = ",task1string.count(".")) #fixed - without Type reworking.

task4 = "Homework"
print('{:>46} {:>46}'.format(task4,""))
a=('{:>50} {:>49}'.format(task4,""))
print(a.count(" "))
print(task4.upper())

