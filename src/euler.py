"""
Project: Dynamical Systems Explorer

Research Log 01
Topic: Epidemic Growth Model

Author: Xirui Gong
"""
from pathlib import Path
import matplotlib.pyplot as plt

def logistic_rate(P: float, r: float, K: float) -> float:
    """
    Compute the growth rate of the logistic model.

    Parameters
    ----------
    P : float
        Current population.

    r : float
        Growth rate.

    K : float
        Carrying capacity.

    Returns
    -------
    float
        Growth rate dP/dt.
    """
    return r * P * (1 - P / K)
P = 100
r = 0.8
K = 1000
dt = 0.1

growth = logistic_rate(P, r, K)
def simulate_logistic(P0: float, r: float, K: float, dt: float, steps: int):
    """
    Simulate logistic growth using Euler's method.
    """
    P = P0
    populations = [P]

    print(f"Step 0: Population = {P:.2f}")

    for step in range(steps):
        growth = logistic_rate(P, r, K)
        P = P + dt * growth
        populations.append(P)

        print(f"Step {step + 1}: Population = {P:.2f}")

    return populations

initial_conditions = [10, 100, 500, 1200]

for P0 in initial_conditions:
    results = simulate_logistic(
        P0=P0,
        r=0.8,
        K=1000,
        dt=0.1,
        steps=300
    )

    plt.plot(results, label=f"P0 = {P0}")

plt.title("Logistic Growth Model")
plt.xlabel("Step")
plt.ylabel("Population")
plt.legend()
output_path = Path(__file__).parent.parent / "figures" / "logistic_growth.png"

plt.savefig(output_path, dpi=300, bbox_inches="tight")

print(f"Figure saved to: {output_path}")
plt.show()

