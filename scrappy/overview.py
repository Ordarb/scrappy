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

    from scrappy.credit_card import CreditCardDefaults
    from scrappy.loan_defaults import LoanDefaults

    a = CreditCardDefaults().run()
    b = LoanDefaults().run()
    df = pd.concat([a, b], 1)
    df.columns = ['Credit Card Defaults', 'Loan Defaults']
    df.plot()
    plt.show()