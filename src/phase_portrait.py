import numpy as np
import matplotlib.pyplot as plt

r = 0.8
K = 1000

P = np.linspace(-100, 1500, 500)

f = r * P * (1 - P / K)

plt.plot(P, f)

plt.xlabel("P")
plt.ylabel("dP/dt")
plt.title("Logistic Growth Function")

plt.axhline(0)
plt.axvline(0, linestyle="--")
plt.axvline(K, linestyle="--")
plt.text(0, 50, "P=0")

plt.text(K, 50, "P=K")
plt.show()