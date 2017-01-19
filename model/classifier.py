"""
	Classification
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

import dataManipulation

class Classifier:
	"""
	Structure for any classifiers
	"""

	def predict(self, data, **kwargs):
		"""
		Forecasts the output given the data
		"""
		pass

	def test(self, testData, testLabels = None, save = None):
		"""
		Tests the model on the given data and computes the mean error and
		the accuaracy of the model if labels are given
		"""
		if testData is not None:
			recognized = 0
			output = []
			for i in range(len(testData)):
				res = self.predict(testData[i])
				output.append(res)
				if testLabels is not None and res == testLabels[i]:
					recognized += 1

			print("Total of correct forecasts : " + str(recognized) + " / " + str(len(testData)))

			if save is not None:
				dataManipulation.saveLabelsToCsv(output, save)

	def train(self, trainData, trainLabels, testData = None, testLabels=None, **kwargs):
		"""
		Trains the model and measure on the test data
		"""
		pass