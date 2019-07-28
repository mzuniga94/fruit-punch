"""
  -------------------------------------------------------------------------------------------
  Group: T-Swift
  Members: Matthew Zuniga, Ryan Talactac, Christian Jimenez, Pooja Gajjar
  File: features.py

  Description: Contains methods for data visualization.
  -------------------------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt

"""
-------------------------------------------------------------------------------------------
@function ShowDataSetPlot(): Shows the first image of each list on a pyplot.
@param Type: List. argAppleSet: The apple set to pass in.
@param Type: List. argBananaSet: The banana set to pass in.
@param Type: List. argCherrySet: The cherry set to pass in.
@param Type: List. argKiwiSet: The kiwi set to pass in.
@param Type: List. argLemonSet: The lemon set to pass in.
@param Type: List. argMangoSet: The mango set to pass in.
@param Type: List. argPearSet: The pear set to pass in.
@param Type: List. argStrawberrySet: The strawberry set to pass in.
@returns: None. 
-------------------------------------------------------------------------------------------
"""
def ShowDataSetPlot(argAppleSet, argBananaSet, argCherrySet, argKiwiSet, argLemonSet, argMangoSet, argPearSet, argStrawberrySet):
    fig = plt.figure()

    axis1 = fig.add_subplot(4,4,1)
    axis1.set_title('Apple')
    axis1.set_axis_off()
    axis1.imshow(argAppleSet[0])

    axis2 = fig.add_subplot(4,4,2)
    axis2.set_title('Banana')
    axis2.set_axis_off()
    axis2.imshow(argBananaSet[0])

    axis3 = fig.add_subplot(4,4,3)
    axis3.set_title('Cherry')
    axis3.set_axis_off()
    axis3.imshow(argCherrySet[0])

    axis4 = fig.add_subplot(4,4,4)
    axis4.set_title('Kiwi')
    axis4.set_axis_off()
    axis4.imshow(argKiwiSet[0])

    axis5 = fig.add_subplot(4,4,5)
    axis5.set_title('Lemon')
    axis5.set_axis_off()
    axis5.imshow(argLemonSet[0])

    axis6 = fig.add_subplot(4,4,6)
    axis6.set_title('Mango')
    axis6.set_axis_off()
    axis6.imshow(argMangoSet[0])

    axis7 = fig.add_subplot(4,4,7)
    axis7.set_title('Pear')
    axis7.set_axis_off()
    axis7.imshow(argPearSet[0])

    axis8 = fig.add_subplot(4,4,8)
    axis8.set_title('Strawberry')
    axis8.set_axis_off()
    axis8.imshow(argStrawberrySet[0])

    plt.show()

"""
-------------------------------------------------------------------------------------------
@function PlotTest(): Plots the X train set and labels with respect to KNN prediction.
@param Type: List. argXTest: The randomized X test set.
@param Type: List. argYKNNPrediction: The y knn prediction with labels.
@returns: None. 
-------------------------------------------------------------------------------------------
"""
def PlotTest(argXTest, argYKNNPrediction):
    amountToPlot = 20

    plt.figure(figsize=(16, 8))
    for i in range(amountToPlot):
        plt.subplot(1, amountToPlot, i + 1)
        plt.imshow(argXTest[i], interpolation='nearest')
        plt.text(0, 0, argYKNNPrediction[i], color='black',
                 bbox=dict(facecolor='white', alpha=1))
        plt.axis('off')

    plt.show()