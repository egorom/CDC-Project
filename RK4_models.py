"""
RK4_models.py
-------------

Modular Runge–Kutta (4th order) solvers for compartmental epidemic models.

Implements:
    - SIR
    - SIR with demography
    - SEIR
    - SEIR with demography

All models assume normalized population (S + I + R = 1, etc.).
"""

import numpy as np


# ============================================================
# Generic RK4 Integrator
# ============================================================

def rk4_system(f, y0, t, params):
    """
    Generic 4th-order Runge-Kutta integrator for systems of ODEs.

    Parameters
    ----------
    f : function
        Function defining system dy/dt = f(y, t, params)
    y0 : array_like
        Initial condition vector
    t : array_like
        Time grid
    params : dict
        Model parameters

    Returns
    -------
    y : ndarray
        Solution array of shape (len(t), len(y0))
    """

    y0 = np.asarray(y0, dtype=float)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    dt = t[1] - t[0]

    for n in range(len(t) - 1):
        k1 = f(y[n], t[n], params)
        k2 = f(y[n] + 0.5 * dt * k1, t[n] + 0.5 * dt, params)
        k3 = f(y[n] + 0.5 * dt * k2, t[n] + 0.5 * dt, params)
        k4 = f(y[n] + dt * k3, t[n] + dt, params)

        y[n + 1] = y[n] + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return y


# ============================================================
# SIR Models
# ============================================================

def sir_rhs(y, t, params):
    """
    Right-hand side of classic SIR model.
    """
    S, I, R = y
    beta = params["beta"]
    gamma = params["gamma"]

    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I

    return np.array([dS, dI, dR])


def sir_demography_rhs(y, t, params):
    """
    SIR model with vital dynamics (birth/death rate mu).
    """
    S, I, R = y
    beta = params["beta"]
    gamma = params["gamma"]
    mu = params["mu"]

    dS = mu - beta * S * I - mu * S
    dI = beta * S * I - gamma * I - mu * I
    dR = gamma * I - mu * R

    return np.array([dS, dI, dR])


def solve_sir(beta, gamma, S0, I0, R0, t, mu=None):
    """
    Solve SIR model (with optional demography).
    """

    y0 = [S0, I0, R0]

    params = {
        "beta": beta,
        "gamma": gamma
    }

    if mu is not None:
        params["mu"] = mu
        sol = rk4_system(sir_demography_rhs, y0, t, params)
    else:
        sol = rk4_system(sir_rhs, y0, t, params)

    return sol


# ============================================================
# SEIR Models
# ============================================================

def seir_rhs(y, t, params):
    """
    Classic SEIR model (no demography).
    """
    S, E, I, R = y
    beta = params["beta"]
    gamma = params["gamma"]
    sigma = params["sigma"]

    dS = -beta * S * I
    dE = beta * S * I - sigma * E
    dI = sigma * E - gamma * I
    dR = gamma * I

    return np.array([dS, dE, dI, dR])


def seir_demography_rhs(y, t, params):
    """
    SEIR model with vital dynamics.
    """
    S, E, I, R = y
    beta = params["beta"]
    gamma = params["gamma"]
    sigma = params["sigma"]
    mu = params["mu"]

    dS = mu - beta * S * I - mu * S
    dE = beta * S * I - sigma * E - mu * E
    dI = sigma * E - gamma * I - mu * I
    dR = gamma * I - mu * R

    return np.array([dS, dE, dI, dR])


def solve_seir(beta, gamma, sigma, S0, E0, I0, R0, t, mu=None):
    """
    Solve SEIR model (with optional demography).
    """

    y0 = [S0, E0, I0, R0]

    params = {
        "beta": beta,
        "gamma": gamma,
        "sigma": sigma
    }

    if mu is not None:
        params["mu"] = mu
        sol = rk4_system(seir_demography_rhs, y0, t, params)
    else:
        sol = rk4_system(seir_rhs, y0, t, params)

    return sol
