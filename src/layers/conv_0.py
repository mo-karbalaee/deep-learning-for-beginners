#----------------------------------
# Exercise: Convolutional layers
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/conv_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/conv.py
# This will save the result to a python file, which you will need for the next exercises.


from src.base import BaseLayer, Phase
from scipy.signal import convolve, correlate #use these functions for convolution and correlation
from src.layers.fully_connected import FullyConnectedLayer #your result of the previous exercise

class FlattenLayer(BaseLayer):
    def __init__(self):
        # TODO: define the necessary class variables
        pass
    
    def forward(self, x):
        """ Return a flattened version of the input.
            param: x (np.ndarray): input, of shape [b, n_channels, p, q] where b is the batch size, 
                   n_channels is the number of channels and p x q is the image size
            returns (np.ndarray): a flattened representation of x of shape [b, v] 
                   where b is the batch size and v is the output size = n_channels * p * q
        """
        # TODO: Implement flattening of the image
        pass
    
    def backward(self, error):
        """ Return the gradient with respect to the input.
            param: error (np.ndarray): the gradient passed down from the subsequent layer, of shape [b, m],
                   where b is the batch size and m is the output size with m = n_channels * p * q from 
                   the forward pass
            returns (np.ndarray): the error with restored dimensions from the forward pass, i.e. with 
                   shape [b, n_channels, p, q] where b is the batch size, n_channels is the number of 
                   channels and p x q is the image size
        """
        # TODO: Restore the image dimensions
        pass


class ConvolutionalLayer(BaseLayer):
    
    def __init__(self, stride, kernel_shape, n_kernels, learning_rate):
        """ 
            param: stride: tuple in the form of (np, nq) which denote the subsampling factor of the 
                   convolution operation in the spatial dimensions
            param: kernel_shape: integer tuple in the form of (n_channels, m, n) where n_channels is 
                   the number of input channels and m x n is the size of the filter kernels
            param: n_kernels (int): number of kernels and therefore the number of output channels
            param: learning_rate (float): learning rate of this layer
        """
        # TODO: define the necessary class variables, hint: have a look at the input variables and consider what else 
        # you need similiar to the FC layer.
        pass 
    
    def forward(self, x):
        """ Return the result of the forward pass of the convolutional layer.
            param: x(np.ndarray): input, of shape [b, n_channels, p, q],  where b is the batch size, 
                   n_channels is the number of input channels and p x q is the image size
            returns (np.ndarray): result of the forward pass, of shape (b, n_kernels, p', q') 
                   where b is the batch size, n_kernels is the number of kernels in this layer and 
                   p' x q' is the output image size (which depends on the stride)
        """
        # TODO: Implement forward pass of the convolutional layer:        
        # (1) store the input for reuse in the backward pass
        self.X = #TODO
        
        # (2) define output tensor: 
        output_tensor = #TODO
        
        # (3) Loop over all kernels and apply cross-correlation:
        for k in #...
            kernel = #TODO: expand dims of weights
            d = #TODO: use the correlation function
            d = #subsample d, consider the stride here
            #TODO: add bias
            #TODO: store in output_tensor list
        #TODO: return output_tensor as np.ndarray (see function description)        
    
    def backward(self, error):
        """ Update the weights of this layer and return the gradient with respect to the input.
            param: error (np.ndarray): of shape (b, n_kernels, p', q') where b is the batch size, n_kernels
                   is the number of kernels and p' x q' is the spacial error size (depends on the stride)
            returns (np.ndarray): the gradient with respect to the input, of shape (b, n_channels, p, q) 
                   where b is the batch size, n_channels is the number of input channels to this layer and 
                   p x q is the image size.
        """ 
        # TODO: Implement backward pass of the convolutional layer:
        # (1) Perform upsampling of error
        err_resampled = #TODO: create empty array of size (b, n_kernels, p, q)
        #TODO: assign the values of the error variable to err_resampled by considering the stride
        #TODO: err_resampled is a placeholder, now reassign the values of err_resampled to error
        
        # (2) Gradient with respect to the bias
        self._gradient_bias = #TODO
        
        # (3) Gradient with respect to lower layers (hint: w.r.t. input)
        dx = #define variable 
        #TODO: loop over input channels and output channels (hint: kernels)
        for #...
            k = #define empty kernel list
            for #...
                #get weights at index
            k = #bring k to the right dims
            #use the convolution function here and store the result in dx
        
        # (4) Gradient with respect to the weights
        #TODO: define the pad sizes: kyhl, kyhr, kxhl, kxhr
        gradient_weights = #define, use it in the loop to store the results
        x_padded = #pad self.X using kyhl, kyhr, kxhl, kxhr with constant values
        #loop over kernels and input
        for #...
            dwh = #define
                for #...
                    #use the correlation function here and store the result in dwh
                
        #TODO: store the gradients_weights as class variable
        
        # (5) update weights and bias using the learning rate and computed results, store as class variables
        #TODO
        
        #TODO: return the gradient with respect to the input as np.ndarray (see function description)
        
    
    def get_gradient_weights(self):
        """ Returns the gradient with respect to the weights from the last call of backward() """
        # TODO: Implement the getter method, hint: class variable
        pass

    def get_gradient_bias(self):
        """ Returns the gradient with respect to the bias from the last call of backward() """
        # TODO: Implement the getter method, hint: class variable
        pass
    
    def initialize(self, weights_initializer, bias_initializer):
        """ Initializes the weights/bias of this layer with the given initializers.
            param: weights_initializer: object providing a method weights_initializer.initialize(weights_shape)
                   which will return initialized weights with the given shape
            param: bias_initializer: object providing a method bias_initializer.initialize(bias_shape) 
                   which will return an initialized bias with the given shape
        """
        # TODO: Implement. To make sure that He initialization works as intended, make sure the second dimension 
        # of weights_shape contains the number of input nodes that can be computed as n_in = n_channels * m * n
        # and reshape the weights to the correct shape afterwards.
        pass