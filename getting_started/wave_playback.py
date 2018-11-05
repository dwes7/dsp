import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import read

Fs, data = read('../Cello Notes/wave/843.wav')
# calculate note frequencies

sample_rate = Fs
T = 1/Fs
t = np.linspace(0, T, T * sample_rate, False)

# generate sine wave notes

# convert to 16-bit data
data = data.astype(np.int16)

# start playback
play_obj = sa.play_buffer(data, 2, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()
