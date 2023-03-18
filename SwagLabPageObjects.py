class LoginPage:
    login_page_url = 'https://www.saucedemo.com/'
    inventory_page_url = 'https://www.saucedemo.com/inventory.html'
    error_button_XPATH = "//h3[@data-test='error']"
    login_pole_XPATH = "//input[@id='user-name']"
    password_pole_XPATH = "//input[@id='password']"
    login_click_button_XPATH = "//input[@id='login-button']"
    error_button_expected_text = fr"Epic sadface: Username and password do not match any user in this service"


class InventoryPage:
    # XPATH путь к описанию товаров и цены состоит из двух частей, между ними в цикле будем конкатенировать индекс!!!
    # Потому что индекс можно прилепить  только к первой части пути
    # На этой странице всего 6 товаров, счёт с первого в цикле
    first_part_inventory_item_XPATH = "//div[@class='inventory_list']/div[@class='inventory_item']"
    second_part_inventory_item_XPATH = "/div[@class='inventory_item_description']/div[@class='inventory_item_label']/a"
    firs_part_price_XPATH = "//div[@class='inventory_item']"
    second_part_price_XPATH = "//div[@class='inventory_item_price']"
    sort_box_XPATH = "//select[@class='product_sort_container']"
    # XPATH элементов в sort-box. Выбор опции сортировки
    a_z_sort_XPATH = "//option[@value='az']"
    z_a_sort_XPATH = "//select[@class='product_sort_container']/option[@value='za']"
    price_low_to_high_XPATH = "//select[@class='product_sort_container']/option[@value='lohi']"
    price_high_to_low_XPATH = "//select[@class='product_sort_container']/option[@value='hilo']"
    # Контейнеры с данными для проверки
    main_item_name_data = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    main_item_price_data = ['$7.99', '$9.99','$15.99', '$15.99', '$29.99', '$49.99']
    shoping_cart_icon_XPATH = "//span[@class='shopping_cart_badge']"    # Динамическая, аккуратно. Это отображение количества добавленных товаров(цифра на значке корзины)

    # ITEMS XPATH могут меняться при изменении верстки!!
    # Это XPATH кнопок добавления и удаления товаров в корзину
    item_sauce_labs_backpack_add_to_cart_XPATH = "//button[@id='add-to-cart-sauce-labs-backpack']"
    item_sauce_labs_backpack_remove_from_cart_XPATH = "//button[@id='remove-sauce-labs-backpack']"

    item_sauce_labs_bike_light_add_to_cart_XPATH = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    item_sauce_labs_bike_light_remove_from_cart_XPATH = "//button[@id='remove-sauce-labs-bike-light']"

    item_sauce_labs_bolt_T_Shirt_add_to_cart_XPATH = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    item_sauce_labs_bolt_T_Shirt_remove_from_cart_XPATH = "//button[@id='remove-sauce-labs-bolt-t-shirt']"

    item_sauce_labs_fleece_jacket_add_to_cart_XPATH = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    item_sauce_labs_fleece_jacket_remove_from_cart_XPATH = "//button[@id='remove-sauce-labs-fleece-jacket']"

    item_sauce_labs_onesie_add_to_cart_XPATH = "//button[@id='add-to-cart-sauce-labs-onesie']"
    item_sauce_labs_onesie_remove_from_cart_XPATH = "//button[@id='remove-sauce-labs-onesie']"

    item_test_all_the_things_T_Shirt_Red_add_to_cart_XPATH = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    item_test_all_the_things_T_Shirt_Red_remove_from_cart_XPATH = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"

    item_all_add_to_cart_XPATH = [item_sauce_labs_backpack_add_to_cart_XPATH,
                                  item_sauce_labs_bike_light_add_to_cart_XPATH,
                                  item_sauce_labs_bolt_T_Shirt_add_to_cart_XPATH,
                                  item_sauce_labs_fleece_jacket_add_to_cart_XPATH,
                                  item_sauce_labs_onesie_add_to_cart_XPATH,
                                  item_test_all_the_things_T_Shirt_Red_add_to_cart_XPATH,]

    item_all_remove_from_cart_XPATH = [item_sauce_labs_backpack_remove_from_cart_XPATH,
                                item_sauce_labs_bike_light_remove_from_cart_XPATH,
                                item_sauce_labs_bolt_T_Shirt_remove_from_cart_XPATH,
                                item_sauce_labs_fleece_jacket_remove_from_cart_XPATH,
                                item_sauce_labs_onesie_remove_from_cart_XPATH,
                                item_test_all_the_things_T_Shirt_Red_remove_from_cart_XPATH]

    # Названия товаров
    sauce_labs_backpack_title_XPATH = "//a[@id='item_4_title_link']"
    sauce_labs_bike_light_title_XPATH = "//a[@id='item_0_title_link']"
    sauce_labs_bolt_T_Shirt_title_XPATH = "//a[@id='item_1_title_link']"
    sauce_labs_fleece_jacket_title_XPATH = "//a[@id='item_5_title_link']"
    sauce_labs_onesie_title_XPATH = "//a[@id='item_2_title_link']"
    the_things_T_Shirt_Red_title_XPATH = "//a[@id='item_3_title_link']"
    # Контейнер нужен будет для проверки, при добавлении в корзину и отображение товара в ней. Число в XPATH товара равно индексу в контейнере
    item_title_index_data = ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie",
                             "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Backpack", "Sauce Labs Fleece Jacket"]


class ShoppingCart:
    # XPATH отображения количества товаров в корзине, на странице товаров. Динамический, меняется при удалении и добавлении
    cart_item_quantity_XPATH = "//span[@class='shopping_cart_badge']"  # Здесь цифры добавления товаров в корзину
    cart_XPATH = "//a[@class='shopping_cart_link']"  # Здесь сама корзина
    your_cart_page_element = "//span[@class='title']"  # Элемент в хедере, для проверки перехода на страницу
    cart_page_url = "https://www.saucedemo.com/cart.html"