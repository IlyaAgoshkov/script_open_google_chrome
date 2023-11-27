import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Google Chrome с помощью Selenium WebDriver
driver = webdriver.Chrome()

# Предполагаем, что пользователь уже авторизован в Discord
logged_in = True

# Если пользователь не авторизован в Discord, то он должен ввести данные учетной записи вручную
if not logged_in:
    email = input("Введите адрес электронной почты: ")
    password = input("Введите пароль: ")

# Запрашиваем у пользователя ввод ссылок на приглашения в Discord
invite_links = []
while True:
    invite_link = input("Введите ссылку на приглашение в Discord (или нажмите Enter, чтобы закончить ввод): ")
    if not invite_link:
        break
    invite_links.append(invite_link)

# Проходим по каждой ссылке в списке
for invite_link in invite_links:
    # Открываем ссылку на приглашение к каналу Discord
    driver.get(invite_link)

    # Ожидаем, пока страница загрузится
    time.sleep(5)

    # Проверяем, авторизован ли пользователь в Discord
    if logged_in:
        # Если пользователь уже авторизован, то перемещаемся на страницу с приглашением и принимаем его
        wait = WebDriverWait(driver, 15)
        wait.until(EC.title_contains('Discord'))
        accept_button = driver.find_element_by_xpath('//button[text()="Присоединиться"]')
        accept_button.click()
    else:
        # Если пользователь не авторизован, вводим данные учетной записи и принимаем приглашение
        login_button = driver.find_element_by_xpath('//button[text()="Войти"]')
        login_button.click()
        email_input = driver.find_element_by_name('email')
        email_input.send_keys(email)
        password_input = driver.find_element_by_name('password')
        password_input.send_keys(password + Keys.RETURN)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.title_contains('Discord'))
        accept_button = driver.find_element_by_xpath('//button[text()="Присоединиться"]')
        accept_button.click()
        logged_in = True

# Закрываем браузер
driver.quit()