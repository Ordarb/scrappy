import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt



class NAAIM(object):

    def __init__(self):
        self.url = r'https://www.naaim.org/programs/naaim-exposure-index/'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):
        driver = self.setup_webdriver()
        page = driver.page_source
        bs_object = BeautifulSoup(page, 'html.parser')
        candidates = bs_object.find_all('p')
        for li in candidates:
            test = li.text
            if li.text == 'Download EXCEL file with data since inception » HERE':
                url = li.find('a', href=True).attrs['href']

        df = pd.read_excel(url)
        df = self._format_file(df)
        df = df[['NAAIM Number']]
        df.columns = ['NAAIM_Exposure_Index']
        #todo: transformation?
        return df


    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df.sort_index(ascending=True, inplace=True)
        return df

    def setup_webdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver






if __name__ == '__main__':

    obj = NAAIM()
    df = obj.run()
    print(df)