import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class FRBSF(object):

    def __init__(self):
        self.url_target = r'https://www.frbsf.org/wp-content/uploads/sites/4/FRBSF_Term_Web_Chart_Data.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        a = pd.read_excel(self.url_target, sheet_name='Two_year_decomposition')
        a = self._format_file(a)
        a = a[['ZCTERM02YR']]
        a.columns = ['TermPremium2y']


        b = pd.read_excel(self.url_target, sheet_name='Ten_year_decomposition')
        b = self._format_file(b)
        b = b[['ZCTERM10YR']]
        b.columns = ['TermPremium10y']

        df = pd.concat([a, b], axis=1)

        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df



if __name__ == '__main__':

    obj = FRBSF()
    df = obj.run()
    print(df)