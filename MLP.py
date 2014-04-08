#!/usr/bin/python
#coding: UTF-8

"""
Multi-Layer Perceptron class, corresponding to each individual
"""

import numpy as np

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
	return np.tanh(x)

# derivative of our sigmoid function
def dsigmoid(x):
	return 1.0 - x**2
	
	
class MLP:
	def __init__(self, *args):
		self.args = args
		n = len(args)
		
		self.layers = [np.ones(args[i] + (i==0)) for i in range(0, n)]
		
		self.weights = list()
		for i in range(n-1):
			R = np.random.random((self.layers[i].size, self.layers[i+1].size))
			self.weights.append(R)
			
		self.m = [0 for i in range(len(self.weights))]
			
		
	def update(self, inputs):
		self.layers[0][:-1] = inputs
		
		for i in range(1, len(self.layers)):
			self.layers[i] = sigmoid(np.dot(self.layers[i-1], self.weights[i-1]))

			
		return self.layers[-1]
		
		
	def backPropagate(self, inputs, outputs, a=0.1, m=0.1):
		
		error = outputs - self.update(inputs)
		de = error*dsigmoid(self.layers[-1])
		deltas = list()
		deltas.append(de)
		
		
		for i in range(len(self.layers)-2, 0, -1):

			deh = np.dot(deltas[-1], self.weights[i].T) * dsigmoid(self.layers[i])
			deltas.append(deh)
			
		deltas.reverse()
		
		for i, j in enumerate(self.weights):
			
			layer = np.atleast_2d(self.layers[i])
			delta = np.atleast_2d(deltas[i])
			
			dw = np.dot(layer.T,delta)
			self.weights[i] += a*dw + m*self.m[i]
			self.m[i] = dw
			


if __name__ == '__main__':
	pat = (((0, 0), 0),
		((0, 1), 1),
		((1, 0), 1),
		((1, 1), 0))


	network = MLP(2, 3, 1)

	for i in range(1000):
		for p in pat:
			network.backPropagate(p[0], p[1])
		
	for p in pat:
		print network.update(p[0])




