import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class CreditEasing(object):

    def __init__(self):
        self.url_target = r'https://www.clevelandfed.org/-/media/files/webcharts/crediteasing/crediteasingbalancesheet.xls'

    def run(self):

        df = pd.read_excel(self.url_target, skiprows=1)
        df = self._format_file(df)
        df = df[['Lending to Financial Institutions', 'Liquidity to Key Credit Markets', 'Traditional Security Holdings',
                 'Federal Agency Debt and Mortgage-Backed Securities Purchases', 'Long-Term Treasury Purchases']]
        df['CreditEasing'] = df.sum(1)
        return df.CreditEasing

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df



if __name__ == '__main__':

    obj = CreditEasing()
    df = obj.run()
    print(df)