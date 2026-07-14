import matplotlib.pyplot as plt


def competition_rates(x, y, r1, r2, K1, K2, alpha, beta):
    """
    Calculate the rates of change for the two competing species.
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
    Simulate the competition model using Euler's method.
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

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Model parameters
r1 = 1
r2 = 1

K1 = 100
K2 = 80

alpha = 2
beta = 1

dt = 0.01
steps = 10000


# Try several initial conditions
initial_conditions = [
    (80, 5),
    (20, 10),
    (20, 30),
    (90, 40)
]


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

    # Plot the trajectory
    plt.plot(
        x_values,
        y_values,
        label=f"Initial: ({x0}, {y0})"
    )

    # Mark the starting point
    plt.scatter(
        x_values[0],
        y_values[0]
    )

    # Print the final populations
    print(
        f"Initial ({x0}, {y0}) "
        f"-> Final ({x_values[-1]:.2f}, {y_values[-1]:.2f})"
    )


# Mark the three important equilibria
plt.scatter(
    100,
    0,
    marker="x",
    s=100,
    label="Equilibrium (100, 0)"
)

plt.scatter(
    0,
    80,
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


# Draw the nullclines
x_line = [i for i in range(101)]

x_nullcline = [
    (K1 - x) / alpha
    for x in x_line
]

y_nullcline = [
    K2 - beta * x
    for x in x_line
]

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


plt.xlabel("Population x")
plt.ylabel("Population y")
plt.title("Competition Model Phase Portrait")

plt.xlim(0, 110)
plt.ylim(0, 90)

plt.legend()
plt.grid()

plt.show()

