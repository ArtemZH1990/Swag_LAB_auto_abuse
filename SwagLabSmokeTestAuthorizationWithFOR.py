from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    """В данном классе локаторы на странице авторизации"""

    login_page_url = 'https://www.saucedemo.com/'

    user_name_pole_XPATH = "//input[@id='user-name']"
    password_pole_XPATH = "//input[@id='password']"
    login_click_button_XPATH = "//input[@id='login-button']"
    error_button_XPATH = "//h3[@data-test='error']"

    basic_password = "secret_sauce"
    users_name_data = ["standard_user",
                       "locked_out_user",
                       "problem_user",
                       "performance_glitch_user"]

    error_button_log_out_user_text = fr"Epic sadface: Sorry, this user has been locked out."


class InventoryPage:
    """В данном классе локаторы на странице товаров"""
    burger_menu_button_XPATH = "//button[@id='react-burger-menu-btn']"
    log_out_link_in_burger_menu = "//a[@id='logout_sidebar_link']"


class TestSmokeAuthorization(unittest.TestCase):
    """Тестовый класс, по прохождению авторизации, под разными логинами"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(LoginPage.login_page_url)
        # Переменная для проверки перехода на базовую страницу авторизации
        self.basic_page_assert = self.assertEqual("https://www.saucedemo.com/", self.driver.current_url)

    def test_authorization_with_for(self):
        for i in LoginPage.users_name_data:
            try:
                # Передаём в поля логина и пароля данные
                self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(i)
                self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
                self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
                # После прохождения авторизации возвращаемся на предыдущую страницу
                self.driver.find_element(By.XPATH, InventoryPage.burger_menu_button_XPATH).click()
                self.driver.find_element(By.XPATH, InventoryPage.log_out_link_in_burger_menu).click()
                self.assertEqual(LoginPage.login_page_url, self.driver.current_url)
            except:
                # Метод clear() не срабатывал, поэтому здесь цикл, на очистку полей после ввода логина и пароля,
                # при условии что есть некорректные данные ввода.(В нашем случае заблокировванный аккаунт)
                while True:
                    passsword_pole = self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH)
                    user_name_pole = self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH)
                    if passsword_pole.get_attribute('value') == user_name_pole.get_attribute('value') == '':
                        break
                    self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(Keys.BACKSPACE)
                    self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(Keys.BACKSPACE)

                print('This login is not valid, check your user-name!')
                continue

    def tearDown(self) -> None:
        self.driver.quit()
