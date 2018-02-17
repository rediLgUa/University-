import pytest
import requests

@pytest.fixture(scope="session")
def app_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture(scope='session')
def bookParam(app_url):
    return {'title': 'Hitler', 'author': 'Sebastian'}

@pytest.fixture(scope="session")
def book(app_url):
    response = requests.post(app_url + "books/", data={"title": "Anna Karenina", "author": "Lev Tolstoy"})
    book = response.json()
    yield book
    r = requests.delete(app_url + "books/{}/".format(book["id"]))
    print(r.status_code)

@pytest.fixture(scope="session")
def role_data(book):
    return {"name": "Anna Karenina", "level": 10, "type": "master", "book": book["id"]}
