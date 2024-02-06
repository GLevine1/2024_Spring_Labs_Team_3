import numpy as np
from scipy import linalg
from scipy.optimize import minimize
from numpy import pi

# Question 1
A = np.array([[3, 1], [1, 2]])
print(A)
print()
b = np.array([[9], [8]])
print(b)
print()
c = np.linalg.solve(A, b) 
print(c)

# Question 2
def y(x):
    return x**2 + 2*x

result = minimize (y,0)
min_x=result.x[0]
print("Minimum value:", result.fun)

# Question 3
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

x = np.linspace(0,1, 1000)

y = np.sin(100*np.pi*x) + 0.5*np.sin(160*np.pi*x)

fft_y=fft(y)

freq= fftfreq(len(x), d=x[1]-x[0])

plt.figure(figsize=(10,6))
plt.plot(freq, np.abs(fft_y))

plt.title('Frequency Response')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0,200)
plt.show()