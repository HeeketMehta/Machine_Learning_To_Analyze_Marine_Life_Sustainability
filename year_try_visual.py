import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('datasets/cleaned_data_final.csv')


list_loc = []
for i in df['LOCATIONS']:
	list_loc.append(i)

new_list_loc = []
for i in list_loc:
	if i is '0':
		pass
	else:
		n = list_loc.count(i)
	if n>=2:
		new_list_loc.append(i)



print(new_list_loc)