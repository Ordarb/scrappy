import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class CFNAI(object):

    def __init__(self):
        self.url_target = r'https://www.chicagofed.org/-/media/publications/cfnai/cfnai-data-series-xlsx.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        df['CFNAI'] = df['CFNAI'].clip(lower=-2, upper=2)
        df['DIFFUSION'] = df['DIFFUSION'].clip(lower=-1, upper=1)
        df['DIFFUSION'] = (df['DIFFUSION'] + 1) / 2
        return df

    def load_data(self):

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

    df['DIFFUSION'].loc['1970':].plot()
    plt.show()

    df['CFNAI'].loc['1970':].plot()
    plt.show()

    print(df)