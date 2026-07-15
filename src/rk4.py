def f(x):
    return x


def euler_step(x, dt):
    return x + dt * f(x)


def rk4_step(x, dt):

    k1 = f(x)

    k2 = f(x + 0.5 * dt * k1)

    k3 = f(x + 0.5 * dt * k2)

    k4 = f(x + dt * k3)

    return x + (dt / 6) * (
        k1
        + 2 * k2
        + 2 * k3
        + k4
    )


x_euler = 1
x_rk4 = 1

dt = 0.1

print("Step | Euler      | RK4")
print("-" * 30)

for i in range(10):

    x_euler = euler_step(x_euler, dt)

    x_rk4 = rk4_step(x_rk4, dt)

    print(
        f"{i+1:>4} | "
        f"{x_euler:>10.6f} | "
        f"{x_rk4:>10.6f}"
    )