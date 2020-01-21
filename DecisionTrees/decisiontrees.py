import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
#Importing the dataframe
df=pd.read_csv("/home/david/Desktop/fCharlie/assignments/iris/Iris.csv")

#Creating an array of the dataset.
array=df.values
#Designating the feature columns and target output columns
X= array[:,0:4]#Picks from the zero to the forth column
Y=array[:,5]#Picks the values of the forth column  only.

#Splitting the dataset into train and test sets.
X_train, X_test, Y_train,Y_test = train_test_split(X,Y, train_size=0.7, random_state=1)

#Initializing the classifier.
decision_tree=DecisionTreeClassifier()
#Training the algorithmn.
decision_tree.fit(X_train, Y_train)
#Checking the accuracy of the algorithmn.
print(decision_tree.score(X_test,Y_test))
