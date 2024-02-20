import scipy.io
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math
plt.close('all')
samplerate1, data1 = wavfile.read("M1.wav")
samplerate2, data2 = wavfile.read("M2.wav")
samplerate3, data3 = wavfile.read("M3.wav")

data1_float = data1/np.iinfo(data1.dtype).max
data2_float= data2/np.iinfo(data2.dtype).max
data3_float= data3/np.iinfo(data3.dtype).max

print("RMS value of M1: ", np.sqrt(np.mean(data1_float**2)))
print("RMS value of M2: ", np.sqrt(np.mean(data2_float**2)))
print("RMS value of M3: ", np.sqrt(np.mean(data3_float**2)))

# Problem 2

# Microphone M1 is closer to the sound source, since the RMS value of M1 is greater than
# the RMS value of M2.

# Problem 3

# CREDIT FOR CODE: GERSHOM

def cross_correlation(signal1, signal2):
    lag_array = np.zeros(signal2.shape[0]-1)
    signal2_array = np.concatenate((lag_array,signal2,lag_array)) 
    signal2_matrix = np.zeros((signal2.shape[0],2*signal2.shape[0]-1))

    for i in range(2*signal2.shape[0]-1):
        signal2_matrix[:, i]= signal2_array[i:i+m2_audio.shape[0]]

    signal1.reshape((1,signal1.shape[0]))
    correlation = np.matmul(signal1, signal2_matrix)
    return correlation 

m1_sampling_rate, m1_audio = wavfile.read("M1.wav")
m2_sampling_rate, m2_audio = wavfile.read("M2.wav")

correlation = cross_correlation(m1_audio, m2_audio)

plt.figure(figsize=(10, 4))
plt.title("Correlation")
plt.xlabel("Time (s)")
plt.ylabel("Correlation")
plt.plot(np.abs(correlation))
plt.grid()


sample_delay = np.argmax(np.abs(correlation))

time_delay  = (sample_delay-m1_audio.shape[0])  /m2_sampling_rate

print("Time delay: " + str(time_delay))

plt.show()