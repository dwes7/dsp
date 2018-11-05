import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read


wav = read('../Cello Notes/wave/594.wav')

wav_array = np.array(wav[1], dtype=float)
n = len(wav_array)


print('signal length', n)

t = np.linspace(0, n, n)

print('time array length', len(t))

plt.plot(t, wav_array)

plt.show()
