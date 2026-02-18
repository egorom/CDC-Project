import numpy as np
import matplotlib.pyplot as plt
from core.rk4 import rk4
from core.sir import SIRModel


def run_stability():

    beta = 0.3
    gamma = 0.1
    model = SIRModel(beta, gamma)
    y0 = np.array([999, 1, 0])

    dt_values = [5.0, 1.0, 0.1]

    for dt in dt_values:
        t = np.arange(0, 100, dt)
        sol = rk4(model.rhs, y0, t)
        plt.plot(t, sol[:,1], label=f"dt={dt}")

    plt.legend()
    plt.title("Time Step Stability Study")
    plt.savefig("stability_plot.png")
    plt.show()


if __name__ == "__main__":
    run_stability()
