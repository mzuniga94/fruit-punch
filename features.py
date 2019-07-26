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

def HOGExtract(image):
    feature, _ = hog(image, orientations=8, pixels_per_cell=(32, 32),
                 cells_per_block=(1, 1), visualize=True, multichannel=False)
    return feature

def ExtractFeature(argSet):
    features = []

    for i in range(np.shape(argSet)[0]):
        features.append(HOGExtract(argSet[i]))

    return features