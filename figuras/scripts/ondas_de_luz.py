
import numpy as np
import matplotlib.pyplot as plt

# Speed of light (m/s)
c = 299792458

# ==========================================
# WAVE CONFIGURATION
# Add or remove waves as needed
# ==========================================

waves = [
    {"wavelength": 660, "amplitude": 1.0, "phase": 0},
    # {"wavelength": 550, "amplitude": 0.5, "phase": 0},
    # {"wavelength": 450, "amplitude": 0.7, "phase": np.pi / 2},
]

# Number of periods of the slowest wave to display
cycles = 5

# ==========================================
# CALCULATIONS
# ==========================================

frequencies = [c / (w["wavelength"] * 1e-9) for w in waves]

# Time range based on the lowest frequency
t_max = cycles / min(frequencies)
t = np.linspace(0, t_max, 3000)

individual_waves = []
total_wave = np.zeros_like(t)

for w, nu in zip(waves, frequencies):

    amplitude = w["amplitude"]
    phase = w["phase"]

    # Wave equation at fixed r:
    # u(r,t) = a(r) cos(2*pi*nu*t + phi(r))

    u = amplitude * np.cos(2 * np.pi * nu * t + phase)

    individual_waves.append(u)
    total_wave += u

# ==========================================
# PLOT
# ==========================================

fig, ax = plt.subplots(figsize=(11, 5))

colors = plt.cm.turbo(np.linspace(0, 1, len(waves)))

for i, (w, u, color) in enumerate(
    zip(waves, individual_waves, colors)
):
    ax.plot(
        t * 1e15,
        u,
        color=color,
        linewidth=1.5,
        label=f"Onda {i+1}: {w['wavelength']} nm"
    )

# Resultant wave
# if len(waves) > 1:
#     ax.plot(
#         t * 1e15,
#         total_wave,
#         color="black",
#         linewidth=2,
#         linestyle="--",
#         label="Superposition"
#     )

ax.set_xlabel("Tiempo (fs)")
ax.set_ylabel("Amplitud (normalizada)")
ax.set_title("Onda de Luz monocromática en una posición fija")

ax.grid(True, alpha=0.25)
ax.axhline(0, color="black", linewidth=0.7)
ax.legend()
ax.margins(x=0)

plt.tight_layout()
plt.savefig("../simple_waves.png", bbox_inches="tight")
plt.show()
