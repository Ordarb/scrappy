import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime


class PartisanConflictIndex(object):

    def __init__(self):
        self.url_root = r'https://www.philadelphiafed.org'
        self.url = self.url_root + '/surveys-and-data/real-time-data-research/partisan-conflict-index'
        self.url_target = None

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        if self.url_target is not None:
            url = self.url_target
        else:
            driver = self.setup_webdriver()
            page = driver.page_source
            bs_object = BeautifulSoup(page, 'html.parser')
            candidates = bs_object.find_all('a', href=True)
            for li in candidates:
                if li.text == 'Excel spreadsheet':
                    url = self.url_root+li.attrs['href']

        df = pd.read_excel(url)
        df = self._format_file(df)
        return df

    @staticmethod
    def _format_file(df):
        df['year_month'] = pd.to_datetime(df['Year'].astype(str)  + df['Month'], format='%Y%B')
        df.set_index(df.columns[3], inplace=True)
        df = df.drop(columns=['Year', 'Month'])
        return df

    def setup_webdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver




if __name__ == '__main__':

    obj = PartisanConflictIndex()
    df = obj.run()
    print(df)