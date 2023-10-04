# Задание №5
# Нужно написать сквозной тест с использованием Selenium, который авторизует пользователя на
# сайте https://www.saucedemo.com/.
# Данные для входа - логин: "standard_user", пароль: "secret_sauce".
# Проверить, что авторизация прошла успешно и отображаются товары.
# Вам необходимо использовать WebDriver для открытия страницы и методы sendKeys() для ввода
# данных в поля формы, и submit() для отправки формы. После этого, проверьте, что на странице
# отображаются продукты (productsLabel.getText() = "Products").

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath","//*[@id=\"user-name\"]")
    input_password = driver.find_element("xpath","//*[@id=\"password\"]")
    login_button = driver.find_element("xpath","//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element("xpath","//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text == "Products":
        print("Авторизация прошла успешно и отображается главная страница")
    else:
        print("Ошибка поиска элемента")

    time.sleep(5)


if __name__ == '__main__':
    first_test()