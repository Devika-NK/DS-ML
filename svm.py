import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

data = pd.read_csv('iris.csv')
print(data.head())

x = data.iloc[:, :4]
print(x.head())
y = data.iloc[:, -1]
print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)
classifier = SVC(kernel='linear')
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print(y_pred)
print("AccuracyScore: ", accuracy_score(y_test, y_pred))
print("Confusion matrix:", confusion_matrix(y_test, y_pred))
