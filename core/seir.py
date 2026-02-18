# core/seir.py

import numpy as np


class SEIRModel:
    def __init__(self, beta: float, gamma: float, sigma: float):
        if min(beta, gamma, sigma) < 0:
            raise ValueError("Parameters must be non-negative.")

        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma

    def rhs(self, t: float, y: np.ndarray) -> np.ndarray:
        S, E, I, R = y
        N = S + E + I + R

        dS = -self.beta * S * I / N
        dE = self.beta * S * I / N - self.sigma * E
        dI = self.sigma * E - self.gamma * I
        dR = self.gamma * I

        return np.array([dS, dE, dI, dR])
