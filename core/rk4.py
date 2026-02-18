# core/rk4.py

from typing import Callable
import numpy as np


def rk4(
    f: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    t: np.ndarray
) -> np.ndarray:
    """
    Fourth-order Runge-Kutta ODE solver.

    Parameters
    ----------
    f : function
        RHS function f(t, y)
    y0 : ndarray
        Initial condition
    t : ndarray
        Time grid (uniformly spaced)

    Returns
    -------
    ndarray
        Solution array of shape (len(t), len(y0))
    """

    if np.any(np.diff(t) <= 0):
        raise ValueError("Time grid must be strictly increasing.")

    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    for n in range(len(t) - 1):
        dt = t[n+1] - t[n]

        k1 = f(t[n], y[n])
        k2 = f(t[n] + dt/2, y[n] + dt*k1/2)
        k3 = f(t[n] + dt/2, y[n] + dt*k2/2)
        k4 = f(t[n] + dt, y[n] + dt*k3)

        y[n+1] = y[n] + dt/6 * (k1 + 2*k2 + 2*k3 + k4)

    return y
