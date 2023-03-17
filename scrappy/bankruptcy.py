import pandas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class Bankruptcy(object):

    def __init__(self):
        self.url = r'https://otce.finra.org/otce/dailyList?viewType=Bankruptcy'

    def run(self):
        df = self.load_data()
        self.advanced_settings()
        #Todo: Transformation Check
        return df

    def load_data(self):
        pass

    def advanced_settings(self):

        start = '01/3/2023'
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

        # iterate trough answer pages
        #todo: loop over pages

        # find info on page
        events = []

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
            events.append({'date': date, 'date_effective': date_eff, 'symbol': symbol, 'symbol_new': symbol_new,
                           'name': name, 'fincl_status': fincl_status, 'fincl_status_new': fincl_status_new,
                           'market': market})

        return pd.DataFrame(events)





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