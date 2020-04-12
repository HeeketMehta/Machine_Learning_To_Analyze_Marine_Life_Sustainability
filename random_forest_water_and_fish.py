from sklearn.ensemble import RandomForestClassifier

import numpy as np

import pandas as pd

np.random.seed(0)

from sklearn.metrics import accuracy_score,recall_score,confusion_matrix



from sklearn.model_selection import train_test_split

df2 = pd.read_csv('datasets/cleaned_data_final.csv')


def water_quality_classification(df2, target_var):


	features = df2.columns[3:10]

	# print(features)


	X_1 = np.array(df2[features])

	y_1 = np.array(df2[target_var])

	X_train, X_test, y_train, y_test = train_test_split(X_1, y_1, test_size=0.30, random_state=42)




	print()

	print("no of training samples = ", len(y_train))
	print("no of testing samples = ", len(y_test))



	clf = RandomForestClassifier(n_jobs= 2, random_state = 0)

	clf.fit(X_train, y_train)

	# Y_predict = clf.predict([[29.7,	5.8,	6.9,	64,	3.8,	0.5,	8443]])
	# 18.3	1	7.2	376	57.2	20.3	83554 are tuples for row 229 (MEGHALAYA) WITH ACTUAL OUTPUT VERY POOR


	# 29.7	5.8	6.9	64	3.8	0.5	8443 are tuples for row 5 (GOA) WITH ACTUAL OUTPUT POOR

	Y_predict = clf.predict(X_test)





	def convert_dict_value_to_string(a):
		x = list(a)
		for i in range (0,len(x)):
			if x[i] == 1:
				if (target_var is 'new_WQI'):
					x[i] = "Excellent"
				else:
					x[i] = "Desirable Water"
			elif x[i]==2:
				if (target_var is 'new_WQI'):
					x[i] = "Good"
				else:
					x[i] = "Acceptable Water"
			elif x[i] == 3:
				if (target_var is 'new_WQI'):
					x[i] = "POOR"
				else:
					x[i] = "Harmful Water"
			elif x[i] == 4:
				x[i] = "Very Poor"
			else:
				x[i] = "Unsuitable"
			
		alpha = np.asarray(x)
		return alpha


	# print(convert_dict_value_to_string(Y_predict))

	print()


	print(pd.crosstab(convert_dict_value_to_string(y_test), convert_dict_value_to_string(Y_predict), rownames = ['Actual Outcome'], colnames = ['Predicted Outcome']))

	# results = confusion_matrix(y_test, Y_predict) 
	# print(results)
	print("ACCURACY :     ",accuracy_score(Y_predict, y_test)*100)








print("OUTPUT FOR WATER QUALITY ANALYSIS IS GIVEN BY - ")

water_quality_classification(df2, 'new_WQI')

print()

print()

print("-------------------------------------------------------------------------")

print("-------------------------------------------------------------------------")


print()

print()


print("OUTPUT FOR FISH CLASSIFICATION IS GIVEN BY - ")

water_quality_classification(df2, 'new_WQI_fishes')