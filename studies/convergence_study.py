import numpy as np
import matplotlib.pyplot as plt
from core.rk4 import rk4
from core.sir import SIRModel


def run_convergence():

    beta = 0.3
    gamma = 0.1
    model = SIRModel(beta, gamma)

    T = 60
    y0 = np.array([999, 1, 0])

    dt_values = [1.0, 0.5, 0.25, 0.125]
    errors = []

    t_ref = np.linspace(0, T, 20000)
    y_ref = rk4(model.rhs, y0, t_ref)

    for dt in dt_values:
        t = np.arange(0, T, dt)
        y = rk4(model.rhs, y0, t)

        ref_interp = np.interp(t, t_ref, y_ref[:,1])
        error = np.linalg.norm(y[:,1] - ref_interp, ord=np.inf)
        errors.append(error)

    plt.loglog(dt_values, errors, 'o-')
    plt.xlabel("dt")
    plt.ylabel("Max Error")
    plt.title("RK4 Convergence Study")
    plt.savefig("convergence_plot.png")
    plt.show()


if __name__ == "__main__":
    run_convergence()
