"""
  -------------------------------------------------------------------------------------------
  Group: T-Swift
  Members: Matthew Zuniga, Ryan Talactac, Christian Jimenez, Pooja Gajjar
  File: main.py

  Description: The main program to run.
  -------------------------------------------------------------------------------------------
"""

"""
  -------------------------------------------------------------------------------------------
  @TODO: Check for redundant import statements. 
  Import statements.
  -------------------------------------------------------------------------------------------
"""
import numpy as np
import preprocessing
import features
import visualization

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

"""
-------------------------------------------------------------------------------------------
Initializing the lists for the fruits in our data set.
-------------------------------------------------------------------------------------------
"""
apple = []
banana = []
cherry = []
kiwi = []
lemon = []
mango = []
pear = []
strawberry = []

"""
-------------------------------------------------------------------------------------------
From preprocessing.py, use GenerateLabels method to generate the labels and append them
to their respective fruit lists.
-------------------------------------------------------------------------------------------
"""
apple, label_apple = preprocessing.GenerateLabels(apple,"apple", 2)
banana, label_banana = preprocessing.GenerateLabels(banana,"banana", 2)
cherry, label_cherry = preprocessing.GenerateLabels(cherry,"cherry", 2)
kiwi, label_kiwi = preprocessing.GenerateLabels(kiwi,"kiwi", 1)
lemon, label_lemon = preprocessing.GenerateLabels(lemon,"lemon", 1)
mango, label_mango = preprocessing.GenerateLabels(mango,"mango", 2)
pear, label_pear = preprocessing.GenerateLabels(pear,"pear", 2)
strawberry, label_strawberry = preprocessing.GenerateLabels(strawberry,"strawberry", 1)

"""
-------------------------------------------------------------------------------------------
Printing the number of images in each folder and label.
-------------------------------------------------------------------------------------------
"""
print("Number of images in apple: " + str(len(apple)))
print("Number of images in banana: " + str(len(banana)))
print("Number of images in cherry: " + str(len(cherry)))
print("Number of images in kiwi: " + str(len(kiwi)))
print("Number of images in lemon: " + str(len(lemon)))
print("Number of images in mango: " + str(len(mango)))
print("Number of images in pear: " + str(len(pear)))
print("Number of images in strawberry: " + str(len(strawberry)))

"""
-------------------------------------------------------------------------------------------
Concatenate the sets. The X set w,ill have the lists. The Y set will have labels.
-------------------------------------------------------------------------------------------
"""
# Concatenate the shape with the lists.
X = np.concatenate((apple, banana, cherry, kiwi, lemon, mango, pear, strawberry))

# Concatenate the label with the labels.
Y = np.concatenate((label_apple, label_banana, label_cherry, label_kiwi, label_lemon, label_mango, label_pear, label_strawberry))

"""
-------------------------------------------------------------------------------------------
In order to make an accurate model, we need to split the data into two sets: A training and
testing set. We have an X train, X test, Y train, and Y test.

From the sklearn library, we use the train_test_split method.

@param X: The list with the concatenated image array.
@param Y: The list with the concatenated label array.
@test_size: The size to split the test/train set. This means 80% training set, 20% test set.
@random_state: Randomizes the test/train set. Can set to any value.
-------------------------------------------------------------------------------------------
"""

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=np.random)

"""
-------------------------------------------------------------------------------------------
Printing the sum of all sets and the shape of the train/test sets.
-------------------------------------------------------------------------------------------
"""

print("Sum of all sets: ", len(apple)+len(banana)+len(cherry)+len(kiwi)+len(mango)+len(lemon)+len(pear)+len(strawberry))
print("Shape of X training set:", X_Train.shape[0])
print("Shape of X test set:", X_Test.shape[0])

processed_X_Train = preprocessing.DataPreprocess(X_Train)
processed_X_Test = preprocessing.DataPreprocess(X_Test)

feature_X_Train = features.ExtractFeature(processed_X_Train)
feature_X_Test = features.ExtractFeature(processed_X_Test)

"""
-------------------------------------------------------------------------------------------
Here we are using sklearn methods to do supervised learning through the K-Nearest Neighbors
Algorithm. knn algorithm will try to find the nearest neighbors, usually represented on a
graph as a dot to find a classification. A lower value of k (n_neighbors) overfits data while
a high value of k, smooths data. This is a supervised learning algorith,.

@param n_jobs: Amount of jobs/epochs to do.
@param weights: Euclidean distance used as the heuristic to determine correctness.
@param n_neighbors: The amount of neighbors that the algorithm samples for correctness.
-------------------------------------------------------------------------------------------
"""

knn = KNeighborsClassifier(n_jobs=-1, weights='distance', n_neighbors=333) # Modify neighbors
knn.fit(feature_X_Train, Y_Train) # See how the labels compare to the X train set with features.

y_knn_prediction = knn.predict(feature_X_Test)

dt = tree.DecisionTreeClassifier()
dt = dt.fit(feature_X_Train, Y_Train)
y_dt_prediction = dt.predict(feature_X_Test)

print("The accuracy of knn algorithm is: ", accuracy_score(Y_Test, y_knn_prediction)*100, '%')
print("The accuracy of decision tree algorithm is: ", accuracy_score(Y_Test, y_dt_prediction)*100, '%')

visualization.ShowDataSetPlot(apple, banana, cherry, kiwi, lemon, mango, pear, strawberry)
visualization.PlotTest(X_Test, y_knn_prediction)