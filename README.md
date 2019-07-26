# Fruit Punch
Fruit Punch is a machine learning program that trains on a dataset of fruit images. The program identifies a fruit based on an image using machine learning algorithms. Data visualization based on accuracy of the machine learning model.

# Developers
1. **Ryan Talactac (Technical Manager)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. ...
   1. ...
2. **Matthew Zuniga (Project Manager)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Created Initial README file
   1. Started current build of Python program. Initial features are:
	* Reading fruit image data set from directories as an array of RGB pixels.
	* Appending labels to list of images.
	* Using knn algorithm.
   1. Imported fruit image data set.
3. **Pooja Gajjar (Product Manager)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. Developed Project Idea(Fruit Image Identifier)
   1. ...
4. **Christian Jimenez (SCRUM Master)**
   1. Collaborated on brainstorming project ideas(google hangouts)
   1. ...
   1.  ...
   
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

##Data Preprocessing:
We will begin by using a dataset we found on Kaggle. See the references for the source to the dataset.

Since we do not have labels or CSV for our dataset, we generate the labels and array ourselves. We do this through
in `preprocessing.py.` This script contains a method to generate the labels by iterating through the `fruit/` directory
and converting each image into a numpy array. This allows us to see how correct our model is.

We preprocess our data using a function that takes our training/testing set, converts it to RGB, resizes it to 72x72
and appends it to a new array. For future considerations, we will tweak this preprocessing model and see how it fits
with the machine learning algorithm(s) we choose.

Then, the data goes through a feature extraction using `skimage` histogram of oriented gradients function. We will adjust
pixels_per_cell to see how that affects how our model learns for the 3rd milestone.

##Training:
We will train the model by using Python library sklearn.

We split the data set into a training set and testing set. We use a 80/20 split for training and testing respectively.

###K-Nearest Neighbors Algorithm
We use sklearn's `KNeigborsClassifier` method to classify given the processed numpy arrays. This is a supervised learning
algorithm so it is lazy. It does not remember what it learns like a neural network.

We hope to implement another machine learning algorithm by the 3rd milestone.

##Data Visualization:
We will visualize the data with matplotlib and test against the accuracy of the model in identifying these images.

We will implement this by the 3rd milestone.

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