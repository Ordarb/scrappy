import pandas as pd
import matplotlib.pyplot as plt

from aionite_evohub.indicator_base import _BaseIndicator
from aionite_evohub.utils import resample_daily, rescale, calc_momentum, quantile_transformation
from aionite_evohub.settings import TIMEZONE


class LoanDefaults(object):
    """
    Delinquency Rate on Credit Card Loans of all US commercial Banks, from the Federal Reserve Bank of St.Louis. Data
    is presented quartely, Publication lag not specified.
    """
    def __init__(self):
        self.url = r'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DRALACBN&scale=left&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly%2C%20End%20of%20Period&fam=avg&fgst=lin&line_index=1&transformation=lin'

    def run(self):
        df = self.load_data()
        return df

    def load_data(self):
        df = pd.read_excel(self.url, skiprows=10)
        df = self._format_file(df)
        #todo: transformation?
        z = -calc_momentum(df.loan_default, windows=[1, 2, 4]) # monthly change
        z = rescale(z, True, 1)

        z['2000':].plot()
        plt.show()

        z['2017':].plot()
        plt.show()

        return z

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df.columns = ['loan_default']
        return df



if __name__ == '__main__':

    obj = LoanDefaults()
    df = obj.run()
    print(df)