import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 101)
y_2 = 1 / (1 + 0.02)**t
y_4 = 1 / (1 + 0.04)**t

fig = plt.figure()
plt.plot(t, y_2, label='2%')
plt.plot(t, y_4, label='4%')
plt.grid()
plt.legend()
plt.xlabel('Year')
plt.ylabel('Normalized Present Value [$-$]')

plt.savefig('present_value_py.svg')
