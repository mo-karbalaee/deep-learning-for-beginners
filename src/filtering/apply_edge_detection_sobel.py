#read image
img = plt.imread('Set5/bird_GT.bmp')
#img = plt.imread('Set5/butterfly_GT.bmp')
#img = plt.imread('Set5/woman_GT.bmp')
#img = plt.imread('Set5/baby_GT.bmp')
#img = plt.imread('Set5/head_GT.bmp')

gray = norm_gray(img)

#sobel
edgeDet = EdgeDetection()
sobel_x, sobel_y = edgeDet.sobel_filter(gray)
sobel_mag = edgeDet.compute_magnitude(sobel_x, sobel_y)

#plotting
fig = plt.figure(figsize=(15, 15))
fig.add_subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title('Gray')
plt.axis('off')
fig.add_subplot(2,2,2)
plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel x')
plt.axis('off')
fig.add_subplot(2,2,3)
plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel y')
plt.axis('off')
fig.add_subplot(2,2,4)
plt.imshow(sobel_mag, cmap='gray')
plt.title('Sobel magnitude')
plt.axis('off')
plt.show()