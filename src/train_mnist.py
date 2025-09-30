import matplotlib
import numpy as np
import matplotlib.pyplot as plt

net = build()

from Tests import Helpers
# TODO: you can change the parameters, depending on the batch size and how many iterations you choose, the training 
# script can run for a few minutes or longer.

# parameters
batch_size = 20 #set here the batch size
net.data_layer = Helpers.MNISTData(batch_size)
n_iters = 100 #set here the number of iterations

# training
net.train(n_iters)

# plotting
plt.plot(range(n_iters), net.loss)
plt.xlabel('iterations')
plt.ylabel('softmax loss')
plt.show()
