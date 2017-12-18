'''Задание 7
Функция принимает три числа a, b, c.
Функция должна определить, существует ли треугольник с такими сторонами и если существует,
то возвращает тип треугольника
Equilateral triangle (равносторонний),
Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).'''

Eq="Equilateral triangle"
Is="Isosceles triangle"
Ve="Versatile triangle"
No="Not a triangle"

def triangle_type(a,b,c):
    if a+b<=c or a+c<=b or b+c<=a:
        return No
    elif a!=b and a!=c and b!=c:
        return Ve
    elif a==b==c:
        return Eq
    else:
        return Is