# core/sir.py

import numpy as np


class SIRModel:
    def __init__(self, beta: float, gamma: float, vaccination_rate: float = 0.0):
        if beta < 0 or gamma < 0 or vaccination_rate < 0:
            raise ValueError("Parameters must be non-negative.")

        self.beta = beta
        self.gamma = gamma
        self.v = vaccination_rate

    def rhs(self, t: float, y: np.ndarray) -> np.ndarray:
        S, I, R = y
        N = S + I + R

        dS = -self.beta * S * I / N - self.v * S
        dI = self.beta * S * I / N - self.gamma * I
        dR = self.gamma * I + self.v * S

        return np.array([dS, dI, dR])

    def R0(self) -> float:
        return self.beta / self.gamma
