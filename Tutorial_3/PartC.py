import scipy.io
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import butter, lfilter
plt.close('all')
samplerate, data = wavfile.read("Cafe_with_noise.wav")
length = data.shape[0] / samplerate
time = np.linspace(0., length, data.shape[0])

# Plot the Signal
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

#Plot the frequency domain
fft_spectrum = np.fft.rfft(data)
freq = np.fft.rfftfreq(data.size, d=1./samplerate)
fft_spectrum_abs = np.abs(fft_spectrum)


plt.plot(freq, fft_spectrum_abs)
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.show()


#Low Pass Filter
#Credit for Filter: Gershom
def butter_lowpass(cutoff_freq, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def apply_lowpass_filter(data, cutoff_freq, fs, order=5):
    b, a = butter_lowpass(cutoff_freq, fs, order=order)
    filtered_data = lfilter(b, a, data)
    return filtered_data


newdata = apply_lowpass_filter(data, 15000, 48000)

wavfile.write("quietCafe.wav", samplerate, newdata)
#for some reason this keeps generating files incompatible with my computer, so here's to hoping it actually works








