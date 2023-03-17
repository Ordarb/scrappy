import pandas
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt
import time


class Bankruptcy(object):

    def __init__(self):
        self.url = r'https://otce.finra.org/otce/dailyList?viewType=Bankruptcy'
        self.events = []

    def run(self):
        df = self.load_data()
        self.advanced_settings()
        #Todo: Transformation Check
        return df

    def load_data(self):
        pass

    def advanced_settings(self):

        start = '01/3/2019'
        end = '01/20/2023'

        driver = self.setup_webdriver()

        # start date
        loc = driver.find_element(By.XPATH, '//*[@id="start_date"]')
        loc.clear()
        loc.send_keys(start)
        # end date
        driver.find_element(By.XPATH, '//*[@id="end_date"]').click()
        loc = driver.find_element(By.XPATH, '//*[@id="end_date"]')
        loc.clear()
        loc.send_keys(end)
        # wait a moment
        driver.implicitly_wait(time_to_wait=5)
        #todo: make it implicitly wait until everything is loaded. Can take very long (minutes)
        time.sleep(60)
        # iterate trough answer pages

        # step 1 find number of pages
        driver.find_element(By.XPATH, r'/html/body/app-root/div/div[2]/div/app-page-container/div/div/app-daily-list-data/div/app-datagrid/div[2]/clr-datagrid/div[1]/div/clr-dg-footer/div/app-pagination-controls/div/div')
        page = driver.page_source
        bs_objects = BeautifulSoup(page, 'html.parser')
        elements = bs_objects.find_all('input')
        pages_max = int(max(elements[-1]['max']))

        pages = np.arange(1, pages_max + 1, 1)
        for page in pages:
            driver.find_element(By.XPATH, '//*[@id="page-number-input"]').click()
            loc = driver.find_element(By.XPATH, '//*[@id="page-number-input"]')
            loc.clear()
            loc.send_keys(page)
            driver.find_element(By.XPATH, '//*[@id="text_filter"]').click()
            time.sleep(10)
            self.scrap_info(driver=driver)


    def scrap_info(self, driver):
        # find info on page
        page = driver.page_source
        bs_objects = BeautifulSoup(page, 'html.parser')
        elements = bs_objects.find_all('clr-dg-row')

        for e in elements:
            infos = e.find_all('clr-dg-cell')
            date = infos[0].text
            date_eff = infos[1].text
            symbol = infos[2].text
            symbol_new = infos[3].text
            name = infos[4].text
            fincl_status = infos[5].text
            fincl_status_new = infos[6].text
            market = infos[7].text
            self.events.append({'date': date, 'date_effective': date_eff, 'symbol': symbol, 'symbol_new': symbol_new,
                           'name': name, 'fincl_status': fincl_status, 'fincl_status_new': fincl_status_new,
                           'market': market})
        return driver





    @staticmethod
    def _format_file(df):
        return df

    def setup_webdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver


if __name__ == '__main__':

    obj = Bankruptcy()
    df = obj.run()
    print(df)