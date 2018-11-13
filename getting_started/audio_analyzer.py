import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt


CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()
x = np.arange(0, 2*CHUNK, 2)
line,= ax.plot(x,np.random.rand(CHUNK))
plt.show(block=False)
ax.set_ylim(-CHUNK,CHUNK )
ax.set_xlim(0, CHUNK)
while True:
    
    data = stream.read(CHUNK)
    data_int16 = struct.unpack(str(CHUNK)+'h', data)
    line.set_ydata(data_int16)
    fig.canvas.draw()
    fig.canvas.flush_events()

    
