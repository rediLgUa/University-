a,b,c = int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье чило: "))
count=0
if a==b and a==c:
    print("3")
elif b==c and b!=a:
    print("2")
elif b==a and b!=c:
    print("2")
elif c==a and c!=b:
    print("2")
else:
    print("0")