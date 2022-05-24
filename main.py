import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[style="display:inline;float:right"]'), '100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    input1 = int(browser.find_element(By.ID, 'input_value').text)

    input2 = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
    input2.send_keys(str(calc(input1)))

    input3 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    input3.click()

finally:
    time.sleep(5)
    browser.close()
