import time
from selenium import webdriver
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import SwagLabPageObjects


class TestAuthorization(unittest.TestCase):
    """Проверка авторизации. Позитивные и негативные сценарии."""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com')
        url_base = self.driver.current_url  # Локальная переменная, для проверки url домашний страницы.
        # Проверка нахождения на главной странице.
        self.assertEqual(SwagLabPageObjects.LoginPage.login_page_url, url_base)

    def test_positive_authorization(self):
        """Тест-кейс проходит авторизацию с валидными данными."""
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('standard_user')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('secret_sauce')
        login_button = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_click_button_XPATH)
        login_button.click()
        url_inventory = self.driver.current_url    # Локальная переменная, для проверки перехода на страницу товаров.
        # Проверка перехода на страницу товаров.
        self.assertEqual(SwagLabPageObjects.LoginPage.inventory_page_url, url_inventory)

    def test_negative_authorization_all(self):
        """Тест-кейс делает авторизацию с не валидными данными, и логином и паролем. Дополнительно ищет всплывающее окно об ошибке."""
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('123')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('123')
        login_button = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_click_button_XPATH)
        login_button.click()
        # Проверка негативного сценария. Переход на страницу товаров не произошел. Панель-оповещение об ошибке, появилась.
        error_button_actual_text = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.error_button_XPATH).text
        self.assertEqual(SwagLabPageObjects.LoginPage.error_button_expected_text, error_button_actual_text)
        self.assertEqual(SwagLabPageObjects.LoginPage.login_page_url, self.driver.current_url)

    def test_negative_authorization_login(self):
        """Тест-кейс проверяет авторизацию с не валидными данными поля логин."""
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('123')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('secret_sauce')
        login_button = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_click_button_XPATH)
        login_button.click()
        # Проверка негативного сценария. Переход на страницу товаров не произошел. Панель-оповещение об ошибке, появилась.
        error_button_actual_text = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.error_button_XPATH).text
        self.assertEqual(SwagLabPageObjects.LoginPage.error_button_expected_text, error_button_actual_text)
        self.assertEqual(SwagLabPageObjects.LoginPage.login_page_url, self.driver.current_url)

    def test_negative_authorization_password(self):
        """Тест-кейс проверяет авторизацию с не валидными данными поля пароль."""
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('standard_user')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('123')
        login_button = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_click_button_XPATH)
        login_button.click()
        # Проверка негативного сценария. Переход на страницу товаров не произошел. Панель-оповещение об ошибке, появилась.
        error_button_actual_text = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.error_button_XPATH).text
        self.assertEqual(SwagLabPageObjects.LoginPage.error_button_expected_text, error_button_actual_text)
        self.assertEqual(SwagLabPageObjects.LoginPage.login_page_url, self.driver.current_url)

    def test_positive_authorization_without_login_click_button(self):
        """Тест-кейс проверяет авторизацию без нажатия на клавишу LOGIN. Имитация нажатия клваиши ENTER."""
        login_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.login_pole_XPATH)
        login_pole.send_keys('standard_user')
        password_pole = self.driver.find_element(By.XPATH, SwagLabPageObjects.LoginPage.password_pole_XPATH)
        password_pole.send_keys('secret_sauce')
        password_pole.send_keys(Keys.RETURN)
        url_inventory = self.driver.current_url    # Локальная переменная, для проверки перехода на страницу товаров.
        # Проверка перехода на страницу товаров.
        self.assertEqual(SwagLabPageObjects.LoginPage.inventory_page_url, url_inventory)

    def tearDown(self) -> None:
        time.sleep(3)   # Для записи презентации(Не зыбыть выставить явное-неявное ожидание)
        self.driver.quit()


