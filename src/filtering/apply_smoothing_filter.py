#read image
img = plt.imread('Set5/bird_GT.bmp')
#img = plt.imread('Set5/butterfly_GT.bmp')
#img = plt.imread('Set5/woman_GT.bmp')
#img = plt.imread('Set5/baby_GT.bmp')
#img = plt.imread('Set5/head_GT.bmp')

#normalize and convert to grayscale
gray = norm_gray(img)
#add noise
noisy = generate_noisy_image(gray)

#apply filters to noisy image
smoothFilter = SmoothingFilter()
mean = smoothFilter.box_filter(noisy)
blurred = smoothFilter.gaussian_filter(noisy)

#plotting
fig = plt.figure(figsize=(15, 15))
fig.add_subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title('Gray')
plt.axis('off')
fig.add_subplot(2,2,2)
plt.imshow(noisy, cmap='gray')
plt.title('Noisy')
plt.axis('off')
fig.add_subplot(2,2,3)
plt.imshow(mean, cmap='gray')
plt.title('Mean')
plt.axis('off')
fig.add_subplot(2,2,4)
plt.imshow(blurred, cmap='gray')
plt.title('Gaussian')
plt.axis('off')
plt.show()