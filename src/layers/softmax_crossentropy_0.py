#----------------------------------
# Exercise: Softmax cross entropy
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/softmax_crossentropy_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/softmax_crossentropy.py
# This will save the result to a python file, which you will need for the next exercises.

from src.base import BaseLayer, Phase

class SoftMaxCrossEntropyLoss(BaseLayer):
    def __init__(self):
        #TODO: define class variable(s)
        pass
    
    def forward(self, x, labels):
        """ Return the cross entropy loss of the input and the labels after applying the softmax to the input. 
            param: x (np.ndarray): input, of shape [b, k] where b is the batch size and k is the input size
            param: labels (np.ndarray): the corresponding labels of the training set in one-hot encoding for 
                   the current input, of the same shape as x
            returns (float): the loss of the current prediction and the label
        """
        # TODO: Implement forward pass
        prediction = #TODO: use self.predict here to apply softmax to the network output
        #Then, compute the cross entropy loss (see equation in description)
        #Hint: for the implementation, you can simplify the equation by getting the indices for the labels beeing 1
        pass
    
    def backward(self, labels):
        """ Return the gradient of the SoftMaxCrossEntropy loss with respect to the previous layer.
            param: labels (np.ndarray): (again) the corresponding labels of the training set for the current input, 
                   of shape [b, k] where b is the batch size and k is the input size
            returns (np.ndarray): the error w.r.t. the previous layer, of shape [b, k] where b is the batch 
                   size and n is the input size
        """
        # TODO: Implement backward pass: compute the gradient of the SoftMax loss (see equation in description)
        # For this, do not use self.prediction directly, but a copy of it
        # Here, also you can find the positive class via the indices for the labels beeing 1
        pass
    
    def predict(self, x):
        """ Return the softmax of the input.  This can be interpreted as probabilistic prediction of the class.
            param: x (np.ndarray): input with shape [b, k], where b is the batch size and n is the input size
            returns (np.ndarray): the result softmax(x), of the same shape as x
        """
        # TODO: Implement softmax (see equation in description)
        # Hint: beforehand, shift the activation by the max value.
        # return and store the prediction as class variable (the latter you need for the backward function)
        pass