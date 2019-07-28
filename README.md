# Fruit Punch
Fruit Punch is a machine learning program that trains on a dataset of fruit images. The program identifies a fruit based on an image using machine learning algorithms. Data visualization based on accuracy of the machine learning model.

# Developers
1. **Ryan Talactac (Technical Manager)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Uploaded initial image set.
   1. Resolved first issue.
   1. Implementing a decision tree algorithm on remote branch
2. **Matthew Zuniga (Project Manager)**
Milestone 1:
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Created Initial README file
Milestone 2:
   1. Started current build of Python program. Initial features are:
	* Preprocessing data by generating labels, converting images to grayscale.
	* Extracting features using histogram of oriented gradients.
	* Using knn algorithm on training and testing sets to calculate accuracy.
   1. Imported fruit image data set.
Milestone 3:
	1. Finished core functionality:
	 * Added data visualization.
	 * Added decision tree algorithm.
3. **Pooja Gajjar (Product Manager)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Developed Project Idea(Fruit Image Identifier)
   1. Update Development Cycle Documentation on Trello - https://trello.com/b/9EN7AWEb
   1. Update Development Cycle Documentation on Trello
   1. Create Use-Cases to Run Tests on Project
4. **Christian Jimenez (SCRUM Master)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Research other ML Algorithms that are Supervised Learning such as decision trees
   1. Collaborated on project design document by adding description 
   
# Technical Implementation
Language(s):
* Python 3.7+

Libraries:
* pandas
* numpy
* matplotlib
* sklearn
* opencv2

Tools:
* Google Colab

## Data Preprocessing:
We will begin by using a dataset we found on Kaggle. See the references for the source to the dataset.

Since we do not have labels or CSV for our dataset, we generate the labels and array ourselves. We do this through
in `preprocessing.py.` This script contains a method to generate the labels by iterating through the `fruit/` directory
and converting each image into a numpy array. This allows us to see how correct our model is.

We preprocess our data using a function that takes our training/testing set, converts it to RGB, resizes it to 72x72
and appends it to a new array. For future considerations, we will tweak this preprocessing model and see how it fits
with the machine learning algorithm(s) we choose.

Then, the data goes through a feature extraction using `skimage` histogram of oriented gradients function. We will adjust
pixels_per_cell to see how that affects how our model learns for the 3rd milestone.

## Training:
We will train the model by using Python library sklearn.

We split the data set into a training set and testing set. We use a 80/20 split for training and testing respectively.

### K-Nearest Neighbors Algorithm
We use sklearn's `KNeigborsClassifier` method to classify given the processed numpy arrays. This is a supervised learning
algorithm so it is lazy. It does not remember what it learns like a neural network.

### Decision Tree Algorithm
We use sklearn's `DecisionTree` method to classify the images as well. This is different in that the shapes of the two
sets must be the same, i.e. the same amount of elements in the both sets. It also does decisions based on a tree-like graph
to mode possible outcomes. 

## Data Visualization:
We will visualize the data with matplotlib and test against the accuracy of the model in identifying these images.

# Usage

To use, please install the following requirements:

* Python 3.7+ (If you're on Windows, ensure that you add Python to your PATH variables when installing.)
* matplotlib `pip install --user matplotlib`
* sk-image `pip install --user scikit-image`
* scipy `pip install --user scipy`
* sklearn `pip install --user scikit-learn`
* opencv `pip install --user opencv-python`

To run the script:

1) Clone the repository. `git clone <repo>`
2) Navigate to the directory. `cd project-swifites-final-project`
3) Run the script. `python main.py`

# References

The data set we used is from here:
https://www.kaggle.com/moltean/fruits#fruits-360_dataset.zip
