import math
import random

# вычисление гипотенузы
print("gypo = ",math.sqrt((179**2)+(971**2))) #fixed - without Type reworking.

# вычисление количества десятков в числе
i = random.randint(10,99)
print("двузначное число = ", i) #fixed - without Type reworking.

i=i//10 #Fixed - only with numbers
if i <= 2:
    print("в числе ",i," десяток")
elif 2 <=i//10<=5:
    print("в числе ",i," десятка")
else:
    print("в числе ",i," десятков")

# вычисление суммы трех чисел
i = str(random.randint(100,999))
print("трехзначное число = ",i) #fixed - without Type reworking.
summa = int(i[0])+int(i[1])+int(i[2])
print("Сумма цифр трехзначного числа = ",summa)

#дано случайное целое число - вывести следующее четное после него
i = random.randint(-999,999)
print("случайное целое число = ",i)
print(int(i//2*2+2)) #fixed

#дано положительное действительное число X. Выведите дробную часть
a = random.uniform (1.0, 2.0)
print("Введите число....Хотя...Не надо напрягаться, я всё сам. Пусть это будет "+str(a))
b=a-int(a)
print("3 знака после точки этого числа = {0:.3f}".format(b))

#Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
a=float(input("введите положительное действительное число: "))
print(str(a-int(a))[2]) #fixed

