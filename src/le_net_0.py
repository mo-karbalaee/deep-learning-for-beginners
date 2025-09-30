#----------------------------------
# Exercise: LeNet
#----------------------------------
# The original python file can be reloaded by typing %load src/le_net_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/le_net.py
# This will save the result to a python file, which you will need for the next exercises.

from src.network import NeuralNetwork
## Load here your implementations of the previous exercises
from src.layers.initializers import He, Const, UniformRandom
from src.layers.conv import FlattenLayer, ConvolutionalLayer
from src.layers.fully_connected import FullyConnectedLayer
from src.layers.pooling import MaxPoolLayer
from src.layers.activation_functions import ReLU, Sigmoid
from src.layers.softmax_crossentropy import SoftMaxCrossEntropyLoss

def build():
    """ returns: a neural network architecture built according to the provided specification
    """ 
    
    net = NeuralNetwork(He(), Const(0.1))
    learning_rate = 0.001
    categories = 10  # MNIST, numbers 0-9
    
    # TODO: Implement the architecture of LeNet by adding layers to net. 
    # Have a look at the NeuralNetwork class how layers can be added.
    # To call the constructors of the layers, have a look at your implementations of the previous exercises.
    
    return net