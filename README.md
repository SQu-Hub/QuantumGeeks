# QuantumGeeks

Welcome to the team repository for the **Superconducting Quantum Research Program - Chip Design Hackathon 2024**. Our team consists of the following members:

- **Tilock Sadhukhan** (Leader)  
- **Indranil Ghosh**  
- **Achyut Chebiyam**  
- **Kazim Mumtaz**  
- **Aniekan Afangideh**  

## Project Overview

We implemented **Project 11**, which involves specifying two superconducting transmons using the Qubit Simulation Module (**QSM**) and simulating their energy spectrum. 

### About QSM

The **Qubit Simulation Module (QSM)** is a software package designed to facilitate the full design process for superconducting qubits and resonators. It provides a Python-based user interface that allows users to:
1. Import QSM as a library.
2. Create a `qSysLayout` object.
3. Pass the `qSysLayout` object into desired simulations.

### Our Implementation

The `_initialize_qsm.py_` file serves as our main script. In this script, we:
- Defined the Hamiltonian of the qubit system.
- Simulated the system using QSM.
- Visualized the results, which include a graph displaying discrete states and their associated energy levels in a bath.

### Results

The simulation produced a graph showing the discrete states of the qubits and their corresponding energy levels, providing insights into the behavior of the system.

## Learn More

Watch our [video](https://youtu.be/y-TJzhbAMmA) for more details about our work.
