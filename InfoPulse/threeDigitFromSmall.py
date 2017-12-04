a,b,c = int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье чило: "))
if a>=b and a>=c:
    if b>=c:
        print(str(c) + " " + str(b) + " " + str(a))
    else:
        print(str(b) + " " + str(c) + " " + str(a))
elif b>=a and b>=c:
    if a>=c:
        print(str(c) + " " + str(a) + " " + str(b))
    else:
        print(str(a) + " " + str(c) + " " + str(b))
elif c>=a and c>=b:
    if a>=b:
        print(str(b) + " " + str(a) + " " + str(c))
    else:
        print(str(a) + " " + str(b) + " " + str(c))





