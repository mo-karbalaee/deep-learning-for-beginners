#some base functions - you do not have to change anything here
def norm_gray(img):
    gray = 0.30*img[:,:,0] + 0.59*img[:,:,1] + 0.11*img[:,:,2]
    gray = gray/255 #convert to [0,1]
    return gray

def generate_noisy_image(gray):
    noise = np.random.normal(0,.1,gray.shape[0]*gray.shape[1]).reshape(gray.shape[0],gray.shape[1])
    #zero center
    m = gray.mean()
    s = gray.std()
    gray = (gray-m)/s
    #add noise to zero centered img
    noisy = gray + noise
    #convert back
    gray = (gray*s)+m    
    return noisy