import unittest
import numpy as np
import os


class TestEdgeDetection(unittest.TestCase):

    def setUp(self):
        self.img = np.load('Tests/Data/img_gray.npy')
        self.gradient_x = np.load('Tests/Data/img_gradient_x.npy')
        self.gradient_y = np.load('Tests/Data/img_gradient_y.npy')
        self.gradient_mag = np.load('Tests/Data/img_gradient_mag.npy')
        self.sobel_x = np.load('Tests/Data/img_sobel_x.npy')
        self.sobel_y = np.load('Tests/Data/img_sobel_y.npy')
        self.sobel_mag = np.load('Tests/Data/img_sobel_mag.npy')
        
    def test_gradient_edges(self):
        edgeDet = self.EdgeDetection()
        pred_gradient_x, pred_gradient_y = edgeDet.gradient_filter(self.img)
        diffx = pred_gradient_x - self.gradient_x
        diffy = pred_gradient_y - self.gradient_y          
        self.assertEqual(diffx.sum(), 0)
        self.assertEqual(diffy.sum(), 0)
        self.assertEqual(pred_gradient_x.shape, pred_gradient_y.shape)
        pred_mag = edgeDet.compute_magnitude(pred_gradient_x, pred_gradient_y)
        diffM = pred_mag - self.gradient_mag
        self.assertEqual(diffM.sum(), 0)

    def test_sobel_edges(self):
        edgeDet = self.EdgeDetection()
        pred_sobel_x, pred_sobel_y = edgeDet.sobel_filter(self.img)
        diffx = pred_sobel_x - self.sobel_x
        diffy = pred_sobel_y - self.sobel_y
        self.assertEqual(diffx.sum(), 0)
        self.assertEqual(diffy.sum(), 0)
        self.assertEqual(pred_sobel_x.shape, pred_sobel_y.shape)
        pred_mag = edgeDet.compute_magnitude(pred_sobel_x, pred_sobel_y)
        diffM = pred_mag - self.sobel_mag
        self.assertEqual(diffM.sum(), 0)
        
if __name__ == "__main__":
    pass