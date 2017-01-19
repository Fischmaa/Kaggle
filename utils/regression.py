"""
	Regressions
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""
import numpy as np

def eveGradientDescent(train, trainLabels, error, errorGrad, test=None, testLabels=None,
	 maxIter = 10000, learningRate = 0.01, regularization = 0.001,
	testTime = 100,
	b1 = 0.9, b2 = 0.999, b3 = 0.999, epsilon = 10**(-8), k = 0.1, K = 10):
	"""
	Computes the gradient descent in order to predict labels thanks to the eve algorithm
	-> Binary classification
	"""
	lossesTrain = []
	weight = np.zeros(train[0].shape)

	# Moving averages
	m = np.zeros(weight.shape)
	v = np.zeros(weight.shape)
	# To compute them
	b1t = 0
	b2t = 0
	# Adaptative learning rate
	d = 1
	# Loss of the last epoch
	oldLoss = 0

	for i in range(maxIter):
		if i > 1000:
			b1t =1
			b2t =1
		else:
			b1t *= b1
			b2t *= b2
		loss = 0
		grad = np.zeros(weight.shape)

		# Computes the full gradient and error
		for j in range(len(train)):
			grad += errorGrad(train[j], trainLabels[j], weight)/len(train)
			loss += error(train[j], trainLabels[j], weight)/len(train)

		grad += regularization*weight

		# Updates the moving averages
		m = b1*m + (1-b1)*grad
		mh = m / (1-b1t)

		v = b2*v + (1-b2)*np.multiply(grad,grad)
		vh = v/(1-b2t)

		# Updates the adaptative learning rate
		if (i > 0):
			# In order to bound the learning rate
			if loss < oldLoss:
				delta = k + 1
				Delta = K + 1
			else:
				delta = 1/(K+1)
				Delta = 1/(k+1)
			c = min(max(delta, loss/oldLoss), Delta)
			oldLossS = oldLoss
			oldLoss = c*oldLoss
			# Computes the feedback of the error function (normalized)
			r = abs(oldLoss - oldLossS)/(min(oldLoss,oldLossS))
			# Updates the correction of learning rate
			d = b3*d + (1-b3)*r
		else:
			oldLoss = loss

		# Updates the weight
		weight -= learningRate*(np.multiply(mh,1/(d*np.sqrt(vh) + epsilon)))

		# Computes the error on the training and testing sets
		if (i % testTime == 0):
			print("Iteration : {} / {}".format(i+1, maxIter))
			print("\t-> Train Loss : {}".format(loss))
			lossesTrain.append(loss)

			if trainLabels is not None and testLabels is not None:
				loss = 0
				for j in range(len(test)):
					loss += error(test[j], testLabels[j], weight)/len(test)
				print("\t-> Test Loss : {}".format(loss))

	return weight, lossesTrain
