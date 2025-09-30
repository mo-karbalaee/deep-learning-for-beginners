#----------------------------------
# Exercise: fast Fourier transform Step 2
#----------------------------------
# The original python file can be reloaded by typing %load src/filtering/fft_step2_0.py in the first line of this cell.
# After successfully solving this exercise, type the following command in the first line of this cell:
# %%writefile src/filtering/fft_step2.py
# This will save the result to a python file, which you will need for the next exercises.

#Step 2:
#add noise to the signal
tone_noisy = tone_mix + np.random.randn(len(x))

#save sounds to disk
norm_tone_mix = np.int16((tone_mix / tone_mix.max()) * 32767)
norm_tone_noisy = np.int16((tone_noisy / tone_noisy.max()) * 32767)
write("orig.wav", sampling_rate, norm_tone_mix)
write("noisy.wav", sampling_rate, norm_tone_noisy)

# compute the FFT of the noisy signal
yf = # TODO: compute the FFT of tone_noisy

# Number of samples in normalized_tone
N = sampling_rate * t
xf = rfftfreq(N, 1 / sampling_rate)

#plotting
fig = plt.figure(figsize=(15, 7))
fig.add_subplot(2,1,1)
plt.plot(tone_noisy[:s])
plt.title("Noisy")
fig.add_subplot(2,1,2)
plt.plot(xf[:s], np.abs(yf)[:s])
plt.title("FFT noisy")
plt.show()