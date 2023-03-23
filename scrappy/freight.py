import pandas as pd
import matplotlib.pyplot as plt

from aionite_evohub.indicator_base import _BaseIndicator
from aionite_evohub.utils import resample_daily, rescale, calc_momentum, quantile_transformation
from aionite_evohub.settings import TIMEZONE


class FreightTraffic(object):
    """
    Equal Weighted Indicator of US Freight indicators:
    """
    def __init__(self):

        self.urls = [('Truck Tonnage', r'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TRUCKD11&scale=left&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&line_index=1&transformation=lin'),
                      ('Rail Freight Carloads', r'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=RAILFRTCARLOADSD11&scale=left&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&line_index=1&transformation=lin'),
                      ('Cass Freight Shipments', r'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=FRGSHPUSM649NCIS&scale=left&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&line_index=1&transformation=lin')
                     ]

    def run(self):

        df = pd.DataFrame()
        for element in self.urls:
            name = element[0]
            url = element[1]
            z = self.load_data(url)
            df = pd.concat([z, df], 1)
        df.columns = [element[0] for element in self.urls]

        df['2005':].plot()
        plt.show()

        df.mean(1).plot()
        plt.show()

        return df

    def load_data(self,url):

        df = pd.read_excel(url, skiprows=10)
        df = self._format_file(df)
        #todo: transformation?

        df.rolling(1).mean()
        df.plot()
        plt.show()

        z = calc_momentum(df, windows=[3]) # monthly change
        z = rescale(z, True, 1)

        z['2017':].plot()
        plt.show()

        return z

    @staticmethod
    def _format_file(df):
        df.set_index(df.columns[0], inplace=True)
        df = df.iloc[:, 0]
        return df



if __name__ == '__main__':

    obj = FreightTraffic()
    df = obj.run()
    print(df)