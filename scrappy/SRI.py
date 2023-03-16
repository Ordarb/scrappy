import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class SRI(object):

    def __init__(self):
        self.url_target = r'https://www.clevelandfed.org/-/media/files/webcharts/systemicrisk/landing_systemicrisk.csv'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        df = pd.read_csv(self.url_target)
        df = self._format_file(df)
        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df



if __name__ == '__main__':

    obj = SRI()
    df = obj.run()
    print(df)