# Dam and River

You are tasked to analyse the safety of a dam and the downstream river system. Downstream of the dam there is a dike ring protected by two main dike sections which must be able to contain water released from the reservoir. The dike sections are connected to each other and form a continuous boundary along the same side of the river. Let $P(F_1)=0.01$ and $P(F_2)=0.01$ denote failure probability of dike section 1 and section 2 respectively. There appears to be a correlation between failures of both sections, $\rho_{1,2}=0.9$, and the figure below shows the effect of the correlation coefficient on the joint failure of the two sections.

%commented paragraphs were used for an exam question with a fault tree

%You are tasked to analyse the safety of a dam. The dam itself can fail due to instability, and another failure mechanism is failure of the spillway due to uncontrolled erosion that could reach the body of the dam. If water levels in the reservoir become high, water is released from the reservoir into the spillway due to overflow, which happens approximately once every 10 years.

%When water is released through spillway, there are two situations that could lead to a weak spillway prone to erosion and failure: 1) hidden damage to the spillway structure that cannot be detected in yearly inspections, and 2) a crack in the concrete of the spillway which has been missed during the yearly inspection.

%Downstream of the dam there is an area protected by two main dike sections which must be able to contain water released from the reservoir. A dike section fails if the river discharge exceeds a critical discharge $Q_c$ with a probability of exceedance of 1/100 per year, which leads to flooding of the area. There appears to be a correlation between failures of both sections, $\rho_{1,2}=0.9$, and the figure below shows the effect of the correlation coefficient on the joint failure of the two sections.

```{figure} ../figures/system-corr-coeff.PNG
---
width: 400px
name: corr-coeff-or
---
Effect of correlation coefficient joint failure, $P(A \cap B)$ (assume that $P(A \cap B)=0.003$ at $\rho=+0.9$, where the arrow is located).
```

**Question 1:** Estimate the probability of flooding of the area protected by the two dike sections. Assume that the failure probability of each mechanism is 0.01, and they are _not_ independent; however, you can use the figure above to quantify this.

```{admonition} Answer
:class: tip, dropdown

Flooding of the protected area occurs when at least one of the two dike section fails. This is a series system. Thus, probability of flooding of the protected area can be determined by:

$$
    P(\textrm{flooding}) &= P(\textrm{dike sections 1 fails}\:\cup \textrm{dike section 2 fails})\\
    P(F_1 \cup F_2) &= P(F_1) + P(F_2) - P(F_1 \cap F_2)
$$

Based on the figure and the correlation $\rho_{1,2} = 0.9$, the joint probability of failure $P(F_1 \cap F_2)=0.003$ and the series failure probability is

$$
    P(\textrm{flooding}) = 0.01 + 0.01 - 0.003 = 0.017 \: \mathrm{/year}
$$
```

## Dam repair: probabilistic planning

The dam has to be repaired. The responsible minister wants to make sure the whole project is finished within 12 months, and only accepts a probability of 10% that actual construction works exceed this duration. The dam reinforcement consists of two activities. The second activity can only start when the first one has been finished. The durations of both activities are uncertain and normally distributed. The first activity has a mean duration of $\mu_1=4$ months and a standard deviation of $\sigma_1 = 1$ month; for the second activity $\sigma_2 = 2$ months.

**Question 2:** Compute the mean duration of the activity 2, so that the project duration would fall within the criterion given by the minister.

```{admonition} Answer
:class: tip, dropdown

Let $T_1$ and $T_2$ denote the duration of activities 1 and 2; $T$ denotes the total duration; $T_1$ and $T_2$ are normally distributed:

$$
    T_1 \sim \mathcal{N}(
        \mu_1=4,\sigma_1=1) \\
    T_2 \sim \mathcal{N}(\mu_2=?,\sigma_2=2) 
$$

$T = T1 + T2$ is also normally distributed, where

$$
\mu_T &= \mu_1 + \mu_2 \\
\sigma_T &= \sqrt{\sigma_1^2 + \sigma_2^2} = \sqrt{5} = 2.326
$$

The probability of project duration greater than 12 months can be found with the complementary standard normal CDF, and should be a maximum of 0.1:

$$
1-\Phi\left[\frac{12\:\mathrm{months}-\mu_T}{\sigma_T}\right]=0.1
$$

Applying the inverse CDF allows us to solve for $\mu_1$:

$$
\frac{12-\mu_T}{\sigma_T} &=\Phi^{-1}[0.9] \\
\frac{12-(\mu_1 + \mu_2)}{\sigma_T} &=1.2816
$$

$$
\mu_1 &= 12 - 1.2816 \cdot \sigma_T - \mu_2 \\
\mu_1 &= 12 - 1.282(2.326) - 4 = 5.018\:\mathrm{months}
$$

<!-- Limit state equation: total duration of constuction will not exceed 12 months, thus:

$$
    Z = 12 - (T_1 + T_2)
$$

The event $Z<0$ reflects that the actual construction works exceed the duration the minister want (12 months). It is acceptable that the actual construction works exceed this duration with a probability of 10%. Thus: $P(Z<0) = 0.1$. This leads to $\beta_z = 1.28155$

Application of Level II reliability calculation:

$$
    \mu_z = 12 - (\mu_1 + \mu_2) = 8 - \mu_2 \\
    \sigma_z = \sqrt{\sigma_1^2 + \sigma_2^2} = \sqrt{5} = 2.326 \\
    8 - \mu_2 = \beta_z \cdot \sigma_z = 2.86 \\
    \mu_2 = 5.13 \: \mathrm{months}
$$ -->
```

## Acceptable risk

The government wants to study the acceptable risk and the acceptable probability of dam failure. Two criteria are used for acceptable risk:

- Societal risk (SR): an FN limit line: $P_f \leq 10^{-2}/n^2$.
- Individual risk (IR): $IR \leq 10^{-4}$ per year.

We know that mortality in case of dam failure is $F_{d|f} = 0.1$ and that the population living downstream of the dam is 1000 people. 

**Question 3:** Plot the FN limit line and indicate the acceptable probability of failure according to both criteria (individual risk, societal risk).

````{admonition} Answer
:class: tip, dropdown

```{figure} ../figures/exercise-dam-fn-limit-line.png
---
width: 500px
---
```
````

**Question 4:** Provide an advice on the acceptable probability of failure for the dam. Give the proposed numerical value and a short motivation.

```{admonition} Answer
:class: tip, dropdown

Based on individual risk criterion, we have:

$$
    IR = P_f P_{d|f} \leq IR_{acc}
$$

where $P_{d|f}=0.1$. Hence, the acceptable probability of failure is:

$$
    P_f \leq \frac{IR_{acc}}{P_{d|f}} = \frac{10^{-4}}{0.1} = 10^{-3} \: \mathrm{/year}
$$

Based on societal risk criterion (FN-Curve):

Acceptable failure probability can be determined by the FN-Curve:

$$
    P_f = 1 - F_N(n) \leq \frac{C}{n^\alpha} = \frac{10^{-2}}{n^2}
$$

Based on given information above, expected number of casualties per dam failure event is $n = F_{d|f}\cdot 1000 = 100$.

$$
    P_f &\leq \frac{10^{-2}}{100^2} \\
    P_f &= 10^{-6} \: \mathrm{/year}
$$
 
The most stringent of the two criteria applies, so the proposed safety standard would be $10^{-6}$ per year for the given inputs.
```
