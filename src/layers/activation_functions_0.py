#----------------------------------
# Exercise: Activation functions
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/activation_functions_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/activation_functions.py
# This will save the result to a python file, which you will need for the next exercises.


from src.base import BaseLayer, Phase

class Sigmoid(BaseLayer):
    def __init__(self):
        super().__init__()
        # TODO: Define class variable(s)
        pass
    
    def forward(self, x):
        """ Return the element-wise sigmoid of the input.
            param: x (np.ndarray): input to the activation function, of arbitrary shape
            returns (np.ndarray): element-wise sigmoid(x), of the same shape as x
        """
        # TODO: Implement forward pass of the Sigmoid, also store it as class variable
        pass
        
    def backward(self, error):
        """ Return the gradient with respect to the input.
            param: error (np.ndarray): the gradient passed down from the subsequent layer, of the same 
                   shape as x in the forward pass
            returns (np.ndarray): the gradient with respect to the previous layer, of the same shape as error 
        """
        # TODO: Implement backward pass of the Sigmoid, reuse stored variable
        pass
    

class ReLU(BaseLayer):
    def __init__(self):
        super().__init__()
        # TODO: Define class variable(s)
        pass
    
    def forward(self, x):
        """ Return the result of a ReLU activation of the input.
            param: x (np.ndarray): input to the activation function, of arbitrary shape
            returns (np.ndarray): element-wise ReLU(x), of the same shape as x
        """
        # TODO: Implement forward pass of the ReLU, store the activation to reuse it in the backward pass
        pass
    
    def backward(self, error):
        """ Return the gradient with respect to the input.
            param: error (np.ndarray): the gradient passed down from the previous layer, arbitrary shape (same as x)
            returns (np.ndarray): gradient with respect to the input, of the same shape as error 
        """
        # TODO: Implement backward pass of the ReLU, reuse stored variable
        pass