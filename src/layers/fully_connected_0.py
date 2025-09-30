#----------------------------------
# Exercise: Fully connected layers
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/fully_connected_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/fully_connected.py
# This will save the result to a python file, which you will need for the next exercises.

from src.base import BaseLayer, Phase

class FullyConnectedLayer(BaseLayer):
    def __init__(self, input_size, output_size, learning_rate):
        """ A fully connected layer.
            param: input_size (int): dimension n of the input vector
            param: output_size (int): dimension m of the output vector
            param: learning_rate (float): the learning rate of this layer
        """
        # TODO: define the necessary class variables, for this have a look at the input variables and the other functions
        pass

    def forward(self, x):
        """ Compute the foward pass through the layer.
            param: x (np.ndarray): input with shape [b, n] where b is the batch size and n is the input size
            returns (np.ndarray): result of the forward pass, of shape [b, m] where b is the batch size and
                   m is the output size
        """
        # TODO: Implement forward pass of the fully connected layer
        
        # (1) Think about what you need to store during the forward pass to be able to compute the gradients in the backward pass 
        self.X = #TODO
        
        # (2) perform the actual forward pass just by matrix multiplication
        # TODO
        
        # return the result        
        pass
    
    def get_gradient_weights(self):
        """ 
        returns (np.ndarray): the gradient with respect to the weights and biases from the last call of backward(...)
        """
        # TODO: Implement the getter method, hint: store the gradient in the backward pass as a class variable, 
        # then you can easily access it here.
        pass
    
    def backward(self, error):
        """ Update the weights of this layer and return the gradient with respect to the previous layer.
            param: error (np.ndarray): of shape [b, m] where b is the batch size and m is the output size
            returns (np.ndarray): the gradient w.r.t. the previous layer, of shape [b, n] where b is the 
                   batch size and n is the input size
        """
        # TODO: Implement backward pass of the fully connected layer
        # Hint: Be careful about the order of applying the update to the weights and the calculation of 
        # the error with respect to the previous layer.
        
        # (1) calculate the error for lower layers using the transposed weights and the error
        # TODO
        
        # (2) update own parameters
        # TODO
        
        # (3) store gradient for testing purposes
        # TODO
        
        # (4) update weights using learning rate and gradient
        # TODO
        
        # (5) delete the bias row which has no meaning
        
        # TODO: return gradient w.r.t. the previous layer
        pass
    
    def initialize(self, weights_initializer, bias_initializer):
        """ Initializes the weights/bias of this layer with the given initializers.
            param: weights_initializer: object providing a method weights_initializer.initialize(weights_shape)
                   which will return initialized weights with the given shape
            param: bias_initializer: object providing a method bias_initializer.initialize(bias_shape) 
                   which will return an initialized bias with the given shape
        """
        # TODO: Implement the initialization using the given initializers. Hint: Stack the weights and bias together 
        # in the weights array.
        pass