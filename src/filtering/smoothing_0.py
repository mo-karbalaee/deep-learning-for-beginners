#----------------------------------
# Exercise: Smoothing filter
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/smoothing_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/smoothing.py
# This will save the result to a python file, which you will need for the next exercises.

class SmoothingFilter():

    #define box filter, also called mean filter
    def box_filter(self, img):              
        m = #TODO: define the 2-D filter kernel of the mean filter        
        mean = #TODO: convolve image with kernel
        return mean

    #define gaussian smoothing filter
    def gaussian_filter(self, img):        
        b = #TODO: define the 2-D kernel of the gaussian smoothing filter 
        blurred = #TODO: convolve image with kernel
        return blurred