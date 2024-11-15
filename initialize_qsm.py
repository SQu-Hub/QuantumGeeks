from qsm import QSM
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Initialize QSM system
def initialize_qsm():
    num_qubits = 2  # Specify the number of qubits
    qsm_system = QSM(num_qubits)
    print("QSM system initialized successfully.")
    return qsm_system

# Step 2: Define a transmon-like Hamiltonian
def define_transmon_hamiltonian(num_levels=4, E_C=0.2, E_J=1.0):
    """
    Define a simplified transmon Hamiltonian:
    H = 4 * E_C * (n^2) - E_J * cos(phi)
    """
    n = np.arange(-num_levels // 2, num_levels // 2)  # Charge states
    H = np.diag(4 * E_C * (n**2))  # Diagonal terms
    for i in range(len(n) - 1):
        H[i, i + 1] = H[i + 1, i] = -E_J / 2  # Off-diagonal terms (cos(phi) term)
    return H

# Step 3: Compute energy levels
def compute_energy_levels(H):
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    return eigenvalues, eigenvectors

# Step 4: Visualize energy spectrum
def plot_energy_spectrum(eigenvalues):
    plt.plot(eigenvalues, 'o', label="Energy Levels")
    plt.xlabel('State Index')
    plt.ylabel('Energy Level (in arbitrary units)')
    plt.title('Energy Spectrum of the Transmon System')
    plt.grid(True)
    plt.legend()
    plt.show()

# Step 5: Additional validation (optional noise simulation)
def add_noise_to_hamiltonian(H, noise_level=0.01):
    """
    Introduce random noise to the Hamiltonian to simulate experimental imperfections.
    """
    noise = noise_level * np.random.randn(*H.shape)
    noisy_H = H + (noise + noise.T) / 2  # Ensure Hermiticity
    return noisy_H

if __name__ == "__main__":
    # Initialize the QSM system
    qsm_system = initialize_qsm()

    # Apply a Hadamard gate and display state vector
    qsm_system.h(0)
    state_vector = qsm_system.state_vector()
    print("State Vector after applying Hadamard Gate:", state_vector)

    # Define the transmon Hamiltonian
    transmon_H = define_transmon_hamiltonian()
    print("Transmon Hamiltonian:\n", transmon_H)

    # Compute eigenvalues (energy levels)
    eigenvalues, eigenvectors = compute_energy_levels(transmon_H)
    print("Eigenvalues (Energy Levels):\n", eigenvalues)

    # Visualize energy spectrum
    plot_energy_spectrum(eigenvalues)

    # Optional: Add noise to the Hamiltonian and recompute energy levels
    noisy_H = add_noise_to_hamiltonian(transmon_H)
    noisy_eigenvalues, _ = compute_energy_levels(noisy_H)
    print("Noisy Eigenvalues (Energy Levels):\n", noisy_eigenvalues)

    # Visualize noisy energy spectrum for comparison
    plot_energy_spectrum(noisy_eigenvalues)
