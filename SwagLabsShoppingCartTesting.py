from selenium import webdriver
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import SwagLabPageObjects
import time


class TestShoppingCart(unittest.TestCase):
    """Тест-класс проверяет добовление и удаление товаров в корзину"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com')
        url_base = self.driver.current_url  # Локальная переменная, для проверки url домашний страницы.
        # Проверка нахождения на главной странице.
        self.assertEqual(SwagLabPageObjects.LoginPage.login_page_url, url_base)
        # Проходим авторизацию
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('standard_user')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('secret_sauce')
        password_pole.send_keys(Keys.RETURN)

    def test_add_item_in_shopping_cart(self):
        """Тест-кейс проверяет добавление товаров в корзину для покупки"""
        # Будем циклом добавлять товары в корзину, проверять соответстивие по количеству
        # Цикл добавляет в корзину товары
        for i in range(len(SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH)):
            self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH[i]).click()

        # Тест проверяет, совпадает ли добавленное количество товара в корзину с отображение количества
        # над иконкой корзины. Добовляем всё что есть на странице, если бы что-то не добавилось тесты слетели.
        # Плюс сделать приведение типов , int -> str или наоборот.
        self.assertEqual(str(len(SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH)), \
                         self.driver.find_element(By.XPATH,
                                                  SwagLabPageObjects.ShoppingCart.cart_item_quantity_XPATH).text)

    def test_remove_from_shopping_cart(self):
        """Тест-кейс проверяет удаление товаров из корзины"""
        # Будем циклом добавлять товары в корзину, проверять соответстивие по количеству
        # Цикл добавляет в корзину товары
        for i in range(len(SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH)):
            self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH[i]).click()

        # Цикл удаляет товары из корзины
        for i in range(len(SwagLabPageObjects.InventoryPage.item_all_remove_from_cart_XPATH)):
            self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.item_all_remove_from_cart_XPATH[i]).click()
        # Проверяем что после удаления товаров из корзины, отсутствует цифровое отбражение
        self.assertEqual('', self.driver.find_element(By.XPATH, SwagLabPageObjects.ShoppingCart.cart_XPATH).text)

    def test_shopping_cart_link(self):
        """Тест-кейс добовляет товары и переходит на страницу оформления покупки в корзине"""
        # Цикл добавляет в корзину товары
        for i in range(len(SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH)):
            self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.item_all_add_to_cart_XPATH[i]).click()
        # Переходим на страницу оформления покупок в корзине
        self.driver.find_element(By.XPATH, SwagLabPageObjects.ShoppingCart.cart_XPATH).click()
        # Проверка перехода на страницу. Элемент YOUR CART может быть изменен,
        # как вариант тест может упасть в будущем
        self.assertEqual('YOUR CART', self.driver.find_element(By.XPATH, SwagLabPageObjects.ShoppingCart.your_cart_page_element).text)

    # Сделать добавление в корзину товара, проверить что именно тот что нужно товар добавился,
    # проверить цену товара, сделать скриншоты в тестах выше. Скрин отображения добавленных товаров
    # над значком корзины

    def tearDown(self) -> None:
        time.sleep(5)  # Для записи презентации(Не зыбыть выставить явное-неявное ожидание)
        self.driver.quit()
