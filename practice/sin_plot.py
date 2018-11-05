import numpy as np
import matplotlib.pyplot as plt

Fs = 8000
f = 5
sample = 8000
Ts =1.0/Fs
x = np.arange(0,1,Ts)

y = np.sin(2*np.pi*f*x) + np.cos(2*np.pi*1/5*f*x)

n=len(y)
k = np.arange(n)


T = n/Fs

frq = k/T

frq = frq[range(n/2)]

Y = np.fft.fft(y)/n 
Y = Y[range(n/2)]

print('frq length', len(frq))
print('len abs(Y)', abs(Y))

plt.subplot(221)
plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(frq, abs(Y), 'r')
plt.xlabel('Freq (Hz)')
plt.xlim(-10, 10)
plt.ylabel('|Y(freq)|')
plt.show()
