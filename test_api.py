from Shop_API import Shop_API
import allure

api = Shop_API("https://web-agr.chitai-gorod.ru/web/api")


@allure.title("API")
@allure.severity("normal")
@allure.description("Поиск книги")
def test_search_book():
    response = api.search_book()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200


@allure.title("API")
@allure.severity("normal")
@allure.description("Открытие раздела 'Новинки'")
def test_search_new_book():
    response = api.search_new_book()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200


@allure.title("API")
@allure.severity("normal")
@allure.description("Открытие страницы выбранной книги")
def test_open_page_book():
    response = api.open_page_book()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200


@allure.title("API")
@allure.severity("normal")
@allure.description("Добавление книги в корзину")
def test_buy_book():
    response = api.buy_book()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200


@allure.title("API")
@allure.severity("normal")
@allure.description("Добавление книги в корзину"
                    "с неправльно выбранным методом вызова")
def test_buy_book_incorrect():
    response = api.buy_book_incorrect()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 405


@allure.title("API")
@allure.severity("normal")
@allure.description("Добавление книги в корзину"
                    "с неправльно указанным ID")
def test_buy_wrong_book():
    response = api.buy_wrong_book()
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 400
