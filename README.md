# Matrix Operations CLI App

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-required-orange)
![Math](https://img.shields.io/badge/math-required-orange)
![Tkinter](https://img.shields.io/badge/tkinter-required-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A feature-rich, command-line Python application for evaluating and manipulating mathematical matrices. Built with NumPy, this tool allows users to input matrices on the fly and perform everything from basic arithmetic to advanced linear algebra calculations.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation Guide](#-installation)
- [Usage & Input Formatting](#-usage--input-formatting)
- [Operations Guide](#-operations-guide)
- [Roadmap](#-roadmap)

## ✨ Features

The application is divided into two main mathematical categories:

### 1. Basic Operations
Perform element-wise or dot-product arithmetic between your primary matrix and:
- **Scalars:** Addition, subtraction, and scalar multiplication.
- **Vectors/Matrices:** Addition, subtraction, and matrix multiplication.

### 2. Advanced Operations
Evaluate matrix properties or generate derived matrices:
- **Determinant & Singularity:** Calculate the determinant and check if a matrix is singular (non-invertible).
- **Transpose:** Swap rows and columns.
- **Symmetry:** 
  - Check if a matrix is symmetric or skew-symmetric.
  - Convert a matrix into a symmetric matrix.
  - Randomly generate symmetric or skew-symmetric matrices of any size.
- **Inverse & Adjoint:** Compute the multiplicative inverse and adjoint matrices.
- **Cofactor Matrix:** Generate the matrix of cofactors.
- **Rank:** Determine the linear independence of the matrix rows/columns.

## 📋 Prerequisites

- **Python 3.10+**: Required for the structural pattern matching (`match`/`case`) utilized in the script.
- **NumPy**: Used for core matrix calculations and linear algebra functions.

## 🚀 Installation

1. Clone the repository or download the script file.
2. Install the required dependency using pip:

```bash
pip install numpy
```

## 💻 Usage & Input Formatting

Run the script from your terminal:

```bash
python matrix_app.py
```

### ⚠️ How to Input Matrices
The application uses Python's `ast.literal_eval` to safely parse your text input into an array. **You must use standard Python list-of-lists syntax.** 

- **3x3 Matrix:** `[[1, 2, 3], [2, 3, 4], [3, 4, 5]]`
- **2x2 Matrix:** `[[1, 2], [3, 4]]`
- **1x3 Vector:** `[[1, 2, 3]]`

> **Note:** Ensure all brackets are properly opened and closed, and separated by commas.

## 🧮 Operations Guide

Once the app is running, you will be greeted by the main menu:

1. **Exit** - Closes the application.
2. **Basic Operations** - Prompts you for a matrix, then asks if you want to operate against a scalar or another vector/matrix.
3. **Advanced Operations** - Prompts you for a matrix, then provides a sub-menu for advanced linear algebra computations (Inverse, Rank, Adjoint, etc.). 

*The app will loop continuously until you type `no` when asked "Do you want to stay?" at the end of an operation cycle.*

## 🗺️ Roadmap

- [ ] **"Remember Me" Matrix Memory:** Variables (`memory`, `s`) are currently initialized in the codebase to pave the way for a memory feature. In future updates, users will be able to save the result of a calculation and use it as the input for their next operation without retyping the matrix.
- [ ] **Enhanced Error Handling:** Improve exception catching for non-square matrices during operations like Adjoint and Cofactor generation to prevent unexpected crashes.

---
*Built with Python and NumPy.*
