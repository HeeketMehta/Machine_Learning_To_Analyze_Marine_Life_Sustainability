from sklearn.ensemble import RandomForestClassifier

import numpy as np

import pandas as pd

np.random.seed(0)
from sklearn.metrics import accuracy_score,recall_score,confusion_matrix



from sklearn.model_selection import train_test_split
# from sklearn.svm import LinearSVC
from sklearn.svm import SVC


#####  CLEANING STAGE ###############

df2 = pd.read_csv('datasets/cleaned_data_final.csv')





features = df2.columns[4:10]

# print(features)


X_1 = np.array(df2[features])

y_1 = np.array(df2['new_WQI'])

X_train, X_test, y_train, y_test = train_test_split(X_1, y_1, test_size=0.30, random_state=42)

print("no of training samples", len(y_train))  ## 45678
print("no of testing samples", len(y_test)) ## 15120


# features = df2.columns[:15]

# print(features)
# y = train['ScoreText']



from sklearn.neighbors import KNeighborsClassifier



clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)



Y_predict = clf.predict(X_test)

#








def convert_dict_value_to_string(a):
	x = list(a)
	# print(x)
	# list_Y_predict = list(Y_predict)
	for i in range (0,len(x)):
		if x[i] == 1:
			x[i] = "Excellent"
		elif x[i]==2:
			x[i] = "Good"
		elif x[i] == 3:
			x[i] = "Poor"
		else:
			x[i] = "Very Poor"
		
	alpha = np.asarray(x)
	return alpha














print(pd.crosstab(convert_dict_value_to_string(y_test), convert_dict_value_to_string(Y_predict), rownames = ['Actual Outcome'], colnames = ['Predicted Outcome']))
# print(preds[0:20])
# print(test['ScoreText'].head(20))

# print("Train acc : ", accuracy_score(train['ScoreText'], y))


print("ACCURACY :     ",accuracy_score(Y_predict, y_test)*100)




