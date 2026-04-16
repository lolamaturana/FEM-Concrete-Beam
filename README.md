<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Columbia_University_1754.svg" width="400" valign="left">

# (ABAQUS) Finite Element Analysis: Bending of a Concrete Beam with Holes

## Project Description
This project analyzes the behavior of two cantilever concrete beam designs with different hole shapes subjected to a uniform load. The primary objective is to evaluate and compare deformation and stress distribution using the finite element method.

The two analyzed designs are:
* **Design 1:** Beam with two circular holes.
* **Design 2:** Beam with two rotated square holes.

## Methodology
The computational analysis was performed using Abaqus simulation software.
* **Elements:** 3-node triangular elements were used under plane stress conditions.
* **Meshing:** Two different mesh densities were implemented: a coarse mesh (~1120 elements) and a fine mesh (~2000 elements) to assess convergence and result accuracy.
* **Validation:** Axial stress results ($\sigma_{xx}$) were compared against theoretical values derived from Euler-Bernoulli beam theory.

## Key Results
* **Displacement:** Both beams exhibited a similar global response, with maximum displacement at the free end. The beam with circular holes showed slightly higher deflections (max 13.62 $\mu$m) compared to the square hole design (max 13.22 $\mu$m), indicating slightly lower stiffness.
* **Von Mises Stresses:** The highest stress concentrations occurred near the fixed supports where bending is greatest. The maximum Von Mises stress difference between the circular (19.62 Pa) and square (19.27 Pa) designs was minimal, suggesting that global loading governed distribution more than hole shape.
* **Mesh Refinement:** The comparison demonstrated that the fine mesh accurately captured sharp stress gradients and local concentrations around the holes, which the theoretical equations and coarse mesh tended to smooth over.

## Academic Context
This project was developed for the course *ENMEE3332 - Finite Elements* at Columbia University, Fu Foundation School of Engineering and Applied Science (Fall 2025), under the supervision of Professor H. Waisman.
