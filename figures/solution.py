"""Set of helper functions for Week 8 part of Project 4, 2023.

Primary purpose is:
    1) define dictionaries to track information about bivariate
       and univariate probability models, as well as a few
       important characteristics,
    2) print and plot results,
    3) perform simple calculations (e.g., covariance, ecdf etc).
       
Organized in order used in solution notebooks.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

from helper import plot_contour
from helper import Bivariate

def univariate_RV_dict(name, symbol, unit):
    """Create a dictionary to track a random variable."""
    d = {"name":name, "symbol":symbol, "unit":unit}
    d = create_plot_label(d)
    return d
      
def create_plot_label(univariate_dict):
    """Combine RV name, symbol, unit into key xlabel."""
    univariate_dict["label"] = (univariate_dict["name"] + ", "
                                + univariate_dict["symbol"] + " ["
                                + univariate_dict["unit"] + "]")
    return univariate_dict
      
def univariate_model_dict(dist_type, parameters,
                          distribution, empirical=False, note=None):
    """Create a dictionary to track a distribution model.
    
    dist_type: string,
    parameters: tuple, from scipy.stats rv_continuous
    distribution: frozen instance of scipy.stats.rv_continuous
    empirical: boolean. Set to True if distribution is a sample
      (array). This is just a placeholder to support other functions
      that will be used for printing results
      (e.g., compare_univar_prob).
    note: string (optional)
    """
    model = {"type":dist_type}
    model["parameters"] = parameters
    model["distribution"] = distribution
    model["empirical"] = empirical
    model["note"] = note
    
    if empirical:
        model["N"] = len(distribution)
        model["sample"] = distribution
    
    return model

def print_dist_model_summary(RV, model_key):
    """Prints info about a model."""
    print(f'Random variable {RV["name"]}, model \"{model_key}\" is:\n'
          f'    distribution: {RV[model_key]["type"]}\n'
          f'      parameters: {[f"{i:.3f}" for i in RV[model_key]["parameters"]]}\n'
          f'      (μ,σ) dist: '
          f'({RV[model_key]["distribution"].mean():.3f}, '
          f'{RV[model_key]["distribution"].std():.3f})\n'
          f'      (μ,σ) data: '
          f'({RV["data"].mean():.3f}, {RV["data"].std():.3f})\n')
    
def calculate_covariance(X1, X2):
    """Covariance of X1 and X2 (numpy arrays)."""
    mean_x1 = X1.mean()
    mean_x2 = X2.mean()
    diff_x1 = X1 - mean_x1
    diff_x2 = X2 - mean_x2
    product = diff_x1 * diff_x2
    covariance = product.mean()
    return covariance

def pearson_correlation(X1, X2):
    """Pearson correlation of X1 and X2 (numpy arrays)."""
    covariance = calculate_covariance(X1, X2)
    correl_coeff = covariance/(X1.std()*X2.std())
    return correl_coeff

def bivariate_model_dict(model_name,
                         X1_key, X1, X2_key, X2, rho):
    """Create dictionary to track the bivariate model.
    
    model_name: string. Arg is root name, which has
      marginal info added; used for plot title.
    X1, X2: dict.from univariate_RV_dict()
    X1_key, X2_key: string. Name of model of X1, X2
    rho: correlation coefficient
    
    returns: dictionary
    """
    
    d = {"X1_key":X1_key, "X1":X1[X1_key],
         "X2_key":X2_key, "X2":X2[X2_key],
         "rho":rho}
    
    d["title"] = (model_name + ": "
                  + r"$X_1 \sim$" + X1_key + ", "
                  + r"$X_2 \sim$" + X2_key + ", "
                  + r"$\rho$ = " + f"{rho:.2f}")
    
    d["xlabel"], d["ylabel"] = X1["label"], X2["label"]
    d["X1X2"] = Bivariate(d["X1"]["distribution"],
                          d["X2"]["distribution"],
                          d["rho"])
    d["data"] = np.array([X1["data"], X2["data"]])
    d["data_X1"], d["data_X2"] = X1["data"], X2["data"]
    
    return d

def compare_bivar_prob(point, model):
    """Compare probabilities at a given point (bivariate).
    
    point: array or list; size = 2.
    model: dictionary defining bivariate distribution.
    
    returns: none, except printed output.
    """
    
    data_X1 = model["data_X1"]
    data_X2 = model["data_X2"]
    N = data_X1.size
    
    left_emp = sum(data_X1 < point[0])/N
    bottom_emp = sum(data_X2 < point[1])/N
    lower_left_emp = sum((data_X1 < point[0])*(data_X2 < point[1]))/N

    union_emp = 1 - lower_left_emp
    intersection_emp = 1 - (left_emp + bottom_emp - lower_left_emp)
    
    lower_left = model["X1X2"].cdf(point)
    union = 1 - lower_left

    left = model["X1"]["distribution"].cdf(point[0])
    bottom = model["X2"]["distribution"].cdf(point[1])
    intersection = 1 - (left + bottom - lower_left)
    
    print(f'-------------------------------------------------')
    print(f'      Comparison, Empirical Values in ( )')
    print(f'-------------------------------------------------')
    print(f'Lower left, P[X1<x1, X2<x2] = {lower_left:.5f}',
          f'({lower_left_emp:.5f})')
    print(f'Left side,         P[X1<x1] = {left:.5f}',
          f'({left_emp:.5f})')
    print(f'Bottom half,       P[X2<x2] = {bottom:.5f}',
          f'({bottom_emp:.5f})')
    print(f'-------------------------------------------------')
    print(f'Case 1: P[X1>x1 or X2>x2]   = {union:.5f}',
          f'({union_emp:.5f})')
    print(f'Case 2: P[X1>x1 and X2>x2]  = {intersection:.5f}',
          f'({intersection_emp:.5f})')
    print(f'-------------------------------------------------')
    
def compare_univar_prob(point, model, dist_key):
    """Compare probabilities at a given point (univariate).
    
    point: float
    model: dictionary defining univariate distribution
    dist_key: specify which distribution model to use
    
    returns: none, except printed output.
    """
    
    data = model["data"]
    N = data.size
    p_data = sum(data < point)/N
    if model[dist_key]["empirical"]:
        N_model = model[dist_key]["N"]
        n_eval = sum(model[dist_key]["sample"]<point)
        p_model = n_eval/N_model
    else:
        X = model[dist_key]["distribution"]
        p_model = X.cdf(point)
    
    print(f'---------------------------------------')
    print(f'  Results for {model["name"]}, case {dist_key}')
    print(f'  Comparison, Empirical Values in ( )')
    print(f'---------------------------------------')
    print(f'P[X<x] = {p_model:.5f} ({p_data:.5f})')
    print(f'P[X>x] = {1 - p_model:.5f} ({1 - p_data:.5f})')
    print(f'There are {N} points in the data set.')
    if model[dist_key]["empirical"]:
        print(f'This distribution is from MCS:')
        print(f'    number of smaples = {N_model}')
    print(f'---------------------------------------')
    
def ecdf(var):
    """Empirical cdf from list or array. Returns [F(x), x]."""
    x = np.sort(var)
    n = x.size
    y = np.arange(1, n+1) / (n + 1)
    return [y, x]

def ecdf_inverse(p, data, exceedance=False):
    """Compute x = F^-1(p) for an empirical distribution."""
    N = len(data)
    if exceedance:
        p = 1 - p
    index = int(np.floor(p*(N + 1)))
    x = np.sort(data)[index - 1]
    return x

def semi_log_plots(dist_1, dist_2, exceedance=True):
    """Helper function for plot_univariate_comparison.
    
    dist_1, dist_2: ndarray, list. Empirical distributions.
    exceedance: bool. Default (True) plots exceedance, 1 - F(x)
    
    returns: matplotlib objects fig, ax
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    
    e_dist_1 = ecdf(dist_1)
    e_dist_2 = ecdf(dist_2)
    if exceedance:
        e_dist_1[0] = 1 - e_dist_1[0]
        e_dist_2[0] = 1 - e_dist_2[0]
    
    ax.step(e_dist_1[1], e_dist_1[0], 
              color='k', label='Data')
    ax.step(e_dist_2[1], e_dist_2[0],
              color='r', label='MCS Sample')
    ax.set_xlabel('$Z(X_1,X_2)$')
    ax.set_yscale('log')
    ax.legend()
    ax.grid()
    return fig, ax

def plot_univariate_comparison(rv_dictionary, dist_key, plot_values):
    """Compare univariate plots.
    
    Assumes model is an empirical distribution (MCS
    
    rv_dictionary: dict. Created from univariate_RV_dict()
    dist_key: str. Name of probability model
    plot_values: array, list (size 4). Limits of X and Y, respectively.
    returns: none, except printed output.
    """
    
    data = rv_dictionary["data"]
    model = rv_dictionary[dist_key]["sample"]
    
    fig, ax = plt.subplots(1)
    ax.hist([data, model],
             bins=plot_values,
             density=True,
             edgecolor='black');
    ax.legend(['Data', 'MCS Sample'])
    ax.set_xlabel('$Z(X_1,X_2)$')
    ax.set_ylabel('Empirical Density [--]')
    ax.set_title('Comparison of Distributions of $Z$');
    
    fig, ax = semi_log_plots(data, model, exceedance=False)
    ax.set_ylabel('CDF, $\mathrm{P}[Z < z]$')
    ax.set_title('Comparison: CDF (log scale expands lower tail)')
    
    fig, ax = semi_log_plots(data, model, exceedance=True)
    ax.set_ylabel('CDF, $\mathrm{P}[Z < z]$')
    ax.set_title('Comparison: CDF (log scale expands lower tail)')