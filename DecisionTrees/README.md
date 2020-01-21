                                          #CODE DOCUMENTATION.
#Decision Tree Classifier With 97.777777% accuracy.
1.Introduction.

This program aims at implementing a decision tree classifier on the Iris dataset.

The dataset is available from the following link https://www.kaggle.com/uciml/iris.

To implement the program download the csv file into your local machine and note the directory of the dataset.



2.code Description.

    a).We first import pandas to be used in reading the csv files.
    
    b).We then import the model to be used, DecisionTreeClassifier from sklearn.tree library.
    
    c.).We then import the train_test_split method form sklearn.model_selection library.
    
    d.).Read the dataset using the method read_csv from pandas.
    
    c.).Using df.head(5) method we print the first 5 entries in the dataset just to ascertain the entries.
    
    d.).We then divide the dataset columns into feature columns and target columns
    
    e.).The dataset values are then split into a set of test values and training values
    
          with a training size of 70% and a test size of 30% using the train_test_split method.
    f.).Initialize the classifier.
    
    g.).We then train the classifier algorithm using the fit method of the classifier.
    
    h.).We then check the accuracy of the algorithm using the score method of the classifier.
