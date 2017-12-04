import math
import random

# вычисление гипотенузы
print("gypo = " +str(int(math.sqrt((179**2)+(971**2)))))

# вычисление количества десятков в числе
i = random.randint(10,99)
print("двузначное число = " +str(i))
i = list(str(i))
if int(i[0]) < 2:
    print("в числе "+i[0]+" десяток")
elif 2 < int(i[0])<5:
    print("в числе "+i[0]+" десятка")
else:
    print("в числе "+i[0]+" десятков")

# вычисление суммы трех чисел
i = random.randint(100,999)
print("трехзначное число = " +str(i))
i = list(str(i))
summa = str(int(i[0])+int(i[1])+int(i[2]))
print("Сумма цифр трехзначного числа = " + summa)

#дано случайное целое число - вывести следующее четное после него
i = random.randint(0,999)
print("случайное целое число = " + str(i))
if i%2==0:
    print(i+2)
else: print(i+1)

