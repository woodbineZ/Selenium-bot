from booking_scrap.booking_filtration import BookingFiltration

import booking_scrap.constants as const
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep



class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";M:\Instalki\chromjum", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        sleep(5)

    def where_we_going(self, destination): 
        what_location_element = self.find_element(By.CSS_SELECTOR, 'button[data-index="0"]')
        what_location_element.click()
        location_element = self.find_element(By.CSS_SELECTOR, 'input[id="bigsearch-query-location-input"]')
        location_element.clear()
        #destination="Larnaca"
        location_element.send_keys(destination)
        sleep(1)
        location_final_click = self.find_element(By.CSS_SELECTOR, 'div[id="bigsearch-query-location-suggestion-0"]')
        location_final_click.click()
        sleep(1)
    
    def when_we_going(self, check_in_date, check_out_date):
        arrival_date = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{check_in_date}"]') 
        arrival_date.click()
        sleep(1)
        departure_date = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{check_out_date}"]')
        departure_date.click()
        sleep(1)

    def who_is_going(self, number_of_guests):
        guests_going = self.find_element(By.CSS_SELECTOR, 'div[data-testid="structured-search-input-field-guests-button"]')
        guests_going.click()
        adding_guests = self.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-adults-increase-button"]')
        for _ in range(number_of_guests):
            adding_guests.click()

    def submit_data(self):
        submit_all_changes = self.find_element(By.CSS_SELECTOR, 'button[class="b134py57 b14gupvm dir dir-ltr"]')
        submit_all_changes.click()
        sleep(2)

    def apply_filtrations(self):
        begin_filtration = self.find_element(By.CSS_SELECTOR, 'button[style="--filter-button_border:1px solid var(--filter-button_border-color, var(--j-qkgmf));"]')
        if (begin_filtration):
            begin_filtration.click()
        # sometimes button appears in different places with other tags of style/class. 
        # begin_filtration_2 = self.find_element(By.CSS_SELECTOR, 'button[style="--filter-button_border:1px solid var(--j-qkgmf);"]')
        # if (begin_filtration_2):
        #     begin_filtration_2.click()
        sleep(1.5)
        filtration = BookingFiltration(driver=self)
        sleep(1)
        filtration.select_price(minimum_price="100", maximum_price="700")
        sleep(3)
        filtration.select_beds(number_of_beds=3)
        filtration.extra_amenities()
        filtration.sumbit_filtrations()
    



