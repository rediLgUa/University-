'''Задание 6
Это уже было, но теперь оформите это функцией:
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.'''

def is_year_leap (arg):
    if arg % 4 != 0 or (arg % 100 == 0 and arg % 400 != 0):
        return False
    else:
        return True

def triangle_possible(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False