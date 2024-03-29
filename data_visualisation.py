
# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('datasets/cleaned_data_final.csv')



df.to_csv('datasets/state.csv')


df2 = pd.read_csv('datasets/state.csv')


def state_graph(df, target):



	def inital_plot(df, variable):

		
		data_0 = df[df['STATE'] == variable]
		data_0.to_csv('datasets/state_filtered.csv', mode = 'a', header = True)
	def following_plots(df, variable):
		
		data_0 = df[df['STATE'] == variable]
		data_0.to_csv('datasets/state_filtered.csv', mode = 'a', header = False)






	def count(var1):

		df3 = pd.read_csv('datasets/state_filtered.csv')
		list_Try = []
		for i in df3['STATE']:
			list_Try.append(i)



		return list_Try.count(var1)


	list1 = ['MEGHALAYA','GUJARAT','MAHARASHTRA','MANIPUR','KERALA','HARYANA',
			'RAJASTHAN','MEGHALAYA','MIZORAM','MANIPUR','PONDICHERRY','ODISHA']

	inital_plot(df2, 'GOA')
	for i in list1:
		n = count(i)
		if n>0:
			pass
		else:
			following_plots(df2, i)



	df3 = pd.read_csv('datasets/state_filtered.csv')


	if target is 'new_WQI':

		df3['Water Quality']=df[target].apply(lambda x:("Excellent" if (x==1)  
												else("Good" if  (x==2)
												else("Poor" if  (x==3)
												else("Very Poor" if  (x==4) 
												else "Unsuitable")))))

	else:


		df3['Water Quality']=df[target].apply(lambda x:("Desirable" if (x==1)  
												else("Acceptable" if  (x==2)
												else"Harmful"
												)))




	df3 = df3[df3.STATE != 'STATE']


	df3.groupby(
	  ['STATE','Water Quality']
	).size().unstack().plot(kind='bar',stacked=False,legend=True)

	plt.xlabel('States')
	plt.ylabel('Count of WQI')






	plt.show()




state_graph(df2, 'new_WQI')


state_graph(df2, 'new_WQI_fishes')



