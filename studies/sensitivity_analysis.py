import numpy as np
import matplotlib.pyplot as plt
from core.rk4 import rk4
from core.sir import SIRModel


def run_sensitivity():

    gamma = 0.1
    betas = np.linspace(0.1, 0.5, 20)

    peak_infected = []

    for beta in betas:
        model = SIRModel(beta, gamma)
        t = np.linspace(0, 100, 2000)
        y0 = np.array([999, 1, 0])
        sol = rk4(model.rhs, y0, t)
        peak_infected.append(np.max(sol[:,1]))

    plt.plot(betas, peak_infected)
    plt.xlabel("Beta")
    plt.ylabel("Peak Infected")
    plt.title("Sensitivity of Peak Infection to Beta")
    plt.savefig("sensitivity_plot.png")
    plt.show()


if __name__ == "__main__":
    run_sensitivity()
