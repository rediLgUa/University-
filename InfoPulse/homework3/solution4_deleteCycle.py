'''
Задание 4

У вас есть список чисел.
Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?
Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, пока он не останется пустым.
'''
numList = [int(x) for x in input("Enter first List for TASK 1 with Spaces : ").split()]
stringInput = input("Enter string for TASK 2: ")
numList2 = [int(x) for x in input("Enter first List for TASK 3 with Spaces: ").split()]
try:
    def listItemDeleting (mass):
        for i in range(len(mass)):
            print(mass)
            del mass[0]
        return
except:
    print("Something wrong. Check code.")

def wordLettersDeleting(sent):
    for i in range(len(sent)):
        print(sent)
        sent=sent[:-1]
#Функция не изменяет исходную переменну, создается илюзия удаления для задания.
try:
    def delMaxtillMin(mass):
        n = 1
        while n < len(mass):
            for i in range(len(mass) - n):
                if mass[i] > mass[i + 1]:
                    mass[i], mass[i + 1] = mass[i + 1], mass[i]
            n += 1
        lenMass=len(mass)
        while i<lenMass:
            print(mass[0],end=" deleted\n")
            mass.pop(0)
            i+=1
except:
    print("Something wrong. Check code.")

listItemDeleting(numList)
wordLettersDeleting(stringInput)
delMaxtillMin(numList2)
