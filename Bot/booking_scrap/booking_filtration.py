# This file include a class with instance methods that will be responsible to interact with our website after we have some results to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def select_price(self, minimum_price, maximum_price):
        min_price = self.driver.find_element(By.ID, 'price_filter_min')
        min_price.click()
        # sleep(3)
        length=len(min_price.get_attribute('value'))
        min_price.send_keys(length * Keys.BACK_SPACE)
        sleep(1)
        min_price.send_keys(minimum_price)
        max_price = self.driver.find_element(By.ID, 'price_filter_max')
        max_price.click()
        sleep(3)
        length_2 = len(max_price.get_attribute('value'))
        max_price.send_keys(length_2 * Keys.BACK_SPACE)
        sleep(1)
        max_price.send_keys(maximum_price)

    def select_beds(self, number_of_beds):
        if number_of_beds in range(1,7):
            beds = self.driver.find_elements(By.CSS_SELECTOR, f'span[aria-label="{number_of_beds}"]')
            beds[2].click()
        else:
            beds = self.driver.find_element(By.CSS_SELECTOR, f'span[aria-label="8+"]')
            beds.click()            

    def extra_amenities(self):
        air_conditioning = self.driver.find_element(By.NAME, 'Klimatyzacja')
        air_conditioning.click()

    def sumbit_filtrations(self):
        submit_filtrations = self.driver.find_element(By.CLASS_NAME, '_1ku51f04')
        submit_filtrations.click()

