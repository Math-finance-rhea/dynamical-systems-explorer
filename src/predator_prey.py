import matplotlib.pyplot as plt
import numpy as np


def predator_prey_rates(x, y, a, b, c, d):
    dx = a * x - b * x * y
    dy = -c * y + d * x * y
    return dx, dy


def simulate_predator_prey(x0, y0, a, b, c, d, dt, steps):
    x = x0
    y = y0

    rabbits = [x]
    foxes = [y]

    for step in range(steps):
        dx, dy = predator_prey_rates(x, y, a, b, c, d)

        x = x + dt * dx
        y = y + dt * dy

        rabbits.append(x)
        foxes.append(y)

    return rabbits, foxes


a = 1
b = 0.1
c = 1.5
d = 0.075

rabbits, foxes = simulate_predator_prey(
    x0=21,
    y0=10,
    a=a,
    b=b,
    c=c,
    d=d,
    dt=0.01,
    steps=2000
)
#plt.plot(rabbits, label="Rabbits")
#plt.plot(foxes, label="Foxes")
# Create a grid of points in the phase plane
X, Y = np.meshgrid(
    np.linspace(0, 40, 15),
    np.linspace(0, 20, 15)
)

# Calculate the direction of the vector field
DX = a * X - b * X * Y
DY = -c * Y + d * X * Y

# Normalize the arrows so they are easier to see
length = np.sqrt(DX**2 + DY**2)

DX_normalized = np.divide(
    DX,
    length,
    out=np.zeros_like(DX),
    where=length != 0
)

DY_normalized = np.divide(
    DY,
    length,
    out=np.zeros_like(DY),
    where=length != 0
)

# Draw the vector field
plt.quiver(
    X,
    Y,
    DX_normalized,
    DY_normalized,
    alpha=0.5
)

# Draw the trajectory
plt.plot(rabbits, foxes, label="Trajectory")

# Mark the coexistence equilibrium
equilibrium_x = c / d
equilibrium_y = a / b

plt.scatter(equilibrium_x, equilibrium_y)
plt.text(
    equilibrium_x,
    equilibrium_y,
    " equilibrium"
)

plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Predator-Prey Phase Portrait")
plt.legend()

plt.savefig(
    "figures/predator_prey_phase_portrait.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()