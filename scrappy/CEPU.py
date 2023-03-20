import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class CEPU(object):

    def __init__(self):
        self.url_target = r'https://www.policyuncertainty.com/media/China_Mainland_Paper_EPU.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        df = pd.read_excel(self.url_target, sheet_name='EPU 2000 onwards')
        df = self._format_file(df)

        return df

    @staticmethod
    def _format_file(df):
        idx = df[['year', 'month']].applymap(str)
        idx = idx.year + ':' + idx.month
        df.index = idx
        df.index = [datetime.strptime(i, '%Y:%m') for i in df.index]
        df = df[['EPU']]
        df.columns = ['CEPU']
        return df



if __name__ == '__main__':

    obj = CEPU()
    df = obj.run()
    df.loc['2000':].plot()
    plt.show()

    print(df)