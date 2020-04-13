
# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





df = pd.read_csv('datasets/cleaned_data_final.csv')



df.to_csv('state.csv')


df2 = pd.read_csv('state.csv')




def inital_plot(df, variable):
	
	data_0 = df[df['STATE'] == variable]
	data_0.to_csv('state_Try.csv', mode = 'a', header = True)


def following_plots(df, variable):
	
	data_0 = df[df['STATE'] == variable]
	data_0.to_csv('state_Try.csv', mode = 'a', header = False)






def count(var1):

	df3 = pd.read_csv('state_Try.csv')
	list_Try = []
	for i in df3['STATE']:
		list_Try.append(i)



	return list_Try.count(var1)


list1 = ['MEGHALAYA','GUJARAT','MAHARASHTRA','MANIPUR','KERALA','HARYANA', 'HIMACHAL PRADESH',
		'RAJASTHAN','MEGHALAYA','MIZORAM','MANIPUR','PONDICHERRY']

inital_plot(df2, 'GOA')
for i in list1:
	n = count(i)
	if n>0:
		pass
	else:
		following_plots(df2, i)



df3 = pd.read_csv('state_Try.csv')




df3.groupby(
  ['STATE','new_WQI']
).size().unstack().plot(kind='bar',stacked=False,legend=True)

plt.show()

