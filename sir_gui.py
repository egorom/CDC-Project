import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

from core.rk4 import rk4
from core.sir import SIRModel
from core.seir import SEIRModel


class EpidemicGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Epidemic Modeling Framework")

        self._build_inputs()
        self._build_buttons()

    # -------------------------------------------------
    # UI Construction
    # -------------------------------------------------

    def _build_inputs(self):

        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0)

        ttk.Label(frame, text="Model Type").grid(row=0, column=0)
        self.model_type = ttk.Combobox(
            frame, values=["SIR", "SEIR"], state="readonly"
        )
        self.model_type.set("SIR")
        self.model_type.grid(row=0, column=1)

        labels = ["Beta", "Gamma", "Sigma (SEIR)", "Vaccination Rate"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=i+1, column=0)
            entry = ttk.Entry(frame)
            entry.insert(0, "0.1")
            entry.grid(row=i+1, column=1)
            self.entries[label] = entry

        ttk.Label(frame, text="Initial S").grid(row=5, column=0)
        self.S0 = ttk.Entry(frame)
        self.S0.insert(0, "999")
        self.S0.grid(row=5, column=1)

        ttk.Label(frame, text="Initial I").grid(row=6, column=0)
        self.I0 = ttk.Entry(frame)
        self.I0.insert(0, "1")
        self.I0.grid(row=6, column=1)

        ttk.Label(frame, text="Initial R").grid(row=7, column=0)
        self.R0 = ttk.Entry(frame)
        self.R0.insert(0, "0")
        self.R0.grid(row=7, column=1)

    def _build_buttons(self):

        ttk.Button(self.root, text="Run Simulation",
                   command=self.run_simulation).grid(row=1, column=0, pady=10)

    # -------------------------------------------------
    # Simulation
    # -------------------------------------------------

    def run_simulation(self):

        try:
            beta = float(self.entries["Beta"].get())
            gamma = float(self.entries["Gamma"].get())
            sigma = float(self.entries["Sigma (SEIR)"].get())
            v = float(self.entries["Vaccination Rate"].get())

            S0 = float(self.S0.get())
            I0 = float(self.I0.get())
            R0_val = float(self.R0.get())

        except ValueError:
            messagebox.showerror("Input Error", "All inputs must be numeric.")
            return

        t = np.linspace(0, 160, 2000)

        if self.model_type.get() == "SIR":

            model = SIRModel(beta, gamma, v)
            y0 = np.array([S0, I0, R0_val])
            sol = rk4(model.rhs, y0, t)

            self._plot_sir(t, sol, model.R0())

        else:

            model = SEIRModel(beta, gamma, sigma)
            y0 = np.array([S0, 0, I0, R0_val])
            sol = rk4(model.rhs, y0, t)

            self._plot_seir(t, sol)

    # -------------------------------------------------
    # Plotting
    # -------------------------------------------------

    def _plot_sir(self, t, sol, R0):

        plt.figure()
        plt.plot(t, sol[:, 0], label="S")
        plt.plot(t, sol[:, 1], label="I")
        plt.plot(t, sol[:, 2], label="R")
        plt.title(f"SIR Model (R0 = {R0:.2f})")
        plt.legend()
        plt.show()

    def _plot_seir(self, t, sol):

        plt.figure()
        plt.plot(t, sol[:, 0], label="S")
        plt.plot(t, sol[:, 1], label="E")
        plt.plot(t, sol[:, 2], label="I")
        plt.plot(t, sol[:, 3], label="R")
        plt.title("SEIR Model")
        plt.legend()
        plt.show()


# -----------------------------------------------------
# Main
# -----------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = EpidemicGUI(root)
    root.mainloop()
