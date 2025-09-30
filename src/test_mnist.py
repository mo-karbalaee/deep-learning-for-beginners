# Perform the prediction for a random test sample from the dataset:
x, l = net.data_layer.get_random_test_sample()

# plotting
fig = plt.figure(figsize=(5, 5))
plt.imshow(x[:28*28].reshape(28, 28), cmap='gray')
plt.title('Input image')
plt.axis('off')
plt.show()

# network prediction
print('Prediction with highest output: {}'.format(np.argmax(net.test(x))))
print('Ground truth: {}'.format(np.argmax(l)))