(econ_optimization)=
# Economic Optimization

The previous sections have focussed on decisions for which the number of actions was limited, e.g. excavation with or without drainage and the associated costs and benefits. However, there are several situations in which the number of actions is unlimited. This occurs when the failure probability level has to be decided for a system that is yet to be designed, with an infinite number of design options. An example of this type of decision problem is the heightening of dikes, as in theory an unlimited amount of values can be chosen for the elevation, e.g. 2m, 5m, 5.1m, 5.11m, 5.1111m 6m etc.

For this situation an economic optimization that takes into account the costs of increasing the safety level and reducing the risks can be applied to derive an optimal level of safety (or the optimal “failure probability”). The economic optimization was developed and applied by {cite:t}`vandantzig1956`, to derive the optimal dike height for South Holland after the 1953 storm surge disaster, as will be further elaborated in the next section.
In the economic optimization the total costs ($C_{tot}$[€]) are determined, consisting of the investments $I$[€] in a safer system and the present value of the risk $R$[€].

$$
    C_{tot} = I + R
$$

The annual risk, or expected economic dagmage is found by:

$$
    E(D) = P_f D
$$

where:

- $E(D)$ the expected value of the risk [€/year]
- $P_f$ the failure probablity of the system per year [1/year]
- $D$ the damage in case of failure [€]

In this approach it is thus assumed that all damages are expressed in monetary terms. Additional criteria for separately considering the loss of human life are included in the next section. 

The present value of the risk for an infinite time horizon can be found as follows:

$$
    R = \frac{P_f D}{r}
$$

The risk can be reduced by constructing a safer system (a lower $P_f$), or limiting the damage (smaller $D$). In this case we assume prevention measures that focus on reducing the failure probability. The investments will become a function of the failure probability of the system, since increasing the safety will lead to an increase of costs. 

$$
    I = I(P_f)
$$

{numref}`economic_optimum` shows the costs and risks as a function of the accepted failure probability of a system. The economic optimum is found when the total costs are minimal.

```{figure} ../figures/economic_opt.svg
---
width: 600
name: economic_optimum
---
Economic optimization: costs, risks and total costs as a function of the
failure probability of the system. 
```

For this situation the following is valid:

$$
    \frac{d C_{tot}}{d P_f} = 0
$$

This approach can be applied to various decisions problems, such as the optimal dike height (see next section) but also the dimensioning of other interventions such as sprinklers or ventilation in tunnels to reduce fire risks. In cases where no continuous functions are available to create a curve as in {numref}`economic_optimum`, the analyst can consider a limited number of design options (e.g. no, small, medium or large sprinklers in a tunnel) and determine investments, risks and total costs for these options.

In addition to the determination of the optimal failure probability, the cost benefit criterion should still be verified. (It is possible that we find an economic optimum with higher total costs than in the current situation without interventions). It is checked whether the benefits of risk reduction are larger than the costs of the dike heightening, i.e. $(P_{f,0} - P_{f,opt}) D > I$.