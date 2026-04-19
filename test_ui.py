from selenium import webdriver
from Shop_UI import Shop_UI
import allure


@allure.title("UI")
@allure.feature("Mozilla Firefox")
@allure.severity("normal")
@allure.description("Проверка работы сайта в браузере Mozilla Firefox")
def test_browser_Firefox():
    driver = webdriver.Firefox()
    with allure.step("Открытие сайта через браузер Mozilla Firefox"):
        Shop_UI(driver)

    driver.quit()


@allure.title("UI")
@allure.feature("Google Chrome")
@allure.severity("normal")
@allure.description("Проверка работы сайта в браузере Google Chrome")
def test_browser_Chrome():
    driver = webdriver.Chrome()
    with allure.step("Открытие сайта через браузер Google Chrome"):
        Shop_UI(driver)

    driver.quit()


@allure.title("UI")
@allure.feature("Microsoft Edge")
@allure.severity("normal")
@allure.description("Проверка работы сайта в браузере Microsoft Edge")
def test_browser_Edge():
    driver = webdriver.Edge()
    with allure.step("Открытие сайта через браузер Microsoft Edge"):
        Shop_UI(driver)

    driver.quit()


@allure.title("UI")
@allure.feature("Google Chrome")
@allure.severity("normal")
@allure.description("Поиск книги по названию")
def test_search():
    driver = webdriver.Chrome()
    with allure.step("Открытие сайта через браузер Google Chrome"):
        shop = Shop_UI(driver)
    with allure.step("Поиск книги с выбранным названием"):
        shop.search("Преступление и наказание")
    with allure.step("Получение рузльтата, сколько книг найдено"):
        result = shop.results()
    final_result = int(result.split()[0])
    with allure.step("Проверка, что результат поиска книги больше 0"):
        assert final_result > 0

    driver.quit()


@allure.title("UI")
@allure.feature("Mozilla Firefox")
@allure.severity("normal")
@allure.description("Добавление книги в корзину для покупок")
def test_add_to_cart():
    driver = webdriver.Edge()
    with allure.step("Открытие сайта через браузер Mozilla Firefox"):
        shop = Shop_UI(driver)
    with allure.step("Поиск книги с выбранным названием"):
        shop.search("Преступление и наказание")
    with allure.step("Переход на страницу выбранной книги из поиска"):
        shop.get_book()
    with allure.step("Добавление книги в корзину покупок"):
        shop.add_to_cart()

    driver.quit()


@allure.title("UI")
@allure.feature("Mozilla Firefox")
@allure.severity("normal")
@allure.description("Удаление книги из корзину для покупок")
def test_delete_to_cart():
    driver = webdriver.Edge()
    with allure.step("Открытие сайта через браузер Mozilla Firefox"):
        shop = Shop_UI(driver)
    with allure.step("Поиск книги с выбранным названием"):
        shop.search("Преступление и наказание")
    with allure.step("Переход на страницу выбранной книги из поиска"):
        shop.get_book()
    with allure.step("Добавление книги в корзину покупок"):
        shop.add_to_cart()
    with allure.step("Удаление книги из корзины покупок"):
        shop.delete_to_cart()

    driver.quit()
