import time

from selenium import webdriver
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


print("Приветствем тебя в нашем интернет-магазине")


class Locators:
    # Названия товаров
    items_name_XPATH = {
                        1: "//a[@id='item_4_title_link']",
                        2: "//a[@id='item_0_title_link']",
                        3: "//a[@id='item_1_title_link']",
                        4: "//a[@id='item_5_title_link']",
                        5: "//a[@id='item_2_title_link']",
                        6: "//a[@id='item_3_title_link']"
                        }

    # Введенная пользователем переменная будет применена, как ключ в данном словаре
    items_add_to_cart_XPATH = {
                               1: "//button[@id='add-to-cart-sauce-labs-backpack']",
                               2: "//button[@id='add-to-cart-sauce-labs-bike-light']",
                               3: "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
                               4: "//button[@id='add-to-cart-sauce-labs-fleece-jacket']",
                               5: "//button[@id='add-to-cart-sauce-labs-onesie']",
                               6: "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
                               }

    # Словарь для последующих проверок цены
    items_price_on_inventory_page_XPATH = {
                                           1: "//div[@class='inventory_item'][1]//div[@class='inventory_item_price']",
                                           2: "//div[@class='inventory_item'][2]//div[@class='inventory_item_price']",
                                           3: "//div[@class='inventory_item'][3]//div[@class='inventory_item_price']",
                                           4: "//div[@class='inventory_item'][4]//div[@class='inventory_item_price']",
                                           5: "//div[@class='inventory_item'][5]//div[@class='inventory_item_price']",
                                           6: "//div[@class='inventory_item'][6]//div[@class='inventory_item_price']"
                                           }

    # Поля логина и пароля, для авторизации
    login_pole_XPATH = "//input[@id='user-name']"
    password_pole_XPATH = "//input[@id='password']"

    # Названия доступных товаров
    main_item_name_data = ["Sauce Labs Backpack",
                           "Sauce Labs Bike Light",
                           "Sauce Labs Bolt T-Shirt",
                           "Sauce Labs Fleece Jacket",
                           "Sauce Labs Onesie",
                           "Test.allTheThings() T-Shirt (Red)"]

    cart_XPATH = "//a[@class='shopping_cart_link']"
    cart_page_url = "https://www.saucedemo.com/cart.html"
    checkout_button_XPATH = "//button[@id='checkout']"
    checkout_first_name_XPATH = "//input[@id='first-name']"
    checkout_last_name_XPATH = "//input[@id='last-name']"
    checkout_postal_code_XPATH = "//input[@id='postal-code']"
    checkout_continue_button_XPATH = "//input[@id='continue']"
    checkout_overview_url = "https://www.saucedemo.com/checkout-step-two.html"
    total_items_price_without_XPATH = "//div[@class='summary_subtotal_label']"
    checkout_finish_button_XPATH = "//button[@id='finish']"
    checkout_complete_url = "https://www.saucedemo.com/checkout-complete.html"

    def validate(self):
        # Проверка ввода пользовательских данных
        while True:
            print("Выберите один из следующих товаров: \n1 - Sauce Labs Backpack\
                                                       \n2 - Sauce Labs Bike Light\
                                                       \n3 - Sauce Labs Bolt T-Shirt\
                                                       \n4 - Sauce Labs Fleece Jacket\
                                                       \n5 - Sauce Labs Onesie\
                                                       \n6 - Test.allTheThings() T-Shirt (Red)")
            try:
                # Применение данной переменной как ключа, будет в словаре items_add_to_cart_XPATH в классе Locators
                i = int(input("Введите номер выбранного товара: "))
                print()
                if 1 <= i <= 6:
                    item_title = Locators.main_item_name_data[i - 1]
                    print(f"Вы выбрали: {item_title}")

                    break
                else:
                    raise Exception
            except:
                print("Вы ввели некорректные данные. Выберте заново один из доступных товаров.")
                print()
        return i




class TestSmokeWithInput(unittest.TestCase, Locators):
    """Тест-кейс включает смоук-тестирование всего бизнес-пути, на основе ввода пользовательских данных"""

    def setUp(self) -> None:
        self.i = self.validate()    # Номер выбранного пользователем товара
        self.item_title = Locators.main_item_name_data[self.i - 1]    # Название выбранного товара
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.saucedemo.com')
        # Проходим авторизацию
        login_pole = self.driver.find_element(By.XPATH, Locators.login_pole_XPATH)
        login_pole.send_keys('standard_user')
        password_pole = self.driver.find_element(By.XPATH, Locators.password_pole_XPATH)
        password_pole.send_keys('secret_sauce')
        password_pole.send_keys(Keys.RETURN)

    def test_smoke_with_input(self):
        # Добавляем выбранный товар в корзину
        user_choice = Locators.items_add_to_cart_XPATH[self.i]    # Переменная i использовалась в теле цикла while во время выбора товара
        self.driver.find_element(By.XPATH, user_choice).click()
        item_price_on_inventory_page_XPATH = self.driver.find_element(By.XPATH, Locators.items_price_on_inventory_page_XPATH[self.i]).text  # Та-самая введенная пользователем переменная
        # Переходим в корзину
        self.driver.find_element(By.XPATH, Locators.cart_XPATH).click()
        # Проверка перехода по url
        self.assertEqual(Locators.cart_page_url, self.driver.current_url)
        user_choice_title = Locators.main_item_name_data[self.i-1]   # Переменная для проверки названия товара
        # Проверка по цене и названию товара
        item_price_on_cart_page_XPATH = "//div[@class='cart_item']//div[@class='inventory_item_price']"    #Переменная, для проверки цены(Возможно её нужно было определить в классе Locators)
        self.assertEqual(item_price_on_inventory_page_XPATH, self.driver.find_element(By.XPATH, item_price_on_cart_page_XPATH).text)
        self.assertEqual(self.item_title, self.driver.find_element(By.XPATH, Locators.items_name_XPATH[self.i]).text)
        # Переход к оформлению товара(Ввод пользовательских данных: Имя, Фамиля, Почтовый индекс)
        self.driver.find_element(By.XPATH, Locators.checkout_button_XPATH).click()
        self.driver.find_element(By.XPATH, Locators.checkout_first_name_XPATH).send_keys('Art')
        self.driver.find_element(By.XPATH, Locators.checkout_last_name_XPATH).send_keys('Zh')
        self.driver.find_element(By.XPATH, Locators.checkout_postal_code_XPATH).send_keys('220')
        self.driver.find_element(By.XPATH, Locators.checkout_continue_button_XPATH).click()
        # Оформление товара
        # Проверка перехода по url, названию товара и цене.
        self.assertEqual(Locators.checkout_overview_url, self.driver.current_url)
        self.assertEqual(self.item_title, self.driver.find_element(By.XPATH, Locators.items_name_XPATH[self.i]).text)
        self.assertEqual(item_price_on_inventory_page_XPATH, self.driver.find_element(By.XPATH, item_price_on_cart_page_XPATH).text)
        # Проверка итоговой цены, без учёта налога и цены товара.
        item_total_price = self.driver.find_element(By.XPATH, Locators.total_items_price_without_XPATH).text.split()    # Переменная для данных цены на финальной странице оформления товара
        self.assertEqual(item_price_on_inventory_page_XPATH, item_total_price[2])
        self.driver.find_element(By.XPATH, Locators.checkout_finish_button_XPATH).click()
        # Проверка перехода на страницу завершения покупки
        self.assertEqual(Locators.checkout_complete_url, self.driver.current_url)

    def tearDown(self) -> None:
        self.driver.quit()
