import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.fftpack import fft
Fs, data = read('../Cello Notes/wave/843.wav')


print('Sample Rate:', Fs)

T = 1.0/Fs

print('Sample Period', T)

L = len(data.T[0])
print('Signal Length:', L)

t = np.linspace(0, L, L)*T
print('Time Vector Length:', len(t))
y1 = data.T[0]
print(len(y1))
plt.subplot(221)
plt.plot(t, y1)

Y1 = fft(y1)

P2 = abs(Y1/L)
P1 = P2[1:L/2]

f = Fs*np.linspace(0, L/2, L/2-1)/L
print('f length', len(f))
print('P1 length', len(P1))
plt.subplot(212)
plt.plot(f, P1)

plt.show()
