def generate_tone(freq, sampling_rate, time):
    x = np.linspace(0, time, sampling_rate * time, endpoint=False)
    y = np.sin((2 * np.pi) * x * freq)
    return x, y

#set parameters for signals
sampling_rate = 44100 # hertz
t = 2  # seconds
s = 1000 #for plotting only a subset

#generate sine wave tones
x, tone_A = generate_tone(440, sampling_rate, t)
x, tone_C = generate_tone(262, sampling_rate, t)

#addition of both signals
tone_mix = tone_A  + tone_C

#plotting
fig = plt.figure(figsize=(15, 10))
fig.add_subplot(3,1,1)
plt.plot(tone_A[:s])
plt.title("Orig tone A")
fig.add_subplot(3,1,2)
plt.plot(tone_C[:s])
plt.title("Orig tone C")
fig.add_subplot(3,1,3)
plt.plot(tone_mix[:s])
plt.title("Orig tone mixed")
plt.show()