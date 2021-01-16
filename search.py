import pandas as pd
import numpy as np

AmdData = pd.read_csv('data/AMD.csv')
print(AmdData)
New_table = AmdData.assign(Return = AmdData.get('Adj Close') - AmdData.get('Open'))
print(New_table)
R_bar = New_table.get('Return').sum() / New_table.shape[0]
print('R Bar value is',round(R_bar,5))

top = 0
for i in range(New_table.shape[0]):
    a =(New_table.get('Return').iloc[i] - R_bar)**2
    top = a + top
std= np.sqrt(top/ ((New_table.shape[0]) - 1))
print('standard deviation is', round(std, 5))


