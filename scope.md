# 🌙 Nightly Matrix App (GUI & CLI Edition) ♣♥

A hybrid Python-based matrix application equipped with both a sleek, Tokyo Night-inspired desktop GUI and an interactive terminal workflow. Utilizing the power of `numpy` for mathematical operations and `ast` for safe string-to-array parsing, this tool provides a comprehensive suite of linear algebra tools—now featuring a visual grid editor, active memory management, and an algebraic system solver.

## 🎯 Scope of the Project

The scope of this project is to provide a lightweight, interactive, and beautifully styled matrix calculator tailored for linear algebra. It bridges the gap between manual calculation, CLI efficiency, and modern desktop UI experiences without requiring heavy computational environments like MATLAB or Jupyter notebooks.

- **In-Scope:** Basic matrix arithmetic (scalar and vector/matrix), advanced linear algebra operations (inverses, adjoints, determinants, rank, cofactors, orthogonality, and independence checks), symmetric/skew-symmetric matrix generation, an interactive pop-up grid editor (`⊞`), active memory management, and symbolic linear system equation formatting/solving.
- **Out-of-Scope:** Complex number algebra, advanced sparse matrix optimizations, and cloud database syncing.
- **Future Scope (Roadmap):** Implementing advanced polynomial root finders (Quadratic and Cubic function solvers) and spectral decomposition tools (Eigenvalues and Eigenvectors).

## 💡 Use Cases

- **Engineering & Math Students:** Verifying manual homework calculations for linear algebra assignments (e.g., checking if a matrix is singular, finding the cofactor matrix, confirming the rank, or solving linear equation systems).
- **Educators:** Quickly generating random symmetric or skew-symmetric matrices of size $N \times N$ to create test questions or demonstrate matrix properties in class.
- **Data Science Beginners:** Getting comfortable with matrix dimensionality, shapes, and the rules of matrix multiplication (dot products) using either the visual grid editor or direct python list inputs.
- **Quick Computations:** Developers and researchers who need to quickly calculate determinants, inverses, or solve matrix equations without leaving their workspace.

## ⚙️ Functionality & Features

The application features a responsive Bento-grid GUI dashboard (and underlying modular math routines) divided into core operation categories:

### 1. Basic Operations
Handles arithmetic between a matrix and either a scalar value or another matrix.
- **Scalar Operations:** Adds, subtracts, or multiplies a matrix by a scalar value. *(Note: Scalar addition/subtraction in this app is implemented by multiplying the scalar by an Identity matrix first, keeping operations mathematically sound for square matrices).*
- **Matrix-to-Matrix Operations:** Performs element-wise addition and subtraction (validating that both matrices share the exact same shape and dimensions) and matrix multiplication (`@`, validating that columns of Matrix 1 match the rows of Matrix 2).

### 2. Advanced Operations
Provides deep-dive linear algebra analysis on a single inputted matrix. Every advanced operation also outputs "Extras" (Singularity, Symmetry, and Determinant) to give a complete profile of the matrix.
- **Determinant & Singularity:** Calculates the determinant and checks if it equals 0 (singular matrices cannot be inverted).
- **Transpose:** Swaps the rows and columns of the matrix.
- **Symmetry Suite:** 
  - Checks if a matrix is symmetric ($A = A^T$) or skew-symmetric ($A = -A^T$).
  - Converts a non-symmetric matrix into a symmetric one by multiplying it by its transpose ($A \cdot A^T$), featuring confirmation prompts for skew-symmetric inputs.
  - Randomly generates $N \times N$ symmetric or skew-symmetric matrices on the fly.
- **Inverse:** Calculates the multiplicative inverse of the matrix (if non-singular).
- **Adjoint:** Computes the adjoint (adjugate) matrix using the formula: `Adjoint = Determinant * Inverse`.
- **Cofactor Matrix:** Computes the cofactor matrix using the transposed inverse scaled by the determinant.
- **Rank:** Determines the rank of the matrix (the maximum number of linearly independent column vectors).
- **Orthogonality & Independence Checkers:** Evaluates whether a matrix is orthogonal ($A \cdot A^T = I$) or column-independent.

### 3. Algebraic Operations & Visual Tools
- **Linear System Solver:** Formats coefficient matrix $A$ and constant vector $B$ into symbolic linear equations ($ax + by + cz = d$) and computes the exact solution vector using `np.linalg.solve`.
- **Visual Grid Editor (`⊞`):** A pop-up spreadsheet-style cell editor with keyboard arrow navigation, two-way input synchronization, and shape presets ($2\times2$, $3\times3$, $3\times1$).
- **Matrix Memory Manager:** Saves results into active memory (`memory`) and lets users instantly load them back into Matrix A or Matrix B (`ANS` functionality).

---
*Built with love ♣♥*
