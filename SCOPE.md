# Matrix Operations CLI App

A Python-based Command Line Interface (CLI) application designed to perform a comprehensive suite of matrix computations. Utilizing the power of `numpy` for mathematical operations and `ast` for safe string-to-array parsing, this tool provides an interactive terminal menu for users to evaluate matrices in real-time.

## 🎯 Scope of the Project

The scope of this project is to provide a lightweight, interactive, and terminal-based calculator specifically tailored for linear algebra. It bridges the gap between manual matrix calculation and heavy computational environments like Jupyter notebooks or MATLAB.

* **In-Scope:** Basic matrix arithmetic (scalar and vector), advanced linear algebra operations (inverses, adjoints, determinants, rank), and symmetric matrix generation.
* **Out-of-Scope:** Complex numbers, eigenvalues/eigenvectors, sparse matrix optimizations, and graphical user interfaces (GUI).
* **Future Scope (Roadmap):** Implementing a "Remember Me" memory matrix variable (initialized as `memory=0` in the script) to store the result of a previous operation and use it as the input for the next calculation, mimicking the `ANS` button on scientific calculators.

## 💡 Use Cases

* **Engineering & Math Students:** Verifying manual homework calculations for linear algebra assignments (e.g., checking if a matrix is singular, finding the cofactor matrix, or confirming the rank).
* **Educators:** Quickly generating random symmetric or skew-symmetric matrices of size N x N to create test questions or demonstrate matrix properties in class.
* **Data Science Beginners:** Getting comfortable with matrix dimensionality, shapes, and the rules of matrix multiplication (dot products) without needing to write throwaway Python scripts.
* **Quick Terminal Computations:** Developers who need to quickly calculate the determinant or inverse of a matrix directly from the command line without leaving their workspace.

## ⚙️ Functionality & Features

The application operates on a continuous `while` loop, allowing back-to-back calculations until the user opts to exit. It is divided into two main operation categories:

### 1. Basic Operations
Handles arithmetic between a matrix and either a scalar value or another matrix.
* **Scalar Operations:** Adds, subtracts, or multiplies a matrix by a scalar value. *(Note: Scalar addition/subtraction in this app is implemented by multiplying the scalar by an Identity matrix first, keeping operations mathematically sound for square matrices).*
* **Matrix-to-Matrix Operations:** Performs element-wise addition and subtraction (validating that both matrices share the exact same shape and dimensions) and matrix multiplication (validating that columns of Matrix 1 match the rows of Matrix 2).

### 2. Advanced Operations
Provides deep-dive linear algebra analysis on a single inputted matrix. Every advanced operation also prints "Extras" (Determinant, Singularity, and Symmetry) to give a complete profile of the matrix.
* **Determinant & Singularity:** Calculates the determinant and checks if it equals 0 (singular matrices cannot be inverted).
* **Transpose:** Swaps the rows and columns of the matrix.
* **Symmetry Suite:** 
  * Checks if a matrix is symmetric (A = A^T) or skew-symmetric (A = -A^T).
  * Converts a non-symmetric matrix into a symmetric one by multiplying it by its transpose (A * A^T).
  * Randomly generates N x N symmetric or skew-symmetric matrices on the fly.
* **Inverse:** Calculates the multiplicative inverse of the matrix (if non-singular).
* **Adjoint:** Computes the adjoint (adjugate) matrix using the formula: `Adjoint = Determinant * Inverse`.
* **Cofactor Matrix:** Computes the cofactor matrix using the transposed inverse scaled by the determinant.
* **Rank:** Determines the rank of the matrix (the maximum number of linearly independent column vectors).

## 🚀 Getting Started

### Prerequisites
You need Python 3 installed along with the `numpy` library.

```bash
pip install numpy
