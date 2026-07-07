# Mathematical Systems Explorer
Author: Xirui Gong


This project marks the first step of my journey into computational modelling. I hope each future project will build upon what I learn here.


A Python project exploring how mathematics can be used to model, understand and predict real-world systems.

## Project Overview

This project combines ordinary differential equations (ODEs), numerical methods and data visualisation to study real-world phenomena.

The goal is to bridge mathematics, programming and computational modelling through interactive simulations.

## Modules

### 1. Epidemic Spread

Question:

How quickly can a disease spread under different transmission rates?

Topics:

- Exponential growth
- Euler's method
- Error analysis

### 2. Investment Growth

Question:

How does wealth evolve under different interest rates?

Topics:

- Continuous growth models
- Numerical approximation
- Long-term behaviour

### 3. Predator-Prey Dynamics

Question:

How do interacting species evolve over time?

Topics:

- Dynamical systems
- Phase portraits
- Stability analysis

## Skills Demonstrated

- Python
- Mathematical modelling
- Numerical methods
- Data visualisation
- Dynamical systems

## Future Improvements

- Interactive user interface
- Adjustable parameters
- Real-world datasets

## Research Notes

Experiment 1: Effect of Growth Rate

Three simulations were performed with different growth rates
(r = 0.2, 0.8, 1.5).

Observation:
- Larger values of r lead to faster population growth.
- Smaller values of r lead to slower population growth.
- All simulations approach the same equilibrium value K = 1000.

Conclusion:
The growth rate r controls how quickly the system approaches equilibrium,
while the carrying capacity K determines the long-term population level.


## Stability Analysis

For the logistic equation

dP/dt = rP(1 - P/K),

the equilibria are:

- P = 0 (unstable)
- P = K (stable)

The simulations confirm that solutions with positive initial conditions converge to the stable equilibrium P = K.