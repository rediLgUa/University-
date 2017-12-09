# Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)
task1string = input("Введите слово(string, строку) = ")
if task1string.isdecimal():
    print("Вы ввели числовое значение")
else:
    print("Вы ввели строчное значение")

# Посчитайте сколько у вас пробелов в строке.
print("кол-во пробелов = ",task1string.count(" ")) #fixed - without Type reworking.

# Посчитайте сколько у вас символов точки '.' в строке.
print("кол-во символов '.' = ",task1string.count(".")) #fixed - without Type reworking.

# Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена пробелами. Выведите ее на экран.
task4 = "Homework"
print(task4.center(100)) #Fix with spaces. Without hardcode.

# Сделайте первые буквы слов строки большими (upper case).
print(task4.upper())

