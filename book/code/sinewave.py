import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, endpoint=True)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title('$y=\sin(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('sinewave.svg')