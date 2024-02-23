(cost_benefit)=
# Cost Benefit Analysis

This section deals with simplified cost benefit analysis for risk reduction interventions in the engineering domain. An important question in evaluating (engineering) projects is whether the benefits outweigh the costs. Cost benefit analysis (CBA) is generally used for appraisal of a wide range of effects of projects or interventions in order to support decision making. The cost benefit analysis starts with defining the system and existing situation. Then, a broad range of effects of the proposed project and intervention can be identified.

{numref}`costs_and_benefits` below shows an overview of effects of the Delta works that were built after the 1953 flood disaster in the Netherlands. The main aim of the delta works was to provide flood protection to the Southwest of the Netherlands. However, other effects included the agricultural benefits to the region (benefits) and the effects on environmental quality in the estuaries in which dams were built (costs or negative effects).

```{list-table} Costs and benefits of the delta works
:header-rows: 1
:name: costs_and_benefits

* - Costs
  - Benefits
* - Construction and maintenance costs
  - Reduction of flood risk (damage, loss of life)
* - Loss of environmental quality
  - Improvement of infrastructure
* - 
  - Recreation
* - 
  - Agricultural benefits
* - 
  - Economic stimulus for the region
* - 
  - Economic stimulus for the water engineering sector
* - 
  - National Pride
```

A choice has to be made for which effects in the CBA are evaluated in monetary terms. For some items, such as construction costs or economic risk reduction (see below) this is straightforward. For other items such as environmental effects or reduction of risk to life, approaches for monetary evaluation exist, but they are not standardized or undisputed.

## Risk Reduction via Probability

When considering investments that primarily focus on risk reduction (e.g. dike reinforcement or reinforcing of buildings for earthquakes), the main benefits will consist of the reduction of expected economic damages. For a measure to be cost effective, the investments should be smaller than the risk reduction.

$$
I < \Delta E(D)
$$ (investment)

where:

- $I$ is investments
- $\Delta E(D)$ present value of risk reduction

This formula can also be used to calculated the benefit/cost ratio, i.e. $\Delta E(D)/I$, which should be greater than 1 for cost effective projects. Note that all costs and the risk reduction are given in terms of present value with a unit of €.

For investments that focus on prevention (i.e. reducing the failure probability of the system) {eq}`investment` can be formulated as follows. 

$$
  I < (P_{f,0} - P_{f, new}) D
$$ 

where:

- $P_{f,0}$ the initial failure probability
- $P_{f,new}$ the failure probability after risk reduction investment

```{admonition} Example: Drainage of a construction site - costs and benefits
The example from the previous section could also be formulated as a simplified cost-benefit analysis. The same values for the variables are used. The costs of the drainage are €150,000. The benefits are equal to the risk reduction, i.e. 

$$
  \Delta E(D) = (P_{f,0} - P_{f,d}) = (0.12 - 0.04)\text{€} 5,000,000 = \text{€} 400,000
$$ 

This shows that costs are smaller than the risk reduction benefits, i.e. $I<\Delta E(D)$. The benefit/cost ratio equals €400,000/€ 150,000 = 2.66

One can easily show that the investment would just be acceptable if the benefits and costs are equal, i.e. when the benefit / cost ratio equals 1. This would still be the case if the probability of failure with drainage equals $P_{f,d} = 0.09$.
```

## Risk Reduction via Damages

Other types of interventions do not affect the probability of an accident, but focus on reducing the damages. They are often indicated as mitigation. An example in the field of flood management concerns raising buildings instead of reinforcing the dikes. In this case the criterion becomes:

$$
I < P_{f,0}(D_0 - D_{new})
$$

where: 

- $D_0$ the initial damage [€]
- $D_{new}$ the damage after investments in reducing the consequences [€]

## Net Present Value

The foregoing assumes that both the costs and benefits are expressed in the same unit, generally in the form of a present value [€]. The net present value (NPV) represents the sum of the present values of the benefit and cost cash flows over a period of time. In engineering we often deal with situations with larger initial investments, whereas the risk reduction benefits are spread out over a longer time period. For example, when a government invests this year in flood protection, the costs are made in year 0, but the benefits will be spread over the coming decades. 

For such situations the failure probability is generally expressed per unit of time, mostly per year. That means that the risk (reduction) is expressed in terms of € per year, whereas the initial investments have the unit of €. The net present value of cost or benefit values over a future range of years can be calculated with {eq}`npv`. To calculate the net present value NPV [€] a discount rate  should be used. The discount rate represents a required return on an investment.

$$
  NPV = \sum_{t=1}^{T} \frac{C_t}{(1+r)^t}
$$ (npv)

where:

- $C_t$ the costs in year $t$ [€]
- $T$ the reference period [years]

```{admonition} Interest Rates
:class: tip, dropdown
The discount rate, $r$, is analagous to opportunity costs and interest rates that you may be familiar with from the field of economics. It provides a way to evaluate the true cost of investing in a particular project over a long time period, for example: if the value of a stock market increases with an annual interest rate of 4%, how does that compare to the expected earnings on the alternative investment under consideration?

Although civil engineering projects are typically not associated with financial investments like stocks and bonds, the need to consider the time value of money is identical. In fact, many governments use the financial instruments like bonds to finance projects, which is easy to see the relationship to interest rates.
```

The contribution of costs in a certain year to the net present value depend on the discount rate and the reference year. Costs or benefits closest to the present will have the greatest contribution. {numref}`present-value` below shows the value of $1/(1+r)^t$ for a given year $t$ for different discount rates. The higher the discount rate, the smaller the contribution to the net present value of costs or benefits that are far away from the present. For an infinite time horizon it can be shown that $\sum 1/(1+r)^t \approx 1/r$. This approximation can be used in evaluating engineering projects with a long life time.

```{figure} ../figures/present_value.svg
---
width: 600
name: present-value
---
Normalized present value of a cost or benefit in year $t$ for different discount rates.
```

(value_human_life)=
## Valuation of Human Life

The previous paragraphs have focussed on the evaluation of economic costs and benefits of risk reduction interventions. Many of these interventions also directly focus on reducing injuries and fatalities. Examples are regulations and investments in traffic safety which have introduced measures such as airbags and seat belts. 

In literature on risk management the economic valuation of human life is often depicted as a difficult problem as it raises numerous moral questions. Some claim it is unethical to put a price on human life because life is priceless. The actual expenditures on risk reducing prospects show however that the investment in the reduction of risks to humans is always finite. Different approaches are available for evaluating the costs of interventions in relation to the reduction of risk to human life, see {cite:t}`vrijling2000`; {cite:t}`jongejan2005` for a further discussion of the various approaches. One of the options is to add the economic value  of  human fatalities to the economic damages, i.e. $D+N \cdot d$. The value of the number of lives lost can be determined with different approaches. 

Several approaches are based on so-called stated preferences.  A survey can reveal how much people are willing to pay, e.g. for safety measures. In these cases the value of statistical life (VoSL) is obtained from the willingness to pay expressed by respondents in surveys. For example, in the cost benefit analysis for the flood defences in the Netherlands a value of a statistical life of €6.7 million per fatality is used {cite:p}`jeuken2013`. The Value of a Statistical life lost in traffic accidents is estimated at €2.6 million {cite:p}`SWOV2012`.

One alternative approach is based on so-called revealed preferences. The costs of saving and extra (statistical) life ($CSX$) for actual life-saving interventions that have been taken in the past can be determined. 

$$
    CSX = \frac{I}{\Delta E(N)}
$$ 

where:

- $CSX$ the costs of saving an extra life [€/life year]
- $\Delta E(N)$ the reduction of the expected number of fatalities per year

An extensive study on  values in various sectors, see {cite:t}`tengs1995` showed that these vary widely across sectors and even within sectors. The highest $CSX$ values are found for risks for small probability – large consequence events, for example in the nuclear domain. For such cases the expected number of fatalities is already small and investments in incremental safety are large.

One other approach is to base the value of a human life on macro-economic indicators. Several metrics have been proposed that relate this value to a person’s economic production.
Given the difficulties associated with economic valuation of human life and the associated risk reduction, it is decided in some domains to develop separate criteria for considering the risk to life. This topic is further elaborated in ⚠️section 3.5.