import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scrappy.ADSI import ADSI
from scrappy.ATSIX import ATSIX
from scrappy.CEPU import CEPU
from scrappy.CFNAI import CFNAI
from scrappy.credit_easing import CreditEasing
from scrappy.EMV import EMV
from scrappy.FRBSF import FRBSF
from scrappy.GPR import GPR
from scrappy.InflationModels import InflationModels
from scrappy.NAAIM import NAAIM
from scrappy.PCI import PartisanConflictIndex
from scrappy.SRI import SRI
from scrappy.TMU import TMU
from scrappy.TPU import TPU




class IndikatorOverview(object):

    def __init__(self, indicator_list):
        self.indicators = indicator_list

    def run(self):

        for self.indicator in self.indicators:

            model = self.indicator()
            df = model.run()
            self.chart(df)

    def chart(self, df):
            df.plot()
            plt.title('{}'.format(self.indicator.__name__))
            plt.show()









if __name__ == '__main__':

    indicator_list = [ADSI, CEPU, CFNAI, EMV, FRBSF, GPR, NAAIM, PartisanConflictIndex, SRI, TMU, TPU]


    obj = IndikatorOverview(indicator_list)
    df = obj.run()
    print(df)