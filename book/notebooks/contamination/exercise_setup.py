import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from scipy import stats
import seaborn as sns

def process_negative_values(q, n, a):
    """Prevents problems with negative values in sqrt of C_C0 function."""
    N_q = sum(q<0)
    N_n = sum(n<0)
    N_a = sum(a<0)
    set_value = 0.001
    if N_q > 0:
        for i in range(len(q)):
            if q[i]<0:
                q[i] = set_value
        print(f'q has {N_q} negative values that have been set to {set_value:.1e}.')
    if N_n > 0:
        for i in range(len(n)):
            if n[i]<0:
                n[i] = set_value
        print(f'n has {N_n} negative values that have been set to {set_value:.1e}.')
    if N_a > 0:
        for i in range(len(a)):
            if a[i]<0:
                a[i] = set_value
        print(f'a has {N_a} negative values that have been set to {set_value:.1e}.')
    return q, n, a

class RandomVariableDistribution():
    """Define a N or LN probability to use in MUDE week 2.7 exercise.
    
    Usage:
    -----
    Create an instance of the class
        by default, the random variable is ~N(0,1)
    Specify distribution using 1st and 2nd moments for N or LN:
        --> use method define_distribution to change it!
             (the method prints a summary of the change)
        for example, copy/paste the following:
            test = RandomVariableDistribution()
            test.print_status()
            test.define_distribution(mean=5, stddev=1, dist_type='LN')
    An instance will include the following attributes:
        - distribution moment and (scipy) parameters shape, location, scale
        - dist_object: distribution object (scipy.stats)
        - get_sample: method for getting random samples from the distribution
        - plot_pdf_or_cdf:
    """
    
    def __init__(self):
        self.mean = 0.
        self.stddev = 1.
        self.dist_type = 'N'
        
    def print_status(self):
        """Returns current parameter values and distribution type."""
        print(f'The mean is {self.mean:.3e}')
        print(f'The standard deviation is {self.stddev:.3e}')
        if self.dist_type == 'N':
            distribution_name = 'Normal'
        elif self.dist_type == 'LN':
            distribution_name = 'Lognormal'
        print('The distribution is ' + distribution_name)
        
    def define_distribution(self,
                            mean=None,
                            stddev=None,
                            dist_type=None,
                            print_new_dist=False):
        """Compute distribution parameters and RV object from moments.
        
        Usage:
        -----
        Optional arguments will override current dist:
            --> default distribution is standard normal, ~N(0,1)
            mean: float
            stddev: float
            dist_type: 'N' or 'LN'
            print_new_dist=True to print distribution changes.
        """
        if mean is None:
            mean = self.mean
        if stddev is None:
            stddev = self.stddev
        if dist_type is None:
            dist_type = self.dist_type
        if dist_type == 'N':
            shape = None
            location = mean
            scale = stddev
            dist_object = stats.norm(loc=location, scale=scale)
        elif dist_type == 'LN':
            """
            Finds distribution parameters of LN-distributed X,
            which are equivalent to the mean and standard deviation
            of the log of X: Y = ln(X), then converts to the
            parameterization used by scipy.stats.lognorm.
            """
            stddev_y = np.sqrt(np.log(1 + (stddev/mean)**2))
            mean_y = np.log(mean) - 0.5*stddev_y**2
            
            shape = stddev_y
            location = 0
            scale = np.exp(mean_y)
            dist_object = stats.lognorm(s=shape,
                                           loc=location,
                                           scale=scale)
        else:
            raise ValueError("You can only use N or LN for self.dist_type.")
        self.mean = mean
        self.stddev = stddev
        self.dist_type = dist_type
        self.shape = shape
        self.location = location
        self.scale = scale
        self.dist_object = dist_object
        self.get_sample = lambda size : self.dist_object.rvs(size=size)
        if print_new_dist:
            self.print_status()
        
    def plot_pdf_or_cdf(self, plot_type='pdf', plot_limits=None):
        """Plots the pdf or cdf (specify choice with plot_type).
        
        Usage:
        -----
        No inputs required, but there are optional inputs:
            plot_type='cdf' to plot cdf (pdf is default value)
            plot_limits: list with 2 values for x-axis
        """
        if plot_limits is None:
            if self.dist_type == 'N':
                plot_limits = [self.mean - 3*self.stddev,
                               self.mean + 3*self.stddev]
            elif self.dist_type == 'LN':
                'Avoid negative or zero value for lognormal dist.'
                lower_value = self.mean - 3*self.stddev
                if lower_value <= 0:
                    lower_value = 0.01
                plot_limits = [lower_value,
                               self.mean + 4*self.stddev]
            else:
                raise ValueError("You can only use N or LN for self.dist_type.")

        plot_x = np.linspace(plot_limits[0], plot_limits[1], 1000)
        if plot_type == 'pdf':
            plot_y = self.dist_object.pdf(plot_x)
            y_label = 'PDF [-]'
        elif plot_type == 'cdf':
            plot_y = self.dist_object.cdf(plot_x)
            y_label = 'CDF [-]'
        else:
            raise ValueError("You must specify pdf or cdf for plot_type.")
        fontsize = 15
        plt.figure()
        plt.plot(plot_x, plot_y, 'k-', linewidth=3)
        plt.xlabel('Random Variable, X', fontsize=fontsize)
        plt.ylabel(y_label, fontsize=fontsize)
        plt.show()
        
def pdf_of_function_of_RV(cases, case_C=True, case_name=None, plot_limits=None):
    """Plot the PDF of a sampled function of random variables (C_C0 or Z).
    
    Usage:
    -----
        cases: a list of arrays
        case_C=True (default) assumes C_C0 is given. False is for Z.
        case_name: list of strings with the labels for each array.
                   e.g., ['Original', 'High sigma_a', 'Low sigma_a']
                       (default will return Case i for all arrays)
        plot_limits: list of two values that override default limits
                     for x-axis.
    """
    bw_adjust = 3 # adjusts smoothness of Seaborn kernel density contours
    labels = []
    
    plt.figure()
    
    for i in range(len(cases)):
        if case_name == None:
            labels.append(f'Case {i+1}')
        else:
            labels.append(case_name[i])
        sns.kdeplot(cases[i], label=labels[i], ax=plt.gca(), bw_adjust=bw_adjust)
    plt.legend()
    if case_C:
        plt.xlabel('Concentration ratio, $C/C_0$ [$-$]')
        if plot_limits == None:
            plt.xlim(0,1)
        else:
            plt.xlim(plot_limits)
    else:
        plt.xlabel('Limit-state function, $Z=\mathrm{threshold}-C/C_0$ [$-$]')
        if plot_limits == None:
            plt.xlim(-2,1)
        else:
            plt.xlim(plot_limits)
    plt.ylabel('PDF [$]$')
    plt.grid()
    plt.show()
    
def monte_carlo(Z):
    """Monte Carlo analysis for sampled function of random variables.
    
    Returns a summary of the analysis and a plot of pf and c.o.v..
    The only input is an array of the sampled limit state-function.
    Assumes that failure is when the limit-state function Z<0.
    """
    N = len(Z)
    Nf = np.sum(Z<0)
    
    if Nf == 0:
        raise ValueError('No failure realizations in the sample!')
    elif Nf == N:
        raise ValueError('All realizations in the sample failed!')
    
    pf = Nf/N
    
    N_f_c = np.cumsum(Z<0)
    N_i = np.arange(1,len(N_f_c)+1,1)
    p_f_c = N_f_c / N_i
    with np.errstate(divide='ignore'):
        V = 1/(np.sqrt(N_i*p_f_c))
    
    print(f'MONTE CARLO RESULTS\n'
          f'--------------------------------------------------\n'
          f'    N = {N}, number of samples\n'
          f'   Nf = {Nf}, number of failed realizations\n'
          f'   pf = {pf:.3e}, estimated failure probability\n'
          f'    V = {V[-1]:.3f}, c.o.v. of estimated pf\n')
    
    plt.loglog(N_i,p_f_c)
    plt.xlim(10,N)
    plt.ylim(10**(np.floor(np.log10(pf)) - 1),1)
    plt.grid()
    plt.xlabel('Realization No.')
    plt.ylabel('Estimated failure probability, $\hat{p}_f$')
    plt.show()
    
    plt.plot(N_i,V)
    plt.xscale('log')
    plt.grid()
    plt.xlabel('time step')
    plt.ylabel('c.o.v.')
    plt.show()
    
    return Nf,pf