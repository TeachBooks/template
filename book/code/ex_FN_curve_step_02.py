import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero

# Cumulative Distribution Function 

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>") # add arrows
    ax.axis[direction].set_visible(True) # x and y from origin
    
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False) # hide borders

N_fatalities = ['0', '10', '100', '']
N_fatalities_loc = [0.03, 0.33, 0.76, 0.95]

pdf = ['0', '0.989', '0.999', '1']
pdf_loc = [0.03, 0.66, 0.86, 0.99]

ax.step(N_fatalities_loc, pdf_loc, color= 'darkblue',linewidth=4)

ax.set_xticks(N_fatalities_loc)
ax.set_xticklabels(N_fatalities)

ax.set_yticks(pdf_loc)
ax.set_yticklabels(pdf)

ax.set_title('Cumulative distribution function, $F_{N}(n) = P(N \leq n)$', x=0.55, y=1.0)
ax.set_xlabel('Fatalities')
ax.set_ylabel('Probability')

ax.text(0.8, 0.9, r'} $10^{-3}$', fontsize=20)
ax.text(0.4, 0.725, r'} $10^{-2}$', fontsize=30)

plt.savefig('ex_FN_curve_step_02_py.svg')