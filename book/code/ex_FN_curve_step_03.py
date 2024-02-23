import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero

# FN curve

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>") # add arrows
    ax.axis[direction].set_visible(True) # x and y from origin
    
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False) # hide borders
    
N_fatalities = ['0', '10', '100','100']
N_fatalities_loc = [0.03,0.33, 0.95, 0.95]

pdf = ['0','$1.1 * 10^{-2}$', '$10^{-3}$','0']
pdf_loc = [0.03,0.99, 0.66, 0.03]

ax.step(N_fatalities_loc, pdf_loc, color= 'darkblue',linewidth=4)

ax.set_xticks(N_fatalities_loc)
ax.set_xticklabels(N_fatalities)

ax.set_yticks(pdf_loc)
ax.set_yticklabels(pdf)

ax.set_title('FN curve, $1-F_{N}(n) = P(N > n)$', x=0.75, y=1.0)
ax.set_xlabel('Fatalities')
ax.set_ylabel('Probability')

plt.savefig('ex_FN_curve_step_03_py.svg')