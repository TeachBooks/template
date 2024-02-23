import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pyvinecopulib as cop

class Bivariate:
    """Bivariate dependent distribution, design to function in the 
    same way as an instance of the scipy.stats.rv_continuous class,
    specifically, with methods: cdf, pdf, rvs.
    """
    
    def __init__(self, X1, X2, rho):
        """Constructor to initialize Bivariate object.
        
        Arguments:
        ---
        X1: scipy.stats.rv_continuous object. Marginal distribution
        X2: scipy.stats.rv_continuous object. Marginal distribution
        rho: float. Pearson correlation coefficient.
        """
        self.X1 = X1
        self.X2 = X2
        self.rho = rho
        self.copula_uv = cop.Bicop(family=cop.BicopFamily.gaussian, parameters = [rho])
        
    def cdf(self, x):
        """Compute cdf with array or list as argument: [x1, x2]."""
        x1 = x[0]
        x2 = x[1]
        u = self.X1.cdf(x1)
        v = self.X2.cdf(x2)
        return self.copula_uv.cdf(np.array([[u, v]]))[0]

    def pdf(self, x):
        """Compute pdf with array or list as argument: [x1, x2]."""
        x1 = x[0]
        x2 = x[1]
        u = self.X1.cdf(x1)
        v = self.X2.cdf(x2)
        return self.copula_uv.pdf(np.array([[u, v]]))[0]*self.X1.pdf(x1)*self.X2.pdf(x2)

    def rvs(self, size=1):
        """Create random sample with keyword argument size."""
        sample = self.copula_uv.simulate(size)
        sample_X1 = self.X1.ppf(sample[:,0])
        sample_X2 = self.X2.ppf(sample[:,1])
        return np.vstack([sample_X1.T, sample_X2.T]).T

def plot_contour(bivar, xy_lim, data=None,
                 design_case=None, design_region=None,
                 nb_points=100):
    """Contour plot of PDF in the bivariate plane (X,Y).
    
    bivar: bivariate distribution, defined by
        scipy.stats.multivariate_normal.
    xy_lim: list. 1x4 list of xlim and ylim (in order) for plot limits.
        
    Optional arguments:
    
    data: array. A 2xN array of points.
    design_case: list. Typically a 1x2 list defining a key
        calculation point; plots as a red dot(s)
    design_region: array. A 2xN array of points that define the
        boundary of a region that will be shaded in gray between
        the boundary and the max y-axis value (ylim[1]).
    nb_points: int. Size of the grid (default: 200).

    returns: matplotlib.pyplot Figure and Axis objects. 
    """
    
    f, ax = plt.subplots(1)

    xlim = [xy_lim[0], xy_lim[1]]
    ylim = [xy_lim[2], xy_lim[3]]

    x = np.linspace(xlim[0], xlim[1], nb_points)
    y = np.linspace(ylim[0], ylim[1], nb_points)
    X,Y = np.meshgrid(x,y)
    pdf = np.zeros(X.shape)
    for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                # if X[i,j]>0 and Y[i,j]>0:
                pdf[i,j] = bivar.pdf([X[i,j], Y[i,j]])
    
    ax.contour(X, Y, pdf, levels=8, cmap=cm.Blues)
    
    if isinstance(data, np.ndarray):
        ax.scatter(data[0,:], data[1,:], s=10.0,
                   facecolors='none', edgecolors='darkgray',
                   label='Data')
    
    if isinstance(design_region, np.ndarray):
        ax.plot(design_region[0,:], design_region[1,:],
                label='Design Boundary', color='k')
        ax.fill_between(design_region[0,:], design_region[1,:],
                        ylim[1], label='Design Region', color='grey')
    
    if design_case:
        ax.plot(design_case[0], design_case[1], 'ro',
                label='Design Case')
    
    ax.set_aspect("equal")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel(r"$X_1$", fontsize=14)
    ax.set_ylabel(r"$X_2$", fontsize=14)
    if isinstance(design_region, np.ndarray) or design_case:
        ax.legend()
    return f, ax 