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
pop = population(inputs=(1, 0), sol=0)

print 'population start with a fittest of %f%%' % (pop.getFittest()[0]*100)

# First generation
gen = 1

bestValue = 0.0

while bestValue < 1.0: 
	
	bestValue, bestIndi = pop.getFittest()
	if not gen % 100 :
		print 'Generation {0} : fittest = {1}%'.format(gen, bestValue*100.0)
	pop.evolve()
	gen += 1
	
bestValue, bestIndi = pop.getFittest()
print '\npopulation end with a fittest of', bestValue

print'best individual gives answer to 1 XOR 1 :', float(bestIndi.update((1, 0))), '\n'
