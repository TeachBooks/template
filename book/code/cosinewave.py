import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, endpoint=True)
y = np.cos(x)

plt.figure()
plt.plot(x, y)
plt.title('$y=\cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('cosinewave.svg')