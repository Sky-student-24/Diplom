import requests
from config import token
import allure


class Shop_API:

    def __init__(self, url):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self.url = url

    @allure.step("Поиск книги по наименованию")
    def search_book(self):
        my_headers = {}
        my_headers["Authorization"] = token
        url_2 = (
            "/v2/search/product?customerCityId=213&products%5Bpage%"
            "5D=1&products%5Bper-page%5D=60&phrase=%D0%BA%D0%BB%D1%8F%D1%8"
            "2%D0%B2%D0%B0%20%D0%BA%D1%80%D0%BE%D0%B2%D0%B8")
        resp = requests.get(self.url + url_2, headers=my_headers)
        return resp

    @allure.step("Переход в раздел 'Новинки'")
    def search_new_book(self):
        my_headers = {}
        my_headers["Authorization"] = token
        url_2 = (
            "/v2/products?include=productTexts%2Cpublisher%2CpublisherBrand%"
            "2CpublisherSeries%2Cdates%2CliteratureWorkCycle%2Crating%"
            "2Cbinding%2Ctags&forceFilters%5BonlyAvailableForSale%5D=1&"
            "forceFilters%5Btags%5D=13&forceFilters%5Btags%5D=4&forceFilters%"
            "5BonlyWithImage%5D=1&customerCityId=213&products%"
            "5Bpage%5D=1&products%5Bper-page%5D=60")
        resp = requests.get(self.url + url_2, headers=my_headers)
        return resp

    @allure.step("Открытие страницы выбранной книги")
    def open_page_book(self):
        my_headers = {}
        my_headers["Authorization"] = token
        resp = requests.get(self.url +
                            "/v1/products/slug/klatva-krovi-3131075",
                            headers=my_headers)
        return resp

    @allure.step("Добавление книги в корзину")
    def buy_book(self):
        my_headers = {}
        my_headers["Authorization"] = token
        body = {
            "id": 3131075
        }
        resp = requests.post(self.url + "/v1/cart/product",
                             headers=my_headers, json=body)
        return resp

    @allure.step("Добавление книги в корзину с некорректным методом вызова")
    def buy_book_incorrect(self):
        my_headers = {}
        my_headers["Authorization"] = token
        body = {
            "id": 3131075
        }
        resp = requests.delete(self.url + "/v1/cart/product",
                               headers=my_headers, json=body)
        return resp

    @allure.step("Добавление книги в корзину с неверным ID")
    def buy_wrong_book(self):
        my_headers = {}
        my_headers["Authorization"] = token
        body = {
            "id": 313107563
        }
        resp = requests.post(self.url + "/v1/cart/product",
                             headers=my_headers, json=body)
        return resp
