"""
Project: Dynamical Systems Explorer

Research Log 01
Topic: Epidemic Growth Model

Author: Xirui Gong
"""
print("Hello, Dynamical Systems!")

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
print(logistic_rate(100, 0.8, 1000))