'''Задание 9
Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
 1-е число – сколько строк будет в песне. По умолчанию 3 
2-е число – сколько «la» будет в строке («la»
в строке объединяются дефисом). По умолчанию 3 
3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!». По умолчанию 0'''
try:
    def song(row=3,la=3,end=0):
        iterator=1
        la = la - 1
        while  iterator<=row:
            if end==0:
                print("la"+"-la"*la, end=".\n")
                iterator+=1
            else:
                print("la" + "-la" * la, end="!\n")
                iterator+=1
except Exception as e:
    print(e)
if __name__=="__main__":
    song()