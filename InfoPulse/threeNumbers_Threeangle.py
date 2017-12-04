a,b,c = int(input("Введите сторону А ")),int(input("Введите сторону B ")),int(input("Введите сторону C "))
if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")