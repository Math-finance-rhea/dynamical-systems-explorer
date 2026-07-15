import numpy as np
import matplotlib.pyplot as plt


def competition_rates(x, y, r1, r2, K1, K2, alpha, beta):
    """
    Return dx/dt and dy/dt for the two-species competition model.
    """
    dx = r1 * x * (1 - (x + alpha * y) / K1)
    dy = r2 * y * (1 - (y + beta * x) / K2)

    return dx, dy


def simulate_competition(
    x0,
    y0,
    r1,
    r2,
    K1,
    K2,
    alpha,
    beta,
    dt,
    steps
):
    """
    Simulate the model using Euler's method.
    """
    x = x0
    y = y0

    x_values = [x]
    y_values = [y]

    for _ in range(steps):
        dx, dy = competition_rates(
            x,
            y,
            r1,
            r2,
            K1,
            K2,
            alpha,
            beta
        )

        x = x + dt * dx
        y = y + dt * dy

        # Prevent tiny negative values caused by numerical error
        x = max(x, 0)
        y = max(y, 0)

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


# --------------------------------------------------
# 1. Model parameters
# --------------------------------------------------

r1 = 1
r2 = 1

K1 = 100
K2 = 80

alpha = 2
beta = 1

dt = 0.01
steps = 10000


# --------------------------------------------------
# 2. Initial conditions
# --------------------------------------------------

initial_conditions = [
    (80, 5),
    (20, 10),
    (20, 30),
    (90, 40)
]


# --------------------------------------------------
# 3. Create the vector field grid
# --------------------------------------------------

x_grid = np.linspace(0, 110, 22)
y_grid = np.linspace(0, 90, 18)

X, Y = np.meshgrid(x_grid, y_grid)

DX, DY = competition_rates(
    X,
    Y,
    r1,
    r2,
    K1,
    K2,
    alpha,
    beta
)


# --------------------------------------------------
# 4. Normalize vector lengths
# --------------------------------------------------

magnitude = np.sqrt(DX**2 + DY**2)

# Avoid division by zero at equilibrium points
magnitude[magnitude == 0] = 1

DX_normalized = DX / magnitude
DY_normalized = DY / magnitude


# --------------------------------------------------
# 5. Plot vector field
# --------------------------------------------------

plt.quiver(
    X,
    Y,
    DX_normalized,
    DY_normalized,
    angles="xy"
)


# --------------------------------------------------
# 6. Plot trajectories
# --------------------------------------------------

for x0, y0 in initial_conditions:
    x_values, y_values = simulate_competition(
        x0,
        y0,
        r1,
        r2,
        K1,
        K2,
        alpha,
        beta,
        dt,
        steps
    )

    plt.plot(
        x_values,
        y_values,
        label=f"Initial: ({x0}, {y0})"
    )

    plt.scatter(
        x0,
        y0,
        marker="o"
    )

    print(
        f"Initial ({x0}, {y0}) "
        f"-> Final ({x_values[-1]:.2f}, {y_values[-1]:.2f})"
    )


# --------------------------------------------------
# 7. Plot nullclines
# --------------------------------------------------

x_line = np.linspace(0, 110, 500)

# dx/dt = 0:
# y = (K1 - x) / alpha
x_nullcline = (K1 - x_line) / alpha

# dy/dt = 0:
# y = K2 - beta*x
y_nullcline = K2 - beta * x_line

plt.plot(
    x_line,
    x_nullcline,
    linestyle="--",
    label="x-nullcline"
)

plt.plot(
    x_line,
    y_nullcline,
    linestyle="--",
    label="y-nullcline"
)


# --------------------------------------------------
# 8. Mark equilibria
# --------------------------------------------------

plt.scatter(
    0,
    0,
    marker="x",
    s=100,
    label="Equilibrium (0, 0)"
)

plt.scatter(
    K1,
    0,
    marker="x",
    s=100,
    label="Equilibrium (100, 0)"
)

plt.scatter(
    0,
    K2,
    marker="x",
    s=100,
    label="Equilibrium (0, 80)"
)

plt.scatter(
    60,
    20,
    marker="x",
    s=100,
    label="Saddle point (60, 20)"
)


# --------------------------------------------------
# 9. Labels and display
# --------------------------------------------------

plt.xlabel("Population x")
plt.ylabel("Population y")
plt.title("Competition Model Phase Portrait")

plt.xlim(0, 110)
plt.ylim(0, 90)

plt.legend(fontsize=8)
plt.grid()
plt.savefig(
    "figures/competition_phase_portrait.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()