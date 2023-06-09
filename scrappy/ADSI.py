import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class ADSI(object):

    def __init__(self):
        self.url_root = r'https://www.philadelphiafed.org'
        self.url = self.url_root + '/surveys-and-data/real-time-data-research/ads'
        self.url_target = r'https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/ads/ads_index_most_current_vintage.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        df = df.clip(lower=-1, upper=1)
        df = (df + 1) / 2
        df = df.rolling(20).mean()

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
                if li.text == 'Most Current ADS Index Vintage':
                    url = self.url_root+li.attrs['href']

        df = pd.read_excel(url)
        df = self._format_file(df)
        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df.index = [datetime.strptime(idx, '%Y:%m:%d') for idx in df.index]
        return df

    def setup_webdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        return driver






if __name__ == '__main__':

    obj = ADSI()
    df = obj.run()

    df.loc['1980':].plot()
    plt.show()

    df.loc['2000':].plot()
    plt.show()

    df.loc['2010':].plot()
    plt.show()

    print(df)