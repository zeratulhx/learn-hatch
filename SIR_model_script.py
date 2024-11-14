import matplotlib.pyplot as plt


print('This is inside the script.')
# Inputs
# Total number of susceptible people at the start of an outbreak
pop_size = 8000000
# Average no. of new infections per infected person per day
beta = 0.5
# Inverse of the average number of days taken to recover
gamma = 0.1
# Number of days to run the simulation for
days = 150
# Number of infected people at the start of the simulation
I_0 = 10

# Initialise data
S = [] # Number of susceptible people each day
I = [] # Number of infected people each day
R = [] # Number of recovered people each day
S.append(pop_size - I_0)
I.append(I_0)
R.append(0)

# Solve model
for i in range(days):
    # Get rate of change of S, I, and R
    dS = - beta * S[i] * I[i] / pop_size
    dR = gamma * I[i]
    dI = -(dS + dR)
    # Get values on next day
    S.append(S[i] + dS)
    I.append(I[i] + dI)
    R.append(R[i] + dR)

# Plot results
plt.plot(range(len(S)), S, label="S")
plt.plot(range(len(I)), I, label="I")
plt.plot(range(len(R)), R, label="R")
plt.xlabel("Time /days")
plt.ylabel("Population")
plt.legend()
plt.show()