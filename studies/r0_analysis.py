import numpy as np
import matplotlib.pyplot as plt
from core.rk4 import rk4
from core.sir import SIRModel


def run_r0_analysis():

    gamma = 0.1
    betas = np.linspace(0.05, 0.3, 25)

    epidemic_sizes = []
    r0_values = []

    for beta in betas:
        model = SIRModel(beta, gamma)
        t = np.linspace(0, 200, 4000)
        y0 = np.array([999, 1, 0])
        sol = rk4(model.rhs, y0, t)

        epidemic_sizes.append(sol[-1, 2])  # final R
        r0_values.append(model.R0())

    plt.plot(r0_values, epidemic_sizes)
    plt.axvline(1.0, linestyle="--", label="R0 = 1")
    plt.xlabel("R0")
    plt.ylabel("Final Epidemic Size")
    plt.title("Epidemic Size vs R0")
    plt.legend()
    plt.savefig("r0_analysis.png")
    plt.show()


if __name__ == "__main__":
    run_r0_analysis()
