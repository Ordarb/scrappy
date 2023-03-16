import pandas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt


class InflationModels(object):
    """
    Derived from the Clevelend Fed
    """
    def __init__(self):
        self.url_target = r'https://www.clevelandfed.org/-/media/files/webcharts/inflationexpectations/inflation-expectations.xlsx'

    def run(self):
        df = self.load_data()
        #Todo: Transformation Check
        return df

    def load_data(self):

        infl_expecations = pd.read_excel(self.url_target, sheet_name='Expected Inflation')
        infl_expecations = self._format_file(infl_expecations)

        risk_premia = pd.read_excel(self.url_target, sheet_name='Ten-year Expected Chart')
        risk_premia = self._format_file(risk_premia)

        return infl_expecations, risk_premia

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df['2023':].index = pd.to_datetime(df['2023'].index, yearfirst=False, dayfirst=True)
        return df



if __name__ == '__main__':

    obj = InflationModels()
    df = obj.run()
    print(df)