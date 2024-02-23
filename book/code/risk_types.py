import numpy as np
import matplotlib.pyplot as plt

# Given Parameters

N_fatalities = np.linspace(1,1000,1000)  # fatalities

P_df = 0.1; beta = 0.1

alpha = 2
k = 3
N_A = 100

r= 0.025
I = 5*10**6
B = 0.33

# Individual Risk

Pf_ind_risk = (beta*(10**-4))/P_df  # per year

# print('Acceptable Failure Probability: ', Pf_ind_risk)

# Societal Risk

C = ((beta*100)/(k*np.sqrt(N_A)))**2  # binomial distribution

Pf_SR = (C/(N_fatalities**alpha))

# Economic Risk

D_damage = (5*10**7)*N_fatalities

Pf_ER = (I*B*r)/(D_damage)

# Visualize

my_linewidth = 4

plt.figure(figsize=(8,6))

plt.yscale('log')
plt.xscale('log')
plt.plot(N_fatalities, Pf_SR, linewidth=my_linewidth, label='Societal Risk')
plt.plot(N_fatalities,Pf_ER, linewidth=my_linewidth, color='r', label='Economic Risk')
plt.axhline(Pf_ind_risk, linewidth=my_linewidth, color='g', label='Individual Risk')

plt.ylabel('Probability of Exceedance, $1-F_N(n)$')
plt.xlabel('Fatalities, N')
plt.ylim(10**(-7),1)

plt.legend(loc='upper right')

plt.savefig('risk_types_py.svg')