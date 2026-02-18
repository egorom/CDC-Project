"""
sir_gui.py
----------

Interactive epidemic modeling tool using SIR and SEIR models
with optional demographic effects.

Backend: RK4_models.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

from RK4_models import solve_sir, solve_seir


class EpidemicApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Epidemic Modeling Tool")

        self._build_ui()

    # ============================================================
    # UI CONSTRUCTION
    # ============================================================

    def _build_ui(self):

        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)

        # -------- Model Selection --------
        model_frame = ttk.LabelFrame(main, text="Model Selection", padding=10)
        model_frame.pack(fill="x", pady=5)

        self.model_type = tk.StringVar(value="SIR")
        ttk.Radiobutton(model_frame, text="SIR", variable=self.model_type,
                        value="SIR").pack(side="left", padx=5)
        ttk.Radiobutton(model_frame, text="SEIR", variable=self.model_type,
                        value="SEIR").pack(side="left", padx=5)

        self.use_demography = tk.BooleanVar()
        ttk.Checkbutton(model_frame, text="Include Demography (μ)",
                        variable=self.use_demography).pack(side="left", padx=10)

        # -------- Parameters --------
        param_frame = ttk.LabelFrame(main, text="Parameters", padding=10)
        param_frame.pack(fill="x", pady=5)

        self.entries = {}

        params = [
            ("β (Transmission)", "0.3"),
            ("γ (Recovery)", "0.1"),
            ("σ (Incubation, SEIR only)", "0.2"),
            ("μ (Birth/Death rate)", "0.01"),
            ("S₀", "0.99"),
            ("E₀", "0.0"),
            ("I₀", "0.01"),
            ("R₀", "0.0"),
            ("Simulation Time", "160"),
            ("Time Step", "0.1")
        ]

        for label, default in params:
            row = ttk.Frame(param_frame)
            row.pack(fill="x", pady=2)
            ttk.Label(row, text=label, width=30).pack(side="left")
            entry = ttk.Entry(row)
            entry.insert(0, default)
            entry.pack(side="right", fill="x", expand=True)
            self.entries[label] = entry

        # -------- Controls --------
        control_frame = ttk.Frame(main)
        control_frame.pack(pady=10)

        ttk.Button(control_frame, text="Run Simulation",
                   command=self.run_simulation).pack(side="left", padx=5)

        ttk.Button(control_frame, text="Clear Plot",
                   command=self.clear_plot).pack(side="left", padx=5)

        # -------- Analysis Panel --------
        self.analysis_label = ttk.Label(main, text="", justify="left")
        self.analysis_label.pack(pady=5)

    # ============================================================
    # SIMULATION LOGIC
    # ============================================================

    def run_simulation(self):

        try:
            params = self._collect_inputs()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        t = np.arange(0, params["T"], params["dt"])

        if self.model_type.get() == "SIR":
            sol = solve_sir(
                params["beta"],
                params["gamma"],
                params["S0"],
                params["I0"],
                params["R0"],
                t,
                mu=params["mu"] if self.use_demography.get() else None
            )
            S, I, R = sol.T
            self._plot_results(t, S, I, R)

            R0_value = self._compute_R0(
                params["beta"],
                params["gamma"],
                params["mu"] if self.use_demography.get() else None
            )

        else:  # SEIR
            sol = solve_seir(
                params["beta"],
                params["gamma"],
                params["sigma"],
                params["S0"],
                params["E0"],
                params["I0"],
                params["R0"],
                t,
                mu=params["mu"] if self.use_demography.get() else None
            )
            S, E, I, R = sol.T
            self._plot_results(t, S, I, R, E)

            R0_value = self._compute_R0(
                params["beta"],
                params["gamma"],
                params["mu"] if self.use_demography.get() else None
            )

        self._update_analysis(t, I, R0_value)

    # ============================================================
    # HELPERS
    # ============================================================

    def _collect_inputs(self):

        beta = float(self.entries["β (Transmission)"].get())
        gamma = float(self.entries["γ (Recovery)"].get())
        sigma = float(self.entries["σ (Incubation, SEIR only)"].get())
        mu = float(self.entries["μ (Birth/Death rate)"].get())
        S0 = float(self.entries["S₀"].get())
        E0 = float(self.entries["E₀"].get())
        I0 = float(self.entries["I₀"].get())
        R0 = float(self.entries["R₀"].get())
        T = float(self.entries["Simulation Time"].get())
        dt = float(self.entries["Time Step"].get())

        if dt <= 0 or T <= 0:
            raise ValueError("Simulation time and time step must be positive.")

        return {
            "beta": beta,
            "gamma": gamma,
            "sigma": sigma,
            "mu": mu,
            "S0": S0,
            "E0": E0,
            "I0": I0,
            "R0": R0,
            "T": T,
            "dt": dt
        }

    def _compute_R0(self, beta, gamma, mu=None):
        if mu is None:
            return beta / gamma
        return beta / (gamma + mu)

    def _plot_results(self, t, S, I, R, E=None):

        plt.figure()
        plt.plot(t, S, label="Susceptible")
        if E is not None:
            plt.plot(t, E, label="Exposed")
        plt.plot(t, I, label="Infected")
        plt.plot(t, R, label="Recovered")

        plt.xlabel("Time")
        plt.ylabel("Population Fraction")
        plt.title(f"{self.model_type.get()} Model Simulation")
        plt.legend()
        plt.grid(True)
        plt.show()

    def _update_analysis(self, t, I, R0_value):

        peak_I = np.max(I)
        peak_time = t[np.argmax(I)]
        total_infected = np.trapz(I, t)

        summary = (
            f"Basic Reproduction Number (R₀): {R0_value:.3f}\n"
            f"Peak Infection: {peak_I:.3f}\n"
            f"Time of Peak: {peak_time:.2f}\n"
            f"Total Infection Burden (AUC): {total_infected:.3f}"
        )

        self.analysis_label.config(text=summary)

    def clear_plot(self):
        plt.close("all")
        self.analysis_label.config(text="")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = EpidemicApp(root)
    root.mainloop()
