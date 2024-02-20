import scipy.io
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')
samplerate, data = wavfile.read("human_voice.wav")
print(samplerate)
#og sample frequency is 48000
length = data.shape[0] / samplerate
time = np.linspace(0., length, data.shape[0])

plt.subplot(2,1,1)
plt.plot(time, data, 'r')
plt.xlabel("time, s [left channel]")
plt.ylabel("signal, relative units")
plt.subplot(2,1,2)
plt.plot(time, data, 'b')
plt.xlabel("time, s [right channel]")
plt.ylabel("signal, relative units")
plt.tight_layout()
plt.show()


newSample= 8000
downFactor= samplerate//newSample
downAudio=data[::downFactor]
wavfile.write("downsampled_audio.wav",newSample, downAudio)
samplerateD, dataD = wavfile.read("downsampled_audio.wav")
print(samplerateD)

lengthD = dataD.shape[0] / samplerateD
timeD = np.linspace(0., lengthD, dataD.shape[0])

plt.subplot(2,1,1)
plt.plot(time, dataD, 'r')
plt.xlabel("time, s [left channel]")
plt.ylabel("downsampled signal, relative units")
plt.subplot(2,1,2)
plt.plot(time, dataD, 'b')
plt.xlabel("time, s [right channel]")
plt.ylabel("downsampled signal, relative units")
plt.tight_layout()
plt.show()
