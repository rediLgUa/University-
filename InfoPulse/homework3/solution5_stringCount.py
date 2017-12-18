'''Задание 5
Создайте строку, в которой написан, какой-то текст. Пример:
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
Усложнённое ** (можно сначала его не делать):
Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)
'''

currentVal = ("Not to know is bad, not to wish to know is worth. Не знать плохо, не хотеть знать еще хуже.")
wordsCount=0
newListwithWords=[]
for i in currentVal.split(" "):
    wordsCount += 1
    newListwithWords.append(i)
print(wordsCount) # вывод количества слов в тексте.

for i in range (len(newListwithWords)):
    newListwithWords[i]=newListwithWords[i].strip(",") # Удаление знаков препинания
    newListwithWords[i]=newListwithWords[i].strip(".") # Удаление знаков препинания
newListwithWords.sort(key=str.lower) # Сортировка по возрастанию в ловер кейсе
print("Sorted list is =",newListwithWords)

#подсчёт количества повторений слова в листе.
count = {}
for i in newListwithWords:
    count.update({i:newListwithWords.count(i)})
print(count)