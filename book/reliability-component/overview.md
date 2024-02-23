(rel_comp)=
# Component Reliability

This Section gives a brief introduction to some of the mathematical foundations of component reliability theory, which is focused on determining the probability of a 'bad thing' happening (see {ref}`intro`). The topic has also been covered in the {ref}`prob_design` Section (especially the {ref}`prob_design_2_rv` example), and is a key part of Step 3 (quantitative analysis) in the {ref}`risk_steps`.

## Definition

In short, a component reliability analysis evaluates the reliability of a particular engineered object, where reliability is the complement of failure probability, $p_f$. The analysis is performed by defining a function of random variables, $g_X(x)$, and mathematically specifying a region of interest, $\Omega$, often called the failure region. The function of random variables implies a multivariate probability density function, $f_X(x)$, where integrating over the failure region $\Omega$ gives $p_f$. 

$$
p_f=\int_\Omega f_X(x)\:\mathrm{d}x
$$

## A Simple Case

The most simple reliability analysis is a univariate case with one random variable. Consider a water distribution *system* that relies on groundwater (i.e., one *component* within the system). Suppose we can model the groundwater elevation as a random variable with the normal distribution:

$$
h_w \: [\mathrm{m}] \sim \mathrm{N}(\mu=5,\sigma=1)
$$

If $h_w$ drops below 2 m, the pumps run dry, and our component fails. In this case our function of random variables is simply:

$$
g(X) \rightarrow g(h_w)=h_w
$$

and failure is defined as:

$$
\Omega: h_w < 2 \mathrm{m}
$$

The component reliability analysis is thus:

$$
p_f=\int_{-\infty}^{2} f_{h_w}(h_w)\:\mathrm{d}h_w
$$

Which is easily evaluated with the CDF of $h_w$:

$$
p_f=F_{h_w}(2)=\Phi\left[ \frac{2-\mu}{\sigma}\right] =\Phi[-3]=0.00135
$$

This is nearly equivalent to the {ref}`prob_design_1_rv` example using river discharge from the {ref}`prob_design` Chapter, the only difference is there a load variable was considered and therefore evaluated with the complementary CDF.

## Not Simple Cases

The example above is 'simple' for three reasons, specifically. It has:
1. only one random variable, so the distribution of $g(X)$ is also univariate
2. the function of random variables, $g(X)$ is linear
3. the distribution of the random variables (variable, in this case) is Gaussian

These three characteristics make component reliability problems very easy to solve. In fact, you should have already done this earlier probability courses with (co)variance propagation methods. For example, solving for the mean and standard deviation of a linear function of random variables that are each Gaussian is straightforward, as the function of random variables is also Gaussian. Unfortunately, as problems become more complex, so do the methods required for solving such problems.

In this book we focus on simple situations with up to two variables (the 'bivariate' case) that can be solved analytically (linear functions and Gaussian random variables). Random variables are limited to continuous parametric distributions and linear measures of dependence (correlation coefficient, multivariate Gaussian). If these requirements are relaxed, we will use simulation to calculate the failure probability numerically (i.e., Monte Carlo simulation).

With this in mind, a generic procedure for using component reliability analysis in a probabilistic design context is:

1. determine probability distributions for each random variable (*marginal* distributions)
2. specify dependence between random variables (or independence)
3. define the function of random variables, $g_X(X)$, and region of interest, $\Omega$
4. integrate multivariate PDF, $f_X(X)$, over $\Omega$ to evaluate probability of interest
5. check probability requirement, and if needed:
6. modify component (i.e., modify 1, 2 or 3)
7. repeat 4, 5 and 6 until the requirement is met

```{note}
The term 'failure' here, widely used in civil engineering, is used here as a matter of convenience. Component reliability methods can also be used to find the probability of something that has nothing to do with failure, as long as it can be desribed with a function of random variables.
```
## Two Random Variables

The example with discharge from two rivers in the Probabilistic Design Chapter can be considered a component reliability problem with two random variables. The discharge of both tributary rivers act as loads because they both are proportional to the main design variable, $q$ or $h_{dike}$. The reliability integral is thus

$$
p_f=\int_\Omega f_{Q_1,Q_2}(q_1,q_2)\:\mathrm{d}x
$$

where the failure region $\Omega$ contains all values of $Q_1$ and $Q_2$ such that the river level exceeds the dike height:

$$
\Omega: h_{dike} \leq h_w(Q_1,Q_2)
$$

Note that if the dike were constructed to a height of 8.29 m, the component reliability would be 0.01 and the failure region would be equivalent to {numref}`design_2_rv_correct`.

<!-- Component reliability Analysis:  
- limit states (servicability, ultimate) and limit-state functions; failure definition
- Design frameworks 
- A simple case 
- Special page to illustrate partial safety factor approach. Start with univariate, then show bivariate (pointing out ‘choice’ that must be made for design point, reference it, then move along). 


- other
  - R-S
  - Z = R + S
  - non-linear
  - most of these should probably go in the component reliability chapter

Overview of non-linear problems (distribution and LSF); explanation of LSF; formulations of structural reliability. the area under the curve. Solution techniquest. Partial safety factor approach / LRFD / beta and reliability index. -->

% save for later: compare Z=R-S to and/or and explicitly show how the generalized method can incorporate higher/lower together or values related to each other; lognormal case

%To simple slope problem: *this example is borrowed from Moss, which is borrowed from Baecher and Christian. Both are excellent texts on risk and reliability analysis in civil and geotechnical engineering.*

% THIS IS REMOVED FOR 2022-23 SINCE THE SEPARATE PAGES WERE NOT COMPLETED

---

_The primary author for this chapter is Robert Lanzafame._

<!--
```{admonition} Exam Information
:class: tip, dropdown
You are expected to recognize the role of random variables (e.g., loads and resistances) within the function of random variables for a component and visualize it on a bivariate plot. Component reliability problems will limited to linear functions of normally distributed random variables; although you will *not* be asked to compute reliability.
``` -->

<!-- ```{admonition} Exam Information
:class: tip, dropdown
You are expected to recognize the role of random variables (e.g., loads and resistances) within the function of random variables for a component and visualize it on a bivariate plot. You may be asked to solve simple component reliability problems, limited to linear functions of normally distributed random variables, and evaluate the role of dependence between variables. You can produce a probabilistic design by modifying the component such that the probability of interest meets a specific criteria.
``` -->

<!-- ```{admonition} Exam Information
:class: tip, dropdown
For the exam, you will be expected to be able to recognize and solve simple component reliability problems, and describe the influence that dependence between random variables may have on the calculated probability of interest. Given a specific problem of interest, you should be able to describe failure (or non-failure) analytically as a function of random variables and visually in a bivariate plot. Using these simple frameworks, you can modify the component such that the probability of interest meets a specific criteria.
``` -->