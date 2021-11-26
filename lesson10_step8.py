from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = driver.find_element_by_id('book')
    button.click()
    value = driver.find_element_by_id('input_value').text
    answer = calc(value)
    answer_field = driver.find_element_by_id('answer')
    answer_field.send_keys(answer)
    final_button = driver.find_element_by_id('solve')
    final_button.click()
except Exception as e:
    print(e)
finally:
    final_answer = driver.switch_to.alert.text
    print(final_answer)
    driver.quit()
