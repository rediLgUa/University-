# Задание 3
# Пользователь вводит целое число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.


y = int(input("Введите год : "))
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("NO")
else:
    print("YES")