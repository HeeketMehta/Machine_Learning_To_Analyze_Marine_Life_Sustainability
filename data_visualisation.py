
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





import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

def line_plot():



	df = pd.read_csv('datasets/state.csv')


	df.groupby(df['year'])
	# df.to_csv('datasets/groupby_year.csv')

	list_Excellent = []
	list_good = []
	list_poor = []
	list_verypoor = []
	list_unsuitable = []


	count_of_excellent = 0
	count_of_good = 0
	count_of_poor = 0
	count_of_verypoor = 0
	count_of_unsuitable = 0
	

	df['Excellent'] = list_Excellent
	df['Good'] = list_good
	df['Poor'] = list_poor
	df['Very Poor'] = list_verypoor
	df['Unsuitable'] = list_unsuitable
	df.index = [2014,2013,2012,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003]


	ax = df.plot.line()
	ax.set_title('Before interpolation')
	ax.set_xlabel("year")
	ax.set_ylabel("Count of Quality")

	f1 = interp1d(df.index, df['Excellent'],kind='cubic')
	f2 = interp1d(df.index, df['Good'],kind='cubic')
	f3 = interp1d(df.index, df['Poor'],kind='cubic')
	f4 = interp1d(df.index, df['Very Poor'],kind='cubic')
	f5 = interp1d(df.index, df['Unsuitable'],kind='cubic')

	df2 = pd.DataFrame()
	new_index = np.arange(2014,2003)
	df2['Excellent'] = f1(new_index)
	df2['Good'] = f2(new_index)
	df2['Poor'] = f3(new_index)
	df2['Very Poor'] = f4(new_index)
	df2['Unsuitable'] = f5(new_index)
	df2.index = new_index

	ax2 = df2.plot.line()
	ax2.set_title('After interpolation')
	ax2.set_xlabel("year")
	ax2.set_ylabel("weight")


	plt.show()

line_plot()