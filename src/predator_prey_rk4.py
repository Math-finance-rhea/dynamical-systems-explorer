import numpy as np
import matplotlib.pyplot as plt


def predator_prey_rates(x, y, a, b, c, d):
    """
    Lotka-Volterra predator-prey model.

    x: rabbits
    y: foxes
    """
    dx = a * x - b * x * y
    dy = -c * y + d * x * y

    return dx, dy


def simulate_euler(x0, y0, a, b, c, d, dt, steps):
    """
    Simulate the predator-prey system using Euler's method.
    """
    x = x0
    y = y0

    rabbits = [x]
    foxes = [y]

    for _ in range(steps):
        dx, dy = predator_prey_rates(x, y, a, b, c, d)

        x = x + dt * dx
        y = y + dt * dy

        rabbits.append(x)
        foxes.append(y)

    return rabbits, foxes


def simulate_rk4(x0, y0, a, b, c, d, dt, steps):
    """
    Simulate the predator-prey system using RK4.
    """
    x = x0
    y = y0

    rabbits = [x]
    foxes = [y]

    for _ in range(steps):
        # First slope: start of the step
        k1x, k1y = predator_prey_rates(x, y, a, b, c, d)

        # Second slope: midpoint using k1
        k2x, k2y = predator_prey_rates(
            x + 0.5 * dt * k1x,
            y + 0.5 * dt * k1y,
            a,
            b,
            c,
            d
        )

        # Third slope: midpoint using k2
        k3x, k3y = predator_prey_rates(
            x + 0.5 * dt * k2x,
            y + 0.5 * dt * k2y,
            a,
            b,
            c,
            d
        )

        # Fourth slope: end of the step using k3
        k4x, k4y = predator_prey_rates(
            x + dt * k3x,
            y + dt * k3y,
            a,
            b,
            c,
            d
        )

        # Weighted average of the four slopes
        x = x + (dt / 6) * (
            k1x + 2 * k2x + 2 * k3x + k4x
        )

        y = y + (dt / 6) * (
            k1y + 2 * k2y + 2 * k3y + k4y
        )

        rabbits.append(x)
        foxes.append(y)

    return rabbits, foxes


# Model parameters
a = 1
b = 0.1
c = 1.5
d = 0.075

# Initial condition
x0 = 21
y0 = 10

# Numerical settings
dt = 0.01
steps = 10000


# Run Euler simulation
rabbits_euler, foxes_euler = simulate_euler(
    x0=x0,
    y0=y0,
    a=a,
    b=b,
    c=c,
    d=d,
    dt=dt,
    steps=steps
)


# Run RK4 simulation
rabbits_rk4, foxes_rk4 = simulate_rk4(
    x0=x0,
    y0=y0,
    a=a,
    b=b,
    c=c,
    d=d,
    dt=dt,
    steps=steps
)


# Calculate the coexistence equilibrium
equilibrium_x = c / d
equilibrium_y = a / b


# Plot both phase-plane trajectories
plt.plot(
    rabbits_euler,
    foxes_euler,
    label="Euler"
)

plt.plot(
    rabbits_rk4,
    foxes_rk4,
    label="RK4"
)

# Mark the equilibrium
plt.scatter(
    equilibrium_x,
    equilibrium_y,
    label="Equilibrium"
)

plt.text(
    equilibrium_x,
    equilibrium_y,
    "  equilibrium"
)

plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Euler vs RK4: Predator-Prey Phase Plane")
plt.legend()
plt.grid()

plt.show()