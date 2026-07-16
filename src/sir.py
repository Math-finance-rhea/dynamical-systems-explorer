import matplotlib.pyplot as plt


# SIR model rates
def sir_rates(S, I, R, beta, gamma, N):

    dS = -beta * S * I / N

    dI = beta * S * I / N - gamma * I

    dR = gamma * I

    return dS, dI, dR


# Euler simulation
def simulate_sir(S0, I0, R0, beta, gamma, dt, steps):

    N = S0 + I0 + R0

    S = S0
    I = I0
    R = R0

    S_values = [S]
    I_values = [I]
    R_values = [R]

    for _ in range(steps):

        dS, dI, dR = sir_rates(
            S,
            I,
            R,
            beta,
            gamma,
            N
        )

        S = S + dt * dS
        I = I + dt * dI
        R = R + dt * dR

        S_values.append(S)
        I_values.append(I)
        R_values.append(R)

    return S_values, I_values, R_values


# Parameters
S0 = 990
I0 = 10
R0 = 0

gamma = 0.1

dt = 0.1
steps = 500

betas = [0.1, 0.2, 0.3, 0.4, 0.5]
time = [i * dt for i in range(steps + 1)]
for beta in betas:

    S, I, R = simulate_sir(
        S0,
        I0,
        R0,
        beta,
        gamma,
        dt,
        steps
    )

    plt.plot(time,I, label=f"β={beta}")


#plt.plot(S, label="Susceptible (S)")
#plt.plot(I, label="Infected (I)")
#plt.plot(R, label="Recovered (R)")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("SIR Epidemic Model")

plt.legend()
plt.grid()
plt.savefig(
    "figures/sir_model.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()