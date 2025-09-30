#----------------------------------
# Exercise: fast Fourier transform Step 1
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/fft_step1_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/fft_step1.py
# This will save the result to a python file, which you will need for the next exercises.

#Step 1:
# Compute the fast Fourier transform (FFT) of the mixed signal, hint: Use the rfft 
yf = # TODO: Compute here the rFFT

# sample frequencies of FFT
N = sampling_rate * t
xf = rfftfreq(N, 1 / sampling_rate)

#Compute the inverse fast Fourier transform (IFFT)
reco_tone = # TODO: Compute here the IFFT

#plotting
fig = plt.figure(figsize=(15, 10))
fig.add_subplot(3,1,1)
plt.plot(tone_mix[:s])
plt.title("Orig tone mixed")
fig.add_subplot(3,1,2)
plt.plot(xf[:s],np.abs(yf)[:s])
plt.title("FFT of tone mixed")
fig.add_subplot(3,1,3)
plt.plot(reco_tone[:s])
plt.title("Reconstructed tone mixed")
plt.show()