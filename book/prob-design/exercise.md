# Exercises

Elsewhere in this book we have covered methods that will allow you to solve the discharge problem on the previous page, for example, propagation of uncertainty, functions of random variables, etc. Try the following exercises to evaluate the distribution of $q$. In each case, you should be able to define both the distribution of $q$ as well as the value of $q_{design}$:

1. Define the distribution of $q_1$ and $q_2$ as LogNormal using Scipy, then evaluate the distribution of $q$ using Monte Carlo Simulation
2. Approximate the distributions of $q_1$ and $q_2$ using only their moments and use error propagation to approximate the distribution of $q$
3. Use the moments to define Normal distributions for $q_1$ and $q_2$, then find the distribution of $q$ (hint: it should also be Normal, and you can solve for it analytically)
4. Use the moments to define Normal distributions for $q_1$ and $q_2$, then use the multivariate normal distribution in Scipy to define a correlation coefficient and explore what the effect of dependence between $q_1$ and $q_2$ has on the result.

```{note}
Solutions to these exercises are on the next page.
```

