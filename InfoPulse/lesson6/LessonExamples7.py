import unittest
import requests
import sys
import json


class BookCreateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Not use now. Just for you as example of setUpClass
        with open("book_data.json") as f:
            cls.data = json.load(f)

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book = {"title": "Anna Karenina", "author": "Lev Tolstoy"}

    # @unittest.expectedFailure
    def test_book_create(self):
        response = requests.post(self.base_url + "books/", data=self.book)
        self.assertEqual(response.status_code, 201)
        # for key in book:
        #     self.assertEqual(book[key], response.json()[key])
        self.book['id'] = response.json()['id']
        self.assertEqual(self.book, response.json())
        # TODO: Проверить, что эту книгу можно получить GET запросом

    # @unittest.skipIf(sys.platform.startswith("win"), "Not able in Windows")
    def test_book_create_without_title(self):
        self.book.pop("title")
        response = requests.post(self.base_url + "books/", data=self.book)
        # TODO: Проверить

    def tearDown(self):
        if "id" in self.book:
            requests.delete(self.base_url + 'books/' + str(self.book['id']))


class BookUpdateTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        response = requests.post(self.base_url + "books/", data={"title": "Anna Karenina", "author": "Lev Tolstoy"})
        self.book = response.json()

    def test_book_update_title(self):
        self.book["author"] = "Tolstoy Lev"
        response = requests.put(self.base_url+"books/{}/".format(self.book["id"]), data=self.book)
        self.assertEqual(response.status_code, 200)
        # TODO: Продолжить проверку

    def tearDown(self):
        requests.delete(self.base_url + 'books/' + str(self.book['id']))


# if __name__ == "__main__":
#     from HtmlTestRunner import HTMLTestRunner
#     unittest.main(testRunner=HTMLTestRunner(output=r"E:\Dropbox\Courses\Automatization\PyCharmProject\learn_unitest\result"))

# # test1 = OurTestCase("test_1")
# # test2 = OurTestCase("test_2")
# print(test1.run())
# print(test2.run())
# test_suite = unittest.TestSuite([test1, test2])
# result = unittest.TestResult()
# test_suite = unittest.TestLoader().loadTestsFromTestCase(BookCreateTests)
# # print(result)
# test_suite.run(result)
# print(result)


