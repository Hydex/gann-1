GANN - Clear meaning
===================

GANN is a combination of GA, for genetic algorithme, and ANN, for Artificial Neural Network.
This project will join these to notions into one single algorithme.

First part : ANN
----------------

We want to create a simple neural network in order to solve the XOR logic gate. The easeiest way to do it is by changing the wieghts through the backretropropagation algorithme. Unless this time, we are trying a whole new method to approach the solution.

Second part : GA
-----------------

That's when the genetic algos come handy : we use a simple population of neural networks to improve the weights. Each time the population evolve, it selects the best individuals, i.e. the neural networks with the better weights, and use them in order to create the next generation.

Ending
------

As we can't actually *reach* the solution, we dicide that after around 2000 generations, most of the evolution has been done. We stop the loop and get the best individual from the last population, then run the XOR gate on him.


Code
====

The project is coded in python, though MLP and population library were created using cython, in order to speed things up a litlle. Feel free to use .so/.py files.

The algorithmes themselfves are quite simple, it should be to hard to translate into any other language (I might try that some day).

Future
======

I will continue improving my code, in order to find other uses to my project.
