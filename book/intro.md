(intro)=
# Risk and Reliability for Engineers 

Almost all activities in life are characterized by some level of risk, such as riding a bike or driving a car, boarding an airplane, or living below sea level behind flood protection system. Particularly within the field of civil engineering, risk and safety are key concepts that should be taken into account explicitly in design and management. Failures of systems providing flood protection, water distribution, transportation networks, air quality control, buildings and other infrastructure are expected to occur rarely, but can lead to large consequences. On the other hand, these systems also provide many benefits to humankind on a daily basis. 

*Risk* is often defined simply as the combination of probability and consequences; it is a measure of how bad something can be (the consequence) combined with the chance that it can happen. In mathematical form: 

$$\text{Risk}_\text{bad thing}=\text{Consequence}_\text{bad thing}\cdot\text{Probability}_\text{bad thing}$$

```{note}
:class: dropdown
Why are the variables above written using words? Because many different terms and symbols are used in different fields of science and enginering which refer to about the same mathematical concepts. For example, 'failure probability,' $p_f$, is often used when designing structural components. However, this term may be misleading when applied to the probability that the concentration of a solute in groundwater exceeds a certain value, or the discharge of a river falling below a regulatory threshold for fish migration.
```

As engineers we are typically concerned with making sure bad things don't happen, or, stated more precisely for our purposes: *reducing the **probability** of a bad thing happening to an **acceptable** level.* To determine if this probability results in a situation that is *safe enough,* an acceptable level of risk needs to be defined. The eventual decision about acceptable risk is predominantly a political one, but engineers can have an important role in the discussion and decision-making. They can provide information on failure probabilities and consequences (economic consequences, life loss, etc.) of a given system and highlight trade-offs between investments in safer systems and risk reduction. Risk plays an important role in many current societal discussions. Examples include recent discussions related to Covid-19 vaccination programs and mitigation measures like facemasks, where there was a lot of uncertainty in the effect of on virus spread. Another example is the discussion over nuclear power versus fossil fuels: both activities bring various benefits (energy generation) but also introduce additional risks to the population and environment. A systematic analysis of risks of (proposed) projects can help to inform the broader societal discussions.

Inevitably, the consideration of risk should result in a specific value of probability that can be used in the design or evaluation of something; in other words, a specific criteria for $\text{Probability}_\text{bad thing}$. For standard applications and systems that are frequently constructed, the risk analysis has been done and building codes are available that define acceptable safety levels in such a way that the failure probability of a structure is sufficiently small. For example, Eurocode provides guidance for the design of structures using so-called target values for the failure probability different safety classes. Thus, critical buildings like hospitals are designed to be stronger than a hardware store. However, for other applications, e.g. special structures or new applications like the reliability of renewable energy-generating components, no standard codes or guidelines are available for design and a more explicit analysis of the reliability and risk of the system is required. An example from the past is the design of the Eastern Scheldt barrier. The acceptable probabilities of failure of the structure and non-closure of the gates were determined based on the acceptable risk of flooding of Zeeland. These probability values formed the basis for the so-called probabilistic design of the barrier in the 1970’s.

```{note}
:class: dropdown
Although much of this book focuses on calculating failure probability, or $\text{Probability}_\text{bad thing}$, we call this a reliability analysis, where *reliability* is simply  

$$\text{Reliability}=1-\text{Probability}_\text{bad thing}$$

So in fact, as engineers we are optimistic, otherwise this chapter would be called Risk and *Un*reliability.
```

## Risk and Reliability in Practice

Throughout this book we will repeatedly draw on the field of flood management to illustrate risk and reliability concepts as this field requires expertise from all perspectives in civil and environmental engineering and geosciences, from climate and hydrologic processes to evacuation and recovery. In addition, this field has driven the development and use of risk and reliability techniques in the Netherlands since the flooding disaster of 1953, not to mention the experience gained during the previous millenium, albeit in a less rigorous mathematical fashion. And finally, new safety standards for primary flood defences in the Netherlands have been in place since 2017 that are formulated as a tolerable failure probability of dike[^dike] segments. As such, dike reinforcements are legally required to be designed according to these new standards, which requires one to show that the failure probability is less than an allowable maximum value.

Despite the focus on flood management, many applications exist in other fields, for example the discussion about the gas extraction in the North of the Netherlands which leads to increased earthquakes, building damage and potential injury to humans. A thorough analysis of the probability of earthquake occurrence, structural safety of various infrastructure (houses, levee, hospitals, pipelines), benefits associated with extracting gas and the resulting level of risk is required to make decisions about how to manage this industry. As with the flood management application, advanced knowledge of probabilistic techniques is needed. 

## It All Comes Back to Probability

In short, risk and reliability concepts cannot be defined or applied without *probability.* It is necessary in order to quantify uncertainty and take it into account when making decisions, regardless of whether our specific task is to investigate, assess, design or create policy for a particular engineering problem. Probability theory is a powerful tool because it provides a way to quantify many aspects of uncertainty, for example:
- precision of measurements
- variability in data
- accuracy and precision of data-driven or physics-based models
- stochastic processes
- unknown conditions due to lack of data or 
- inability to predict the outcome of future events with sufficient accuracy or precision
- and many more

It is crucial that civil and environmental engineers and geoscientists are able to understand and apply the concepts of risk and reliability, as well as probability theory. As such, these lecture provide an introduction to the fundamental techniques and concepts necessary to do so. 

## Book Overview

Risk and reliability concepts have been organized into five primary chapters to introduce fundamental concepts and progressively illustrate how they are applied in practice.
- **Probabilistic Design** describes how probability is used in the design process and illustrates key concepts through simple examples and 'patterns' (analytic expressions and visual representations).
- **Risk Analysis** as a process is formally defined and quantitative risk measures are introduced.
- **Component Reliability** and **System Reliability** briefly introduce approaches for evaluating reliability, or $\text{P}_\text{bad thing}$, in order to carry out probabilistic assessment and design quantitatively. This is the *quantitative analysis* step of a risk analysis.
- **Risk evaluation** provides simple quantitative tools and a framework for establishing risk-based safety standards and economic risk criteria. This is a key step in the risk analysis process.

Additional chapters are provided to put these concepts into context, explain industry-specific characteristics or indicate possibilities of additional study for the student.

### Additional Resources

If you are in need of a quick refresher on fundamental probability and statistics topics, you may find the online course [Probability and Statistics for Engineers](https://tudelft-citg.github.io/learn-probability/) helpful. This course was created for those who need to brush up on topics from a prior bachelors-level course. If you have no background in probability and statistics you will need to take a more thorough approach; we recommend the Probability Theory and Statistics courses offered in the Mastering Mathematics series from TU Delft, which you can find [here](https://online-learning.tudelft.nl/topic/mastering-mathematics/) (also on EdX).

### Additional Information

This book was developed and used for use in the master's program in the faculty of Civil and Environmental Engineering at Delft University of Technology in the Netherlands. Although the concepts are relevant for a wider audience outside the faculty, the generic reference "for Engineers" in the title refers to the diverse areas of emphasis evolving within the field historically referred to as "civil engineering." For example, our MSc programs in Environmental Engineerinng and Applied Earth Sciences.

Additional information about authors, licenses and how the book is made can be found on the {ref}`Credits and License page <credits>`. We hope you enjoy this book, and don't hesitate to contact {ref}`the Editor <editor>` with questions or suggestions!

[^dike]: A dike is a structure, typically made of soil, that protects a specific region from flooding by physically holding back water. Usually associated with rivers, such structures are also widely used on the coast, especially in low elevation areas such as the Netherlands. The Dutch word for levee is *dijk,* but English word *dike* is used in this book. Outside of the Netherlands the words *embankment* and *levee* are used.

---

This book is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png"/></a>