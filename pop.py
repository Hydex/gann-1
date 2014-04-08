"""
Population class, includes main function such as evolve, getFitness, selection...
"""

from random import randrange, choice, random

import numpy as np

from MLP import MLP

class population:
	
	# Initialisation
	def __init__(self, inputs=(0, 1), sol=1, size=50, mut=2):
		self.pop = [self.generate() for i in range(size)]
		self.mut = mut
		self.sol = sol
		self.inputs = inputs
		
	# Evolve population
	def evolve(self):
	
		self[-1] = self.getFittest()
		next = list()
		
		selections = [self.selection(len(self)/10) for _ in range(2)]
		
		for indis in zip(*selections):
			for elt in self.crossover(indis, 10):
				next.append(self.mutate(elt))
				
		self.pop[:-1] = next[:-1]
		
	# Evolving methods
	def selection(self, iterations):
		indis = [self.getFitness(i) for i in self]
		totalFitness = sum(list(indis))

		for _ in range(iterations):
			r = randrange(int(totalFitness))
			s = 0
			for index, value in enumerate(indis):
				s += value
				if s >= r:
					yield self[index]
					break
	
	
	def crossover(self, indis, n):
		j, k = indis
		for _ in range(n/2):
			x, y = [MLP(2, 3, 2) for _ in range(2)]
			x.weights[0] = j.weights[0]
			x.weights[1] = k.weights[1]
			
			y.weights[0] = k.weights[0]
			y.weights[1] = j.weights[1]
			
			yield x
			yield y
	
	def mutate(self, indi):
		if randrange(100) <= self.mut:
			new = MLP(2, 3, 1)
		
			new.weights[0] = np.dot(indi.weights[0], MLP(2, 3, 1).weights[0])
			return new
		else:
			return indi

	def generate(self):
		return MLP(2, 3, 1)
		
	def getMaxFit(self):
		return 0
	
	# Fitness calc
	def getFittest(self):
		return sorted([(self.getFitness(indi), indi) for indi in self])[0][1]
		
	def getFitness(self, indi):	
		return abs(self.sol - float(indi.update(self.inputs)))
	
	# Specials methods
	def __getitem__(self, i):
		return self.pop[i]
		
	def __setitem__(self, i, val):
		self.pop[i] = val
		
	def __len__(self):
		return len(self.pop)



	
