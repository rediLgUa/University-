a,b,c = int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье чило: "))
if a>=b>=c:
    if b>=c:
        a,c=c,a
    else:
        a,b,c=b,c,a
elif b>=a and b>=c:
    if a>=c:
        a,b,c=c,a,b
    else:
        b,c=c,b
elif c>=a and c>=b:
    if a>=b:
        a,b=b,a
else: a,b,c=b,c,a
print(a,b,c) #fixed - without Type reworking.



