#----------------------------------
# Exercise: Edge Detection
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/edge_detection_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/edge_detection.py
# This will save the result to a python file, which you will need for the next exercises.

class EdgeDetection():
    
    #compute gradient in x and y direction
    def gradient_filter(self,img):
        k_x = #TODO: define the 1-D kernel in x-direction of the gradient
        k_y = #TODO: define the 1-D kernel in y-direction of the gradient
        gradient_x = #TODO: convolve the image with the k_x
        gradient_y = #TODO: convolve the image with the k_y
        return gradient_x, gradient_y
    
    #define sobel filter in x and y direction
    def sobel_filter(self,img):
        sx = #TODO: define the sobel filter kernel in x-direction
        sy = #TODO: define the sobel filter kernel in y-direction     
        sobel_x = #TODO: convolve the image with the s_x
        sobel_y = #TODO: convolve the image with the s_y
        return sobel_x, sobel_y
    
    #compute magnitude of filtered image of both directions
    def compute_magnitude(self,x,y):
        magnitude = #compute the magnitude of x and y
        return magnitude