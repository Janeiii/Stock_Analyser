import pandas as pd
import numpy as np
import pandas_datareader as pdr
from datetime import datetime

def search_symbol():
    amd_data = pdr.get_data_stooq(symbols='NIO', start=datetime(2000, 1, 1), end=datetime.now())
    print(amd_data)
    #new_table = amd_data.assign(Return=amd_data.get('Adj Close') - amd_data.get('Open'))
    #print(new_table)
    #r_bar = new_table.get('Return').sum() / new_table.shape[0]
    #print('R Bar value is', round(r_bar, 5))
    #top = 0
    #for i in range(new_table.shape[0]):
        #a = (new_table.get('Return').iloc[i] - r_bar) ** 2
        #top = a + top
    #std = np.sqrt(top / ((new_table.shape[0]) - 1))
    #print('standard deviation is', round(std, 5))
