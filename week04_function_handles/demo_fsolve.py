"""Practice understanding of function handles.

Use scipy.optimize.fsolve to find the closest root of a function.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve #pass in a function handle and an initial guess to find the root of the function
# TODO! Add an import statement so you can use fsolve


def eval_quadratic(x, a, b, c):
    """Evaluate f(x) = a*x^2 + b*x + c."""
    #return np.zeros_like(x)  # TODO! Update this so it returns parabola
    return a*x**2 + b*x + c

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
    X0= 1 # TODO! Define a constant "X0" with the initial guess

    # plot the parabola and initial guess as an x
    fig, ax = plot_quadratic( A, B, C) # plot the parabola
    # TODO! Add the initial guess to the plot as a black "x"
    ax.plot(X0, 'kx', label='Initial guess', color='black')

    # call fsolve to find the closest root, add to plot as red circle
    #X= fsolve(eval_quadratic, X0, args=(A, B, C)) #if putting the value in parentesis it will return a float, we want the function to evaluate and work with the value
    root= fsolve(eval_quadratic, X0, args=(A, B, C)) #if putting the value in parentesis it will return a float, we want the function to evaluate and work with the value
    ax.plot(root, 0, 'ro', label='Root', mfc='none') #seethrough center facecolor='none', mfc='none'
    #print(X)
    # TODO! Call fsolve using the necessary arguments and keyword arguments
    # TODO! Add the found root to the plot as a red circle with a see-through center
    #ax.plot(X, eval_quadratic(X, A, B, C), 'ro' , label= 'Root',  facecolor='none' ) #seethrough center facecolor='none', mfc='none'
    plt.show()
