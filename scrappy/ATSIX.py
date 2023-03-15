import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime


class ATSIX(object):
    """
    A continuous curve of inflation expectations three to 120 months ahead, analogous to a yield curve.
    """
    def __init__(self):
        self.url_target = r'https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/atsix/atsix_vintages.xlsx'

    def run(self):
        ''' Returns the Inflation and Real Rate term structure expectation. '''
        # Inflation Term Structure
        inflation = pd.read_excel(self.url_target, sheet_name='InfExp')
        inflation = self._format_file(inflation)

        # Real Rate Term Structure
        real_rate = pd.read_excel(self.url_target, sheet_name='Real')
        real_rate = self._format_file(real_rate)

        return inflation, real_rate

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        return df




if __name__ == '__main__':

    obj = ATSIX()
    df = obj.run()
    print(df)