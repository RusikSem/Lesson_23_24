from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

driver_service = Service(executable_path='./chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=driver_service)

import time

driver.maximize_window()

url_list = [0, 'https://www.selenium.dev/downloads', 'https://ooek.od.ua/user/?next=/profile/', 'https://id.cisco.com/', 'https://www.linkedin.com/', 'https://email.seznam.cz/']
for i in range(1, len(url_list)):
    url = url_list[i]
    driver.get(url)
    name = f'site{i}.png'
    try:
        f = open(name, 'rb')
        b = f.read()
        f.close()
    except:
        pass
    else:
        name1 = f'site{i}t{time.time()}.png'
        f1 = open(name1, 'wb')
        f1.write(b)
        f1.close()

    driver.get_screenshot_as_file(name)
    time.sleep(3)
