import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(-2*np.pi, 2*np.pi, 30)
y = np.array([0,0,1,0,0,0,2,-1,0,0,0,0,-1,0])
y.shape
x = np.linspace(-5, 9, 14)
x.shape
#markerline, stemlines, baseline = plt.stem(x, np.cos(x))
markerline, stemlines, baseline = plt.stem(x, y)

plt.show()
plt.close(1)
