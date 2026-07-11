import matplotlib.pyplot as plt


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


rabbits, foxes = simulate_predator_prey(
    x0=40,
    y0=9,
    a=1,
    b=0.1,
    c=1.5,
    d=0.075,
    dt=0.01,
    steps=2000
)

plt.plot(rabbits, label="Rabbits")
plt.plot(foxes, label="Foxes")
plt.plot(rabbits, foxes)
plt.scatter(c / d, a / b)
plt.text(c / d, a / b, " equilibrium")
plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Phase Plane")

plt.show()