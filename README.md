<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Columbia_University_1754.svg" width="400" valign="left">

# Finite Element Analysis Portfolio: Structural & Fluid Mechanics (Civil Engineering)
This repository contains two major projects developed using the **Finite Element Method (FEM)** to solve complex engineering problems in structural mechanics and fluid dynamics.

---

## Project 1: Bending of a Concrete Beam with Holes - Using ABAQUS

### Project Description
This study analyzes the structural behavior of two cantilever concrete beam designs under a uniform distributed load ($q = 1 \text{ kN/m}^2$). The primary focus is evaluating how different geometric discontinuities (hole shapes) affect the stress distribution and overall stiffness of the beam.

**Analyzed Designs:**
* **Design 1:** Two circular holes ($d = 0.15 \text{ m}$).
* **Design 2:** Two rotated square holes ($d = 0.15 \text{ m}$).

### Methodology
* **Software:** Abaqus/Standard.
* **Element Type:** 3-node triangular elements under plane stress conditions.
* **Mesh Density:** Comparison between a Coarse Mesh (~1120 elements) and a Fine Mesh (~2000 elements).
* **Validation:** Numerical results were compared against the **Euler-Bernoulli beam theory** ($\sigma_{xx} = -My/I$).

### Key Results
* **Displacement:** Design 1 (circular) showed slightly higher maximum deflection ($13.62 \mu\text{m}$) than Design 2 ($13.22 \mu\text{m}$), indicating the square hole configuration provided slightly higher stiffness in this specific setup.
* **Stress Concentration:** The highest Von Mises stresses occurred near the fixed supports ($19.62 \text{ Pa}$ for Design 1; $19.27 \text{ Pa}$ for Design 2).
* **Convergence:** Fine mesh refinement was critical to capturing local stress gradients near the hole edges that theoretical models typically overlook.

---

## Project 2: Potential Airflow Around an Airfoil - Using MATLAB & ABAQUS

### Project Description
This project involves the numerical simulation of a 2D steady-state potential airflow around a **NACA 4424 airfoil** confined between parallel plates. The fluid is assumed to be ideal (inviscid, incompressible, and irrotational).

### Methodology
This project demonstrates a hybrid workflow between commercial software and custom programming:
* **Preprocessing:** Mesh generation and nodal/element data extraction performed in **Abaqus**.
* **Solver:** A custom **MATLAB-based FEM solver** developed to solve the Laplace equation ($\nabla^2\phi = 0$) for the velocity potential.
* **Postprocessing:** Velocity components ($u, v$) and pressure fields (via **Bernoulli’s Equation**) were calculated and visualized in MATLAB.
* **Advanced Features:** Implementation of **isoparametric elements** and **Gauss quadrature** integration for numerical consistency.

### Key Results
* **Flow Visualization:** Successfully identified stagnation points at the leading and trailing edges.
* **Pressure Field:** Captured high-pressure zones at stagnation points and low-pressure zones along the airfoil surfaces, matching theoretical potential flow expectations.
* **Validation:** MATLAB results showed excellent agreement with Abaqus native heat transfer analogies (NT11) used for verification.

---

## Technical Skills & Tools
* **Finite Element Method (FEM):** Linear static analysis, potential flow theory, weak form derivation.
* **Software:** Abaqus/CAE (Standard/Explicit).
* **Programming:** MATLAB (Custom solver development, matrix assembly, postprocessing).
* **Numerical Methods:** Isoparametric mapping, Gauss quadrature, bandwidth optimization (AHBW).

## Academic Context
These projects were completed for the course **ENMEE3332: Finite Elements** at **Columbia University, The Fu Foundation School of Engineering and Applied Science** (Fall 2025), under the supervision of **Professor H. Waisman**.

## How to Run
1.  **Abaqus Project:** Open the `.inp` files in Abaqus/CAE or submit via command line to view the structural results.
2.  **MATLAB Project:** * Ensure all `.m` scripts and the `.inp` mesh files are in the same directory.
    * Run the main script (e.g., `FinalProject_Solver.m`) to perform the analysis and generate plots.
