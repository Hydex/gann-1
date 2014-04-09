GANN - Clear meaning
===================

GANN is a combination of GA, for genetic algorithme, and ANN, for Artificial Neural Network.
This project will join these to notions into one single algorithme.

First part : ANN
----------------

We want to create a simple neural network in order to solve the XOR logic gate. The easeiest way to do it is by changing the wieghts through the backretropropagation algorithme. Unless this time, we are trying a whole new method to approach the solution. Note that the learning function has been coded, but is not used during the process.

Second part : GA
-----------------

That's when the genetic algos come handy : we use a simple population of neural networks to improve the weights. Each time the population evolve, it selects the best individuals, i.e. the neural networks with the better weights, and use them in order to create the next generation.

Evolution : The evolution and selection structure I'm currently using are not the methods we usually use in genetic algorithme, details can be found at http://synbiozis.pythonanywhere.com/.

Others methods : - the fitness is defined using the result of a individual for the logic gate, the closer it is to the solution, the greater the fitness will be.
                 - the mutation method is yet to be changed. For now, every layer of a individual has a 2% chance to be multiplied by a random float between 0 and 2.

Ending
------

After the population has reached the solution, we stop the loop and get the best individual from the last population, then run the XOR gate on him.


Code
====

The project is coded in python, though MLP and population library were created using cython, in order to speed things up a litlle. Feel free to use .so/.py files.

The algorithmes themselfves are quite simple, it should be to hard to translate into any other language.

