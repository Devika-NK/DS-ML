import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('iris.csv')
print(data.head())

x=data.iloc[:,:4]
print(x.head())
y=data.iloc[:,-1]
print(y.head())

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.20)
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)
print(y_pred)

print("AccuracyScore: ",accuracy_score(y_test,y_pred))

plt.figure(figsize=(12, 8))
tree.plot_tree(classifier)
plt.title("Decision Tree for Iris Dataset")
plt.show()