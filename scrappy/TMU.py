import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
import os
import glob

class TMU(object):

    def __init__(self):
        self.url = r'https://www.dropbox.com/s/o4ddj33odyyz4v6/Twitter_Economic_Uncertainty.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):
        driver = self.setup_webdriver()
        btn = driver.find_element(by=By.XPATH, value='//*[@id="fvsdk-container"]/div[1]/header/div[1]/div[1]/button')
        btn.click()

        path = os.path.join(os.path.expanduser('~'), 'downloads')
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        path_to_excel = max(paths, key=os.path.getctime)
        df = pd.read_excel(path_to_excel)
        df = self._format_file()

        #todo: transformation?
        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df = df[['TMU-WGT']]
        df.columns = ['Twitter Market Uncertainty']
        return df

    def setup_webdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver



if __name__ == '__main__':

    obj = TMU()
    df = obj.run()
    print(df)