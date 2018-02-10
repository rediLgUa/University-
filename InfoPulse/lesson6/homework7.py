import unittest
import requests
from HtmlTestRunner import HTMLTestRunner

class BookCreateTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book = {"title": "JESUS","author": "ChRIST"}

    def test_book_create(self):
        req = requests.post(url= self.base_url + "books/", data=self.book)
        self.assertEqual(req.status_code, 201)
        for key in self.book:
            self.assertEqual(self.book[key], req.json()[key])
        self.book['id'] = req.json()['id']
        self.assertEqual(self.book, req.json())
        req = requests.get(url= self.base_url + "books/"+str(self.book['id'])+"/")
        self.assertEqual(req.status_code,200)

    def test_book_create_without_title(self):
        self.book.pop("title")
        req = requests.post(self.base_url + "books/", data=self.book)
        self.assertEqual(req.status_code,400)

    def test_book_create_without_author(self):
        self.book.pop("author")
        req = requests.post(self.base_url + "books/", data=self.book)
        self.assertEqual(req.status_code,400)

    def test_book_create_without_data(self):
        self.book.pop("author")
        req = requests.post(self.base_url + "books/", data="")
        self.assertEqual(req.status_code,400)
    #skip test example
    @unittest.skip("another parameters will be implemented")
    def test_new_param_of_book(self):
        req = requests.post(url=self.base_url+"books/",data=self.book + {"cost":"100"})
        self.assertEqual(req.status_code,400)

    def tearDown(self):
        if "id" in self.book:
            req=requests.delete(self.base_url + 'books/' + str(self.book['id']))
            self.assertEquals(req.status_code,204)

class BookUpdateTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        req = requests.post(self.base_url + "books/", data={"title": "JESUS","author": "ChRIST"})
        self.book = req.json()

    def test_book_update_title(self):
        self.book["title"] = "SATAN"
        req = requests.put(self.base_url+"books/{}/".format(self.book["id"]), data=self.book)
        self.assertEqual(req.status_code, 200)

    def test_book_update_author(self):
        self.book["author"] = "LORD"
        req = requests.put(self.base_url+"books/{}/".format(self.book["id"]), data=self.book)
        self.assertEqual(req.status_code, 200)

    def test_book_update_via_empty_space(self):
        self.book["author"] = " "
        self.book["title"] = " "
        req = requests.put(self.base_url+"books/{}/".format(self.book['id']), data=self.book)
        self.assertEqual(req.status_code,400)

    def tearDown(self):
        requests.delete(self.base_url + 'books/' + str(self.book['id']))

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output=r"d:\result"),verbosity=1)

#
