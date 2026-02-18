# core/analysis.py

import numpy as np
from typing import Tuple


def compute_peak_infected(solution: np.ndarray) -> Tuple[float, int]:
    """
    Returns peak infected value and its index.
    Assumes I is column 1.
    """
    I = solution[:, 1]
    idx = np.argmax(I)
    return I[idx], idx


def compute_final_size(solution: np.ndarray) -> float:
    """
    Returns final recovered population.
    Assumes R is last column.
    """
    return solution[-1, -1]


def compute_observed_order(dt_values, errors):
    """
    Computes slope of log-log error curve.
    """
    log_dt = np.log(dt_values)
    log_err = np.log(errors)
    slope, _ = np.polyfit(log_dt, log_err, 1)
    return slope
