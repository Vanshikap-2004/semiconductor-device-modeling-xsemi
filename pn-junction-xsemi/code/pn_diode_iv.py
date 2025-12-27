import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19       # Charge (C)
k = 1.38e-23      # Boltzmann constant (J/K)
T = 300           # Temperature (K)

# Device parameters (use your calculated Is)
Is = Is = 1.047e-17      # Replace with value from your PDF
V = np.linspace(0, 1, 200)

# Ideal diode equation
I = Is * (np.exp(q * V / (k * T)) - 1)

# Plot
plt.plot(V, I)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("I–V Characteristics of PN Junction (300 K)")
plt.grid(True)
plt.show()
