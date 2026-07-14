import numpy as np
import matplotlib.pyplot as plt


# Parameters
K1 = 100
K2 = 80
alpha = 2
beta = 1


# x-values for plotting
x = np.linspace(0, 120, 500)


# Nullclines
x_nullcline = (K1 - x) / alpha
y_nullcline = K2 - beta * x


# Plot the two non-axis nullclines
plt.plot(
    x,
    x_nullcline,
    label=r"$dx/dt = 0$: $y=(K_1-x)/\alpha$"
)

plt.plot(
    x,
    y_nullcline,
    label=r"$dy/dt = 0$: $y=K_2-\beta x$"
)


# The other two nullclines are the axes:
# x = 0 and y = 0
plt.axvline(0, linestyle="--", label=r"$x=0$")
plt.axhline(0, linestyle="--", label=r"$y=0$")


plt.xlim(0, 120)
plt.ylim(0, 100)

plt.xlabel("Population x")
plt.ylabel("Population y")
plt.title("Competition Model Nullclines")

plt.legend()
plt.grid()
plt.show()