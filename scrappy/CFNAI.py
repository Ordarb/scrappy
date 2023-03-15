import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime


class CFNAI(object):

    def __init__(self):
        self.url_target = r'https://www.chicagofed.org/-/media/publications/cfnai/cfnai-data-series-xlsx.xlsx'

    def run(self):

        df = pd.read_excel(self.url_target, sheet_name='data')
        df = self._format_file(df)

        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df



if __name__ == '__main__':

    obj = CFNAI()
    df = obj.run()
    print(df)