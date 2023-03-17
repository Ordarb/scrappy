import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class IDEMV(object):

    def __init__(self):
        self.url_target = r'https://www.policyuncertainty.com/media/All_Infectious_EMV_Data.csv'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        df = pd.read_csv(self.url_target, encoding='ISO-8859-1')
        df = self._format_file(df)

        return df

    @staticmethod
    def _format_file(df):
        idx = df[['day', 'month', 'year']].applymap(str)
        idx = idx.day + '.' + idx.month + '.' + idx.year
        df.index = idx
        df.index = [datetime.strptime(i, '%d.%m.%Y') for i in df.index]
        df = df[['All_Infectious_EMV_Data']]
        df.columns = ['ID-EMV']
        return df



if __name__ == '__main__':

    obj = IDEMV()
    df = obj.run()
    print(df)