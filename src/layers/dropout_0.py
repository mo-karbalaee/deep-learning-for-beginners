#----------------------------------
# Exercise: Dropout
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/dropout_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/dropout.py
# This will save the result to a python file, which you will need for the next exercises.


from src.base import BaseLayer, Phase
from src.layers.initializers import He, Const #your results of previous exercises
from src.layers.conv import FlattenLayer, ConvolutionalLayer #your results of previous exercises
from src.layers.fully_connected import FullyConnectedLayer #your results of previous exercises
from src.layers.pooling import MaxPoolLayer #your results of previous exercises

class DropOut(BaseLayer):
    
    def __init__(self, probability):
        """ DropOut Layer.
            param: probability: probability of each individual activation to be set to zero, in range [0, 1]    
        """
        super().__init__()
        # TODO: Implement initialization        
        pass
    
    def forward(self, x):
        """ Forward pass through the layer: Set activations of the input randomly to zero.
            param: x (np.ndarray): input
            returns (np.ndarray): a new array of the same shape as x, after dropping random elements
        """
        # TODO: Implement forward pass of the Dropout layer
        
        #Forward pass for training
        if self.phase == Phase.train:
            #define a binary mask that applies a random choice [0,1] for each pixel with the probability [1-p,p]
            self.mask = #TODO
            #compute the inverted dropout: x*mask/p
            #TODO: return result of inverted dropout
        
        #Forward pass for testing
        else: 
            #TODO: return result for test phase
    
    def backward(self, error):
        """ Backward pass through the layer: Return the gradient with respect to the input.
            param: error (np.ndarray): error passed down from the subsequent layer, of the same shape as the 
                   output of the forward pass
            returns (np.ndarray):  gradient with respect to the input, of the same shape as error
        """
        # TODO: Implement backward pass of the Dropout layer (case: inverted dropout!)
        pass