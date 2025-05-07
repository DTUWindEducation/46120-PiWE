"""Practice understanding of function handles.

Use scipy.optimize.fsolve to find the closest root of a function.
"""
import matplotlib.pyplot as plt
import numpy as np
# TODO! Add an import statement so you can use fsolve
import scipy
from scipy.optimize import fsolve


def eval_quadratic(x, a, b, c):
    """Evaluate f(x) = a*x^2 + b*x + c."""
    return a * x**2 + b * x + c  # TODO! Update this so it returns parabola


def plot_quadratic(a, b, c, xplot=np.linspace(-5, 5, 301)):
    """Plot a quadratic function."""
    fig, ax = plt.subplots(figsize=(6, 3))  # initialize figure
    yplot = eval_quadratic(xplot, a, b, c)  # define y-values to plot
    ax.plot(xplot, yplot)  # plot the quadratic function
    ax.plot(xplot, np.zeros_like(xplot), '--', c='0.3', zorder=0)  # plot a zero-line
    ax.set(xlim=xplot[[0, -1]], xlabel='x', ylabel='y')  # add labels
    ax.grid()  # add a grid
    fig.tight_layout()  # rescale axes in figure to look nice
    return fig, ax


if __name__ == '__main__':
    # define constants for parabola coefficients and initial guess
    A, B, C = 1, 1, -12
    X0 = 2  # TODO! Define a constant "X0" with the initial guess
    
            
    #ax.scatter(X0, eval_quadratic(X0, A, B, C), color='black', marker='x', label='Initial Guess')
    # plot the parabola and initial guess as an x
    fig, ax = plot_quadratic(A, B, C)
       
    ax.plot(X0, 0, 'kx')# TODO! Add the initial guess to the plot as a black "x"

    # call fsolve to find the closest root, add to plot as red circle
    root = fsolve(eval_quadratic, X0, args=(A, B, C))# TODO! Call fsolve using the necessary arguments and keyword arguments
    ax.plot(root, 0, 'ro', mfc='none') # TODO! Add the found root to the plot as a red circle with a see-through center

    plt.show()
