import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('datasets/state.csv')


df.groupby(df['year'])



list_Excellent = []
list_good = []
list_poor = []
list_verypoor = []
list_unsuitable = []



x = df.loc[df['year'] == 2014, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)


# print(list_good)



x = df.loc[df['year'] == 2013, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)



x = df.loc[df['year'] == 2012, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)




x = df.loc[df['year'] == 2011, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)






x = df.loc[df['year'] == 2010, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)





x = df.loc[df['year'] == 2009, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)



x = df.loc[df['year'] == 2008, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)





x = df.loc[df['year'] == 2007, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)



x = df.loc[df['year'] == 2006, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)




x = df.loc[df['year'] == 2005, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)





x = df.loc[df['year'] == 2004, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)





x = df.loc[df['year'] == 2003, 'new_WQI']
listx = []
for i in x:
	listx.append(i)

n_Excellent = listx.count(1)
n_good = listx.count(2)
n_poor = listx.count(3)
n_verypoor = listx.count(4)
n_unsuitable = listx.count(5)
# n_good = listx.count(2)
list_Excellent.append(n_Excellent)
list_good.append(n_good)
list_poor.append(n_poor)
list_verypoor.append(n_verypoor)
list_unsuitable.append(n_unsuitable)




list_year = ['2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003']

# print(list_year.reverse())
df2 = pd.DataFrame(list(zip(list_year, list_Excellent, list_good, list_poor, list_verypoor, list_unsuitable)), columns = ['Year','Excellent','Good','Poor','Very_Poor','Unsuitable'])


df2.to_csv('datasets/year_vs_new_wqi.csv')
# 

ax = plt.gca()

df2.plot(kind='line',x='Year',y='Excellent',ax=ax, marker='o', markersize=2)
df2.plot(kind='line',x='Year',y='Good', color='orange', ax=ax, marker='o', markersize=2)
df2.plot(kind='line',x='Year',y='Poor',ax=ax, color='green', marker='o', markersize=2)
df2.plot(kind='line',x='Year',y='Very_Poor', color='brown', ax=ax, marker='o', markersize=2)
df2.plot(kind='line',x='Year',y='Unsuitable', color='purple', ax=ax, marker='o', markersize=2)




plt.xlabel('Year')
plt.ylabel('Number of WQI Values')


plt.show()
