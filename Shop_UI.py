from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Shop_UI:

    def __init__(self, driver):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru")
        self._driver.maximize_window()

    @allure.step("Поиск книги по наименованию")
    def search(self, term):
        """
            Ввод наименования книги в поле поиска и нажатие кнопки поиска
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "app-search"))
            ).send_keys(term)
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button.search-form__button-search"))
            ).click()

    @allure.step("Получение рузультата")
    def results(self):
        """
            Получение количества найденных книг
        """
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "div.catalog-products-total"))
            )
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "div.catalog-products-total").text

    @allure.step("Переход на страницу выбранной книги")
    def get_book(self):
        """
            Нажатие иконки выбранной книги
        """
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(.,"
                                             " 'Преступление и наказание')]"))
            ).click()

    @allure.step("Добавление книги в корзину")
    def add_to_cart(self):
        """
            Нажатие кнопки 'Купить" на странице выбранной книги,
            что означает добавить в корзину
        """
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button.product-buttons__main-action"))
            ).click()

    @allure.step("Удаление книги из корзины")
    def delete_to_cart(self):
        """
            Нажатие иконки со значком 'мусорного бака' на странице корзины,
            для удаления книги из корзины
        """
        self._driver.get("https://www.chitai-gorod.ru/cart")
        WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "button.cart-item__delete-button"))
                ).click()
