# file = open('test2.txt')
# file2 = open('file2.txt', 'w')
# num = 0
# for line in file:
#     file2.write(str(num) + " " + line)
#     num += 1
# file.close()
# file2.close()
import requests
# url = "http://httpbin.org/get"
# headers = {'user-agent':'roman browser'}
# params = {'blah1':'yeah', 'blah2':'not yeah'}
# resp = requests.get(url, headers = headers)
# print(resp.text)
# resp = requests.get(url, headers = headers, params=params)
# print(resp.text)
# print(resp.json())

book_data = {'title': 'Roman', 'author':'Me'}

# book = requests.post("https://pulse-rest-testing.herokuapp.com/books/", data=book_data)
# books = book.json()
# print(books)
r = requests.post("https://pulse-rest-testing.herokuapp.com/books/", data=book_data)
book = r.json()
print(book)

bookDelete = requests.delete("https://pulse-rest-testing.herokuapp.com/books/"+str(book['id']))

bookDelete = requests.delete("https://pulse-rest-testing.herokuapp.com/books/"+"20")
bookDelete = requests.delete("https://pulse-rest-testing.herokuapp.com/books/"+"22")
bookDelete = requests.delete("https://pulse-rest-testing.herokuapp.com/books/"+"23")
print(bookDelete.status_code)
