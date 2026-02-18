# Numerical Epidemiology Framework

An epidemiological modeling framework using a verified fourth-order Runge–Kutta (RK4) solver.

This project demonstrates:

- High-order numerical ODE integration
- SIR and SEIR epidemic modeling
- Sensitivity and convergence analysis
- Linear stability analysis
- Phase portrait visualization
- Vaccination modeling
- Unit testing and production-grade architecture

---

## Mathematical Models

### SIR Model

dS/dt = -β S I / N - v S

dI/dt = β S I / N - γ I

dR/dt = γ I + v S

Where:
- β = infection rate
- γ = recovery rate
- v = vaccination rate
- R₀ = β / γ

---

### SEIR Model

dS/dt = -β S I / N
dE/dt = β S I / N - σ E
dI/dt = σ E - γ I
dR/dt = γ I

---

## Numerical Method

The system is solved using a fourth-order Runge–Kutta (RK4) integrator:

y_{n+1} = y_n + (1/6)*(k1 + 2*k2 + 2*k3 + k4)


A convergence study verifies fourth-order accuracy.

---

## Features

### Verified Numerical Accuracy
- Log-log convergence study
- Observed order ≈ 4

### Sensitivity Analysis
- Peak infection vs β
- Time-to-peak analysis

### R₀ Analysis
- Epidemic threshold behavior
- Final epidemic size vs R₀

### Stability Study
- Time step sensitivity
- Numerical stability exploration

### Phase Portraits
- S vs I trajectory visualization

### Linear Stability
- Jacobian evaluation
- Eigenvalue analysis

### Vaccination Modeling
- Optional vaccination term in SIR

---

## Project Structure

```
core/          # Numerical solvers and model definitions
studies/       # Reproducible numerical experiments
tests/         # Unit tests
sir_gui.py     # Interactive GUI
```

---


## Running the Studies

```
python studies/convergence_study.py
python studies/sensitivity_analysis.py
python studies/r0_analysis.py
python studies/stability_study.py
python studies/phase_portrait.py
```

---

## Running the GUI

```
python sir_gui.py
```

---

## Testing

```
pytest tests/
```

---

## Requirements

- Python 3.9+
- NumPy
- Matplotlib
- PyTest

Install with:

```
pip install -r requirements.txt
```

---

## Engineering Highlights

- Modular architecture
- Separation of concerns
- Type hints
- Input validation
- Numerical verification
- Research-style reproducibility

---

## Applications

- Epidemiological modeling
- Dynamical systems research
- Numerical methods verification
- Scientific computing education
- Parameter sensitivity analysis
