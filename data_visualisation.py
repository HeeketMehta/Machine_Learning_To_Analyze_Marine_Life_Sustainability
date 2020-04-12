
# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





df = pd.read_csv('datasets/cleaned_data_final.csv')



df.to_csv('state.csv')


df2 = pd.read_csv('state.csv')

for i in df['STATE']:
	if i == 'GOA' or 'GUJARAT':
		pass
	else:
		df2.drop([i], axis = 1, inplace = True)

df2.to_csv('state1.csv')