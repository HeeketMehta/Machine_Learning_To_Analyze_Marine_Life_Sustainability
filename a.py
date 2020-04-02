import pandas as pd
import numpy as np

################################################################# PROCESSING THE FILE AND CONVERTING DTYPES ###################################################
df = pd.read_csv(r"waterData1.csv",encoding="ISO-8859-1")

df['Temp'] = pd.to_numeric(df['Temp'], errors = 'coerce')
df['B.O.D. (mg/l)'] = pd.to_numeric(df['B.O.D. (mg/l)'], errors = 'coerce')
df['NITRATENaN N+ NITRITENaNN (mg/l)'] = pd.to_numeric(df['NITRATENaN N+ NITRITENaNN (mg/l)'], errors = 'coerce')
df['TOTAL COLIFORM (MPN/100ml)Mean'] = pd.to_numeric(df['TOTAL COLIFORM (MPN/100ml)Mean'], errors = 'coerce')
df['FECAL COLIFORM (MPN/100ml)'] = pd.to_numeric(df['FECAL COLIFORM (MPN/100ml)'], errors = 'coerce')


# print(df.dtypes)


df.fillna(0, inplace = True)



# print(df.dtypes)
df.drop(df.index[262], inplace=True)
df.drop(df.index[433], inplace=True)
df.drop(df.index[1914], inplace=True)







#################################################################################################################








########################################################################### FOR CLEANING TEMPERATURE ####################################################



list_of_all_temp = []
sum_avg = 0
c = 0
for i in df['Temp']:
	list_of_all_temp.append(i)
	if i == 0 :
		pass
	else :
		sum_avg = sum_avg + i
		c = c + 1


mean_temp = sum_avg/c

print("Mean Temp = ",mean_temp)

df.to_csv('ayushi.csv')
# df['Temp'].replace(0, mean_temp)

for i in df['Temp']:
	if i == 0 :
		df[i] = mean_temp
	else:
		pass

########################### TO CALCULATE MSE FOR TEMP ############################
list_mean = []

list1 = list_of_all_temp
n = len(list1)
# print(n)
for i in range(0,n):
	list_mean.append(mean_temp)
	


MSE = np.square(np.subtract(list_mean,list_of_all_temp)).mean() 
#################################################################################









#################################################################################################


################################################# FINDING MEAN AND NO OF NAN VALUES ###########################


sum_avg = 0
c = 0
################################ NUMBER OF NAN VALUES FOR ALL ATTRIBUTES #########################################
count_temp = 0  
count_bod = 0 
count_nit = 0
count_do = 0
count_ph = 0
count_total = 0   
count_cond = 0
count_fecal = 0  


for i in df['Temp']:
	if i == 0 :
		count_temp = count_temp + 1



for i in df['D.O. (mg/l)']:
	if i == 0 :
		count_do = count_do + 1


for i in df['PH']:
	if i == 0 :
		count_ph = count_ph + 1


for i in df['CONDUCTIVITY (µmhos/cm)']:
	if i == 0 :
		count_cond = count_cond + 1



for i in df['NITRATENaN N+ NITRITENaNN (mg/l)']:
	if i == 0 :
		count_nit = count_nit + 1



for i in df['FECAL COLIFORM (MPN/100ml)']:
	if i == 0 :
		count_fecal = count_fecal + 1



for i in df['TOTAL COLIFORM (MPN/100ml)Mean']:
	if i == 0 :
		count_total = count_total + 1



for i in df['B.O.D. (mg/l)']:
	if i == 0 :
		count_bod = count_bod + 1



print("TOTAL TEMP  NAN = ",count_temp)
print("TOTAL DO  NAN = ",count_do)
print("TOTAL BOD  NAN = ",count_bod)
print("TOTAL PH  NAN = ",count_ph)
print("TOTAL FECAL  NAN = ",count_fecal)
print("TOTAL TOTAL NAN = ",count_total)
print("TOTAL CONDUCTIVITY  NAN = ",count_cond)
print("TOTAL NITRITE  NAN = ",count_nit)



df.to_csv('shanay.csv')

