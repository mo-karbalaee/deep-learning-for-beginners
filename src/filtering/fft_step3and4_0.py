#----------------------------------
# Exercise: fast Fourier transform Step 3 and 4
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/fft_step3and4_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/fft_step3and4.py
# This will save the result to a python file, which you will need for the next exercises.

#Step 3:
#filtering the noisy signal in the fourier domain: 
#Hint: compute a threshold based on the magnitude of the fourier representation (absolute value) that only restores the two peaks
yf_clean = #TODO: filter the noisy signal

#Step 4:
#compute the inverse fast Fourier transform
filtered_tone = #TODO: compute the IFFT of yf_clean

#store filtered tone to disk
norm_filtered_tone = np.int16(filtered_tone * (32767 / filtered_tone.max()))
write("clean.wav", sampling_rate, norm_filtered_tone)

#plotting
fig = plt.figure(figsize=(15, 10))
fig.add_subplot(3,1,1)
plt.plot(xf[:s], np.abs(yf_clean)[:s])
plt.title("FFT filtered")
fig.add_subplot(3,1,2)
plt.plot(filtered_tone[:s])
plt.title("Reconstructed filtered tone mixed")
fig.add_subplot(3,1,3)
plt.plot(tone_mix[:s])
plt.title("Original tone mixed")
plt.show()