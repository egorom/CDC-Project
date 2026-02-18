import numpy as np
from core.rk4 import rk4


def test_exponential():

    def f(t, y):
        return y

    y0 = np.array([1.0])
    t = np.linspace(0, 1, 1000)

    sol = rk4(f, y0, t)

    exact = np.exp(1)
    error = abs(sol[-1,0] - exact)

    assert error < 1e-5
