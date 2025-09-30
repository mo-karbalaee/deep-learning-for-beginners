import unittest
import numpy as np
import os


class TestSmoothingFilter(unittest.TestCase):

    def setUp(self):
        self.noisy = np.load(os.path.abspath('Tests/Data/img_noisy.npy'))
        self.box = np.load(os.path.abspath('Tests/Data/img_box.npy'))
        self.gaussian = np.load(os.path.abspath('Tests/Data/img_gaussian.npy'))
        
    def test_box_filter(self):
        myfilter = self.SmoothingFilter()
        predicted_box = myfilter.box_filter(self.noisy)
        diff = predicted_box - self.box        
        self.assertEqual(diff.sum(), 0)        
        
    def test_gaussian_filter(self):
        myfilter = self.SmoothingFilter()
        predicted_gaussian = myfilter.gaussian_filter(self.noisy)
        diff = predicted_gaussian - self.gaussian
        self.assertEqual(diff.sum(), 0)

        
if __name__ == "__main__":
    pass