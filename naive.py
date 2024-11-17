import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

data = pd.read_csv('iris.csv')
print(data.head())

x = data.iloc[:, :4]
print(x.head())

y = data.iloc[:, -1]
print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)
print(x_train.head())
print(x_test.head())

sc = StandardScaler()
sc.fit(x_train)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

classifier = GaussianNB()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print(y_pred)
print(y_test)

print("Accuracy : ", metrics.accuracy_score(y_test, y_pred))
print("Confusion matrix:", metrics.confusion_matrix(y_test, y_pred))
