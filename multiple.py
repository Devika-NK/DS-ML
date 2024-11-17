import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics, linear_model

data = pd.read_csv('diabetes.csv')
print(data.head())

x = data.iloc[:, 7]
print(x.head())
y = data.iloc[:, 6]
print(y.head())

x = np.array(x).reshape(-1, 1)
print(x)
y = np.array(x).reshape(-1, 1)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)
classifier = linear_model.LinearRegression()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
y_pred_train = classifier.predict(x_train)
print(y_pred)

print("R2_Score: ", metrics.r2_score(y_test, y_pred))
print("Mean_squared_error:", metrics.mean_squared_error(y_test, y_pred))
