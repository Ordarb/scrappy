import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class GPR(object):

    def __init__(self):
        self.url_target = r'https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        df = pd.read_excel(self.url_target)
        df = self._format_file(df)

        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df = df[['GPR', 'GPRT', 'GPRA']]
        df.columns = ['GPR', 'Threats', 'Acts']
        df = df.dropna()
        return df



if __name__ == '__main__':

    obj = GPR()
    df = obj.run()
    print(df)