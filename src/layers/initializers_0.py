#----------------------------------
# Exercise: Initializers
#----------------------------------
# The original python file can be reloaded by typing %load src/layers/initializers_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/layers/initializers.py
# This will save the result to a python file, which you will need for the next exercises.


from src.base import BaseLayer, Phase

class Initializer:
    """ Base class for initializers. """
    def initialize(self, weight_shape):
        """ Return weights initialized according to the subclass definition. 
            Required to work for arbitrary weight shapes.
            Base class. 
        """
        
        # Raises an exeption in base class.
        raise NotImplementedError('Method is not implemented')

        
class Const(Initializer):
    
    def __init__(self, value):
        """ Create a constant initializer.
            params: value (float): constant that is used for initialization of weights
        """
        # TODO: Implement
        pass

    def initialize(self, weight_shape):
        """ Return a new array of weights initialized with a constant value provided by self.value.
            param: weight_shape: shape of the new array
            returns (np.ndarray): array of the given shape
        """
        # TODO: Implement
        pass

class UniformRandom(Initializer):
    
    def initialize(self, weight_shape):
        """ Return a new array of weights initialized by drawing from a uniform distribution with range [0, 1].
            param: weight_shape: shape of new array
            returns (np.ndarray): array of the given shape
        """
        # TODO: Implement
        pass

        
class He(Initializer):
       
    def initialize(self, weight_shape):
        """ Return a new array of weights initialized according to He et al.: Delving Deep into Rectifiers.
            param: weight_shape: shape of the np.array to be returned, the second dimension is assumed to be the 
                   number of input nodes
            returns (np.ndarray): array of the given shape
        """        
        # TODO: Implement based on the equation in the description, hint: check the size of the weight array
        pass