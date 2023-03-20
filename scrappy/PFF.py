import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class PFF(object):

    def __init__(self):
        self.url_target = r'https://www.frbsf.org/wp-content/uploads/sites/4/proxy-funds-rate-data.xlsx?20230302'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        df = pd.read_excel(self.url_target, skiprows=9)
        df = self._format_file(df)
        df = df.loc[:, 'Effective funds rate'] - df.loc[:, 'Proxy funds rate']
        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df



if __name__ == '__main__':

    obj = PFF()
    df = obj.run()
    print(df)