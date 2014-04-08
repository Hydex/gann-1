#!/usr/bin/python
#coding: UTF-8

"""
Initiate a population with a solution to my problem (XOR for the combination (1, 0), solution should be 1.
Evolve the population a few 2000 times before getting the result of the final test as a float.
Using numpy and radom module.
"""

from time import time

from pop import *

# Initiatiing a population with the input and the solution (i.e. (1 XOR 0) -> 1)
pop = population(inputs=(1, 1), sol=0)

print 'population start with a fittest of', pop.getFitness(pop.getFittest())

# First generation

for gen in range(1, 2001):

	if not gen % 100 : print 'Generation', gen, ': fittest =', pop.getFitness(pop.getFittest())
	pop.evolve()

best = pop.getFittest()
print '\npopulation end with a fittest of', pop.getFitness(best)

print'best individual gives answer to 0 XOR 1 :', float(best.update((1, 1))), '\n'
