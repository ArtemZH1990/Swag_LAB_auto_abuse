import time
from selenium import webdriver
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import SwagLabPageObjects
import datetime


class TestSortBox(unittest.TestCase):
    """Тестируем сорт-бокс страницы товаров. Наличие, фильтрацию"""
    inventory_item_name_data = []  # Контейнер для сбора данных имен товаров

    def setUp(self):
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
        # Обращение к сорт-боксу
        self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.sort_box_XPATH).click()

    def test_sort_box_sorting_from_a_to_z(self):
        """Тест-кейс проходит авторизацию, ищет окно сорт-бокса, выбирает сортировку по алфавиту"""
        # Обращаемся к сорт-боксу, выбираем сортировку по алфавиту
        self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.a_z_sort_XPATH).click()
        # Цикл для сбора названий товаров
        for i in range(1, 7):
            inventory_item = self.driver.find_element(By.XPATH, (SwagLabPageObjects.InventoryPage.first_part_inventory_item_XPATH + f'[{i}]' + SwagLabPageObjects.InventoryPage.second_part_inventory_item_XPATH)).text
            self.inventory_item_name_data.append(inventory_item)
        # Проверка на соответствие названий товаров, отсортированных по алфавиту
        self.assertEqual(SwagLabPageObjects.InventoryPage.main_item_name_data, self.inventory_item_name_data)
        self.inventory_item_name_data.clear()
        # Скрин-шот для отчёта
        actual_date = datetime.date.today().strftime('%m.%d.%Y')
        self.driver.save_screenshot(r"C:\Users\ART\PycharmProjects\pythonProject1\Trainee\2023\Feb\ScreenShot\Sort_a_to_z " + actual_date + ".png")

    def test_sort_box_sorting_from_z_to_a(self):
        """Тест-кейс проходит авторизацию, ищет окно сорт-бокса, выбирает сортировку по алфавиту, реверсивно. От z до a"""
        # Обращаемся к сорт-боксу, выбираем сортировку по алфавиту, реверсивно от z-a
        self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.z_a_sort_XPATH).click()
        # Цикл для сбора названий товаров
        for i in range(1, 7):
            inventory_item = self.driver.find_element(By.XPATH, (SwagLabPageObjects.InventoryPage.first_part_inventory_item_XPATH + f'[{i}]' +
                                                                 SwagLabPageObjects.InventoryPage.second_part_inventory_item_XPATH)).text
            self.inventory_item_name_data.append(inventory_item)
        # Проверка на соответствие названий товаров, отсортированных по алфавиту
        self.assertEqual(SwagLabPageObjects.InventoryPage.main_item_name_data[::-1], self.inventory_item_name_data)
        self.inventory_item_name_data.clear()
        # Скрин-шот для отчёта
        actual_date = datetime.date.today().strftime('%m.%d.%Y')
        self.driver.save_screenshot(r"C:\Users\ART\PycharmProjects\pythonProject1\Trainee\2023\Feb\ScreenShot\Sort_z_to_a " + actual_date + ".png")

    def test_sort_box_sorting_by_price_low_to_high(self):
        """Тест-кейс проходит авторизацию, ищет окно сорт-бокса, выбирает сортировку по цене, по возрастанию"""
        # Обращаемся к сорт-боксу, выбираем сортировку по цене, от возрастанию
        self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.price_low_to_high_XPATH).click()
        # Цикл для сбора цен товаров
        for i in range(1, 7):
            inventory_item = self.driver.find_element(By.XPATH, (SwagLabPageObjects.InventoryPage.firs_part_price_XPATH + f'[{i}]' + SwagLabPageObjects.InventoryPage.second_part_price_XPATH)).text
            self.inventory_item_name_data.append(inventory_item)
        # Проверка на соответствие цен товаров, отсортированных по возрастанию
        self.assertEqual(SwagLabPageObjects.InventoryPage.main_item_price_data, self.inventory_item_name_data)
        self.inventory_item_name_data.clear()
        # Скрин-шот для отчёта
        actual_date = datetime.date.today().strftime('%m.%d.%Y')
        self.driver.save_screenshot(r"C:\Users\ART\PycharmProjects\pythonProject1\Trainee\2023\Feb\ScreenShot\Sort_by_price_low_to_high " + actual_date + ".png")

    def test_sort_box_sorting_by_price_high_to_low(self):
        """Тест-кейс проходит авторизацию, ищет окно сорт-бокса, выбирает сортировку по цене, по убыванию"""
        # Обращаемся к сорт-боксу, выбираем сортировку по цене, по убыванию
        self.driver.find_element(By.XPATH, SwagLabPageObjects.InventoryPage.price_high_to_low_XPATH).click()
        # Цикл для сбора цен товаров
        for i in range(1, 7):
            inventory_item = self.driver.find_element(By.XPATH, (
                        SwagLabPageObjects.InventoryPage.firs_part_price_XPATH + f'[{i}]' + SwagLabPageObjects.InventoryPage.second_part_price_XPATH)).text
            self.inventory_item_name_data.append(inventory_item)
        # Проверка на соответствие цен товаров, отсортированных по убыванию
        self.assertEqual(SwagLabPageObjects.InventoryPage.main_item_price_data[::-1], self.inventory_item_name_data)
        self.inventory_item_name_data.clear()
        # Скрин-шот для отчёта
        actual_date = datetime.date.today().strftime('%m.%d.%Y')
        self.driver.save_screenshot(r"C:\Users\ART\PycharmProjects\pythonProject1\Trainee\2023\Feb\ScreenShot\Sort_by_price_high_to_low " + actual_date + ".png")

    # Сделать проверки добавление и удаление элементов в корзину, там динамический скриптуля счёт с 1!!!!
    # Сделать скриншоты стринц!!!

    def tearDown(self) -> None:
        time.sleep(5)   # Для записи презентации(Не зыбыть выставить явное-неявное ожидание)
        self.driver.quit()

