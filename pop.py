"""
Population class, includes main function such as evolve, getFitness, selection...
"""

from random import randrange, choice, random

import numpy as np

from MLP import MLP

class population:
	
	# Initialisation
	def __init__(self, inputs=(1, 1), sol=0, size=50, mut=2):
		self.pop = [self.generate() for i in range(size)]
		self.mutationRatio = mut
		self.sol = 1
		self.inputs = (1, 0)
		
	# Evolve population
	def evolve(self):
	
		self[-1] = self.getFittest()[1]

		next = list()
		
		selections = [self.selection(len(self)/10) for _ in range(2)]
		
		for indis in zip(*selections):
			next.extend([elt for elt in self.mutate(self.crossover(indis, 10))])
							
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
			x, y = [MLP(2, 3, 1) for i in range(2)]
			
			r = randrange(1, len(j.args)-1)
			
			for i in range(r):
				x.weights[i] = j.weights[i]
				y.weights[i] = k.weights[i]
				
			for i in range(r, len(j.args)-1):
				x.weights[i] = k.weights[i]
				y.weights[i] = j.weights[i]
				
			yield x
			yield y
	
	def mutate(self, indis):
		for indi in indis:
			indi.weights = [weight * random() * 2 if randrange(100) <= self.mutationRatio else weight for weight in indi.weights]
			yield indi

	def generate(self):
		return MLP(2, 3, 1)
		
	def getMaxFit(self):
		return 0
	
	# Fitness calc
	def getFittest(self):
		return sorted([(self.getFitness(indi), indi) for indi in self])[-1]
		
	def getFitness(self, indi):
		#print '\n', indi.args, '\n'
		return 1 - abs(self.sol - float(indi.update(self.inputs)))
	
	# Specials methods
	def __getitem__(self, i):
		return self.pop[i]
		
	def __setitem__(self, i, val):
		self.pop[i] = val
		
	def __len__(self):
		return len(self.pop)



	
