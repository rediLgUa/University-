import requests

def test_book_create(app_url,bookParam):
    response = requests.post(app_url+"books/",data=bookParam)
    assert response.status_code==201
    bookJson=response.json()
    bookParam['id']=bookJson['id']
def test_book_read(app_url,book):
    response = requests.get(app_url+"books/"+str(book['id'])+'/')
    jsonrespID = response.json()
    print(response.text)
    assert book['id'] in jsonrespID['id']
    print(book)