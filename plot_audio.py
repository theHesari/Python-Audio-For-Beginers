from signal import signal
import wave
import numpy as np
import matplotlib.pyplot as plt 

#open wave file and set get its params
obj = wave.open("file_example_WAV_1MG.wav", "rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
audio_duration = n_samples/sample_freq
print(audio_duration)
obj.close()

#convert the buffer to an array and seprate its channels in a 2D array (audio is an stereo file)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
signal_array.shape = -1,2
signal_array = signal_array.T 
time = np.linspace(0, audio_duration, num=n_samples)

#check if the len of time and each channels len is equal
print(signal_array[:10])
print(time[:10])
print(len(signal_array[0]), len(signal_array[1]), len(time))

#plot it!
plt.figure(1)
plt.plot(time , signal_array[0])
plt.title("Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal")
plt.xlim(0, audio_duration)
plt.show()
plt.figure(1)
plt.plot(time , signal_array[1])
plt.title("Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal")
plt.xlim(0, audio_duration)
plt.show()