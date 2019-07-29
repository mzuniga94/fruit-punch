"""
  -------------------------------------------------------------------------------------------
  Group: T-Swift
  Members: Matthew Zuniga, Ryan Talactac, Christian Jimenez, Pooja Gajjar
  File: features.py

  Description: Contains methods for extracting features for the data.
  -------------------------------------------------------------------------------------------
"""

import numpy as np
from skimage.feature import hog


"""
-------------------------------------------------------------------------------------------
@function HOGExtract(): Extracts histogram of an image and stores it into features. 
@param Type: Takes in an image 
@param Type: List. argYKNNPrediction: The y knn prediction with labels.
@returns: features 
-------------------------------------------------------------------------------------------
"""


def HOGExtract(image):
    feature, _ = hog(image, orientations=8, pixels_per_cell=(32, 32),
                 cells_per_block=(1, 1), visualize=True, multichannel=False)
    return feature

"""
-------------------------------------------------------------------------------------------
@function ExtractFeature(): Loops through data set and calls HOGEXTRACT to store features
in an array
@param Type: argSet. Data Set.
@returns: Array of features 
-------------------------------------------------------------------------------------------
"""


def ExtractFeature(argSet):
    features = []

    for i in range(np.shape(argSet)[0]):
        features.append(HOGExtract(argSet[i]))

    return features
