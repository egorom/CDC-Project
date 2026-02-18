import numpy as np


def sir_jacobian(beta, gamma, S, I, R):

    N = S + I + R

    J = np.array([
        [-beta*I/N, -beta*S/N, 0],
        [beta*I/N, beta*S/N - gamma, 0],
        [0, gamma, 0]
    ])

    return J


def eigenvalues(J):
    return np.linalg.eigvals(J)
