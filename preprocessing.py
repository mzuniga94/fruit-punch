"""
  -------------------------------------------------------------------------------------------
  Group: T-Swift
  Members: Matthew Zuniga, Ryan Talactac, Christian Jimenez, Pooja Gajjar
  File: preprocessing.py

  Description: Contains data preparation and preprocessing methods.
  -------------------------------------------------------------------------------------------
"""

import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage.transform import resize

"""
-------------------------------------------------------------------------------------------
@function LoadImage(): Load images and assigns labels.
@param Type: List. argLabelArray: Array to return with labels generated from data set.
@param Type: String. argFruitName: Name of the fruit
@param Type: Integer. argNumDirectories: Number of directories to search.
@returns: Types: List (argLabelArray), String (label). Returns the argLabelArray and label.
-------------------------------------------------------------------------------------------
"""
def GenerateLabels(argLabelArray, argFruitName, argNumDirectories):
    label = []

    for folderNumber in range(argNumDirectories):
        directory = "fruit/" + argFruitName + str(folderNumber + 1) + "/*.jpg"
        print(directory)
        for file in glob.glob(directory):
            image = np.asarray(plt.imread(file))
            argLabelArray.append(image)
            label.append(argFruitName)
    return argLabelArray, label

"""
-------------------------------------------------------------------------------------------
@function DataPreprocess(): Preprocesses the image arrays we .
@param Type: List. argSet: The training/testing set.
@returns: Type: List preprocess: Returns the processed set.
-------------------------------------------------------------------------------------------
"""
def DataPreprocess(argSet):
    processed = []

    for i in range(np.shape(argSet)[0]):
        image = cv2.cvtColor(argSet[i], cv2.COLOR_BGR2GRAY)
        image = resize(image, (72, 72), anti_aliasing=True)
        processed.append(image)

    return processed