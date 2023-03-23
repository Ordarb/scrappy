import pandas as pd
import matplotlib.pyplot as plt

from aionite_evohub.indicator_base import _BaseIndicator
from aionite_evohub.utils import resample_daily, rescale, calc_momentum, quantile_transformation
from aionite_evohub.settings import TIMEZONE

class CreditCycle(object):

    def __init__(self):
        self.url = r'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TOTBKCR&scale=left&&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Weekly%2C%20Ending%20Wednesday&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin'

    def run(self):
        df = self.load_data()
        return df

    def load_data(self):
        df = pd.read_excel(self.url, skiprows=10)
        df = self._format_file(df)
        #todo: transformation?
        z = df.pct_change(1)
        #z = calc_momentum(z.credit_cycle, windows=[12, 24]) # monthly change
        z = z.rolling(12).mean()
        z = calc_momentum(z.credit_cycle, windows=[4, 24, 52]) # monthly change
        #z = z.clip(upper=0.4, lower=-0.4)
        z = rescale(z, True, 1)

        z.plot()
        plt.show()

        z['2006':'2009'].plot()
        plt.show()

        z['2019':].plot()
        plt.show()

        return df

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df.columns = ['credit_cycle']
        return df



if __name__ == '__main__':

    obj = CreditCycle()
    df = obj.run()
    print(df)