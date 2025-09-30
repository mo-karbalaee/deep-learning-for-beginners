#----------------------------------
# Exercise: Pooling
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/pooling_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/pooling.py
# This will save the result to a python file, which you will need for the next exercises.


from src.base import BaseLayer, Phase
from src.layers.conv import FlattenLayer, ConvolutionalLayer #your results of previous exercises
from src.layers.fully_connected import FullyConnectedLayer #your result of previous exercises

class MaxPoolLayer(BaseLayer):
    
    def __init__(self, neighborhood=(2, 2), stride=(2, 2)):
        """ Max pooling layer.
           param: neighborhood: tuple with shape (sp, sq) which denote the kernel size of the pooling operation in 
           the spatial dimensions
           param: stride: tuple with shape (np, nq) which denote the subsampling factor of the pooling operation in
           the spacial dimensions
        """
        # TODO: define necessary class variables, for this, have a look at the input and at the forward and backward 
        # function.
        pass
    
    def forward(self, x):
        """ Return the result of maxpooling on the input.
            param: x (np.ndarray) with shape (b, n_channels, p, q) where b is the batch size, 
                   n_channels is the number of input channels and p x q is the image size
            returns (np.ndarray): the result of max pooling, of shape (b, n_channels, p', q')
                   where b is the batch size, n_channels is the number of input channels and 
                   p' x q' is the new image size reduced by the stride. 
        """
        # TODO: Implement forward pass of max pooling, think of what you need to store for the backward pass
        # (1) store the input tensor shape: TODO
        
        # (2) calculate the output shape: 
        # for this, loop through the image size (p,q), the neighborhood (sp, sq), and the stride (np, nq) and compute 
        # the output of the pooling operation according to:
        # (W-F + 2P)/S + 1,
        # where in our case padding P is 0, W means image size, and F means neighborhood size
        # TODO
        
        # (3) The complete output shape then is [batch_size, n_channel and the result of (2)]
        # TODO
        
        # (4) initialize the max pooling result array using the output size:
        result = #TODO
        
        # (4) Create an empty dictionary to store the values for the switch operation used in the backward pass
        self.switches = # TODO
        
        # (5) Now, compute the forward pass of max pooling: Loop over the output shape
        for this_batch in #...
            for this_channel in #...
                for y_out in #...
                    for x_out in #...
                        x_in = #TODO
                        input_part = #TODO: get values of x according to current indices and neighborhood size
                        max_idx = #TODO: get max index of input part, hint: have a look at np.unravel_index
                        #define a shape tuple to access the switch variable
                        shape = #TODO
                        self.switches[shape] = #TODO
                        #assign values to result
                        result[shape] = #TODO
        #return the result of max pooling                
        pass 
    
    def backward(self, error):
        """ Return the gradient with respect to the previous layer.
            param: error(np.ndarray): the gradient passed own from the subsequent layer, 
                   of shape [b, n_channels, p', q'] where b is the batch size, n_channels is the 
                   number of channels and p' x q' is the image size reduced by the stride
            returns (np.ndarray): the gradient w.r.t. the previous layer, of shape [b, n_channels, p, q] 
                   where b is the batch size, n_channels is the number of input channels to this layer and 
                   p x q is the image size prior to downsampling.
        """
        # TODO: Implement backward pass of max pooling
        
        # (1) initialize a variable to compute the gradient
        # TODO
        
        # (2) Iterate over the switch dictionary: TODO
        # Hint: subgradients: the winner takes it all, see description
        
        #return the gradient w.r.t. the previous layer
        pass 