import numpy as np
import matplotlib.pyplot as plt
from core.rk4 import rk4
from core.sir import SIRModel


def run_phase_portrait():

    model = SIRModel(0.3, 0.1)
    t = np.linspace(0, 100, 2000)
    y0 = np.array([999, 1, 0])
    sol = rk4(model.rhs, y0, t)

    plt.plot(sol[:,0], sol[:,1])
    plt.xlabel("S")
    plt.ylabel("I")
    plt.title("Phase Portrait (S vs I)")
    plt.savefig("phase_portrait.png")
    plt.show()


if __name__ == "__main__":
    run_phase_portrait()
