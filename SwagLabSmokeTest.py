from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


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

    def test_standart_user_authorization(self):
        # Проверка ввода первого логина из базы данных(standart_user). Переход на страницу товаров. Проверка по URl
        self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(LoginPage.users_name_data[0])
        self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
        self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
        self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)
        # Переход со страницы товаров, на страницу авторизации. Проверка по URL
        self.driver.find_element(By.XPATH, InventoryPage.burger_menu_button_XPATH).click()
        self.driver.find_element(By.XPATH, InventoryPage.log_out_link_in_burger_menu).click()
        self.basic_page_assert

    def test_locked_out_user_aithorization(self):
        # Проверка ввода первого логина из базы данных(locked_out_user). Данный логин заблакирован, переходи на страницу товаров невозможен
        # При попытке авторизации должно появиться всплывающее окно
        self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(LoginPage.users_name_data[1])
        self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
        self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
        # Переменная для отображения актуального текста сообщения, о не пройденной авторизации
        # Проверка по тексту и наличию элемента. Проверка по URL
        error_button_actual_text = self.driver.find_element(By.XPATH, LoginPage.error_button_XPATH).text
        self.assertEqual(LoginPage.error_button_log_out_user_text, error_button_actual_text)
        self.basic_page_assert

    def test_problem_user_authorization(self):
        # Проверка ввода первого логина из базы данных(problem_user). Переход на страницу товаров. Проверка по URl
        self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(LoginPage.users_name_data[2])
        self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
        self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
        self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)
        # Переход со страницы товаров, на страницу авторизации. Проверка по URL
        self.driver.find_element(By.XPATH, InventoryPage.burger_menu_button_XPATH).click()
        self.driver.find_element(By.XPATH, InventoryPage.log_out_link_in_burger_menu).click()
        self.basic_page_assert

    def test_performance_glitch_user_authorization_V1(self):
        # Проверка ввода первого логина из базы данных(performance_glitch_user). Переход на страницу товаров. Проверка по URl
        self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(LoginPage.users_name_data[3])
        self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
        # В данном методе кликаем по кнопке login до тех пор, пока не перейдём на страницу товаров
        while True:
            self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
            if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
                break
        # Переход со страницы товаров, на страницу авторизации. Проверка по URL
        self.driver.find_element(By.XPATH, InventoryPage.burger_menu_button_XPATH).click()
        self.driver.find_element(By.XPATH, InventoryPage.log_out_link_in_burger_menu).click()
        self.basic_page_assert

    def test_performance_glitch_user_authorization_V2(self):
        # Проверка ввода первого логина из базы данных(performance_glitch_user). Переход на страницу товаров. Проверка по URl
        self.driver.find_element(By.XPATH, LoginPage.user_name_pole_XPATH).send_keys(LoginPage.users_name_data[3])
        self.driver.find_element(By.XPATH, LoginPage.password_pole_XPATH).send_keys(LoginPage.basic_password)
        self.driver.find_element(By.XPATH, LoginPage.login_click_button_XPATH).click()
        # Здесь можно было указать явное ожидание, отображения веб элемента на странице товаров, но я прописал неявное в setUp
        # Переход со страницы товаров, на страницу авторизации. Проверка по URL
        self.driver.find_element(By.XPATH, InventoryPage.burger_menu_button_XPATH).click()
        self.driver.find_element(By.XPATH, InventoryPage.log_out_link_in_burger_menu).click()
        self.basic_page_assert

    def tearDown(self) -> None:
        self.driver.quit()
