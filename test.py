"""
	Test - Test the different classifiers
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

import dataManipulation
from utils.distances import *
from utils.error import *
import model.knn
import model.oneVsAll
import model.logistic

# Defines the percentage of data used for training
TRAIN = 0.9

print("Extract Data and shuffles")
data = dataManipulation.extractPicturesFromCSV("data/Xtr.csv")
labels = dataManipulation.extractLabelsFromCSV("data/Ytr.csv")
length = int(len(labels)*TRAIN)

data, label = dataManipulation.shuffleDataLabel(data, labels)

# Separates between train and test sets
trainData, trainLabels = data[:length], labels[:length]
testData, testLabels = data[length:], labels[length:]

"""
# KNN
print("Test knn classifier - Kernel - 5")
knn = model.knn.ClassifierKNN(distanceKernelPoly, nearestNeighbor=5)
knn.train(trainData, trainLabels, testData, testLabels)

print("Test knn classifier - Euclidean - 3")
knn = model.knn.ClassifierKNN(distance, 3)
knn.train(trainData, trainLabels, testData, testLabels)

print("Test knn classifier - distanceKernelRBS - 5")
knn = model.knn.ClassifierKNN(distance, 5)
knn.train(trainData, trainLabels, testData, testLabels)
"""

# Logistic regression
print("Test one vs all logistic regression")
ova = model.oneVsAll.oneVsAll(model.logistic.ClassifierLogistic, error=logisticLoss, errorGrad=logisticGrad)
ova.train(trainData, trainLabels, testData, testLabels)
