# 🌙 Nightly Matrix App (GUI Edition)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-required-orange)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-purple)
![License](https://img.shields.io/badge/license-MIT-green)

A sleek, dark-themed desktop GUI application for evaluating and manipulating mathematical matrices. Built with Python's Tkinter and NumPy, this "Nightly Edition" upgrades the original CLI experience with a built-in terminal, modern placeholder inputs, and an integrated memory system for rapid sequential calculations.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage & Input Formatting](#-usage--input-formatting)
- [The Memory System](#-the-memory-system)
- [Operations Guide](#-operations-guide)

## ✨ Features

- **"Nightly" Dark Mode UI:** A custom-styled interface featuring a hacker-style integrated green-on-black output console, custom scrollbars, and clearable text entries.
- **Matrix Memory Manager:** Save the output of your last calculation into active memory and instantly load it back into Matrix A or Matrix B for seamless chain calculations.
- **Basic & Advanced Math:** Perform element-wise arithmetic, matrix multiplication, determinants, inversions, and cofactor generations.
- **Symmetry Tools:** Check symmetry, force symmetry via multiplication, or randomly generate symmetric/skew-symmetric matrices of any size.

## 📋 Prerequisites

- **Python 3.8+**
- **NumPy:** Used for core matrix calculations.
- **Tkinter:** Python's standard GUI package (usually included with standard Python installations. Linux users may need to install `python3-tk` via their package manager).

## 🚀 Installation

1. Clone the repository or download the script file.
2. Install the required dependency using pip:

```bash
pip install numpy
```

3. Run the application:

```bash
python nightly_matrix_app.py
```

## 💻 Usage & Input Formatting

The application features three main input fields at the top of the window: **Matrix A**, **Matrix B**, and **Scalar / Size**.

### ⚠️ How to Input Matrices
The app uses Python's `ast.literal_eval` to safely parse text. **You must use standard Python list-of-lists syntax.** 

- **3x3 Matrix:** `[[1, 2, 3], [2, 3, 4], [3, 4, 5]]`
- **2x2 Matrix:** `[[1, 2], [3, 4]]`
- **1x3 Vector:** `[[1, 2, 3]]`

> **Pro Tip:** You can quickly clear any input field (or the output console) by clicking the red `✕` button on the right side of the box.

## 💾 The Memory System

Located in the top right corner, the Memory System allows you to reuse data without retyping it:

1. **Save Output to Mem:** After performing an operation (e.g., Matrix A + Matrix B), click this to save the resulting matrix into active memory. The status indicator will light up green.
2. **Mem -> A / Mem -> B:** Click these to instantly paste your saved matrix into the respective input fields for your next operation.

## 🧮 Operations Guide

### 1. Basic Scalar (A & Scalar)
Operations requiring **Matrix A** and the **Scalar** field:
- **A + Scalar** / **A - Scalar** / **A * Scalar**

### 2. Basic Matrix (A & B)
Operations requiring both **Matrix A** and **Matrix B**:
- **A + B** / **A - B** / **A @ B** (Matrix Multiplication/Dot Product)

### 3. Advanced Operations (Matrix A)
Operations requiring only **Matrix A**:
- **Det & Singularity:** Calculates determinant and checks invertibility.
- **Rank:** Determines linear independence.
- **Transpose:** Flips the matrix over its diagonal.
- **Inverse:** Computes the multiplicative inverse.
- **Adjoint & Cofactor:** Generates derived matrices.

### 4. Symmetry Operations
Operations requiring **Matrix A** OR the **Scalar** field:
- **Check / Make Symmetric (A):** Checks Matrix A. If not symmetric, converts it using `A @ A.T`.
- **Gen Symmetric / Gen Skew-Sym:** Requires a single integer in the **Scalar / Size** field (e.g., entering `3` generates a 3x3 matrix). Populates the console with a randomly generated matrix of that size.

---
*Built with Python, Tkinter, and NumPy.*
## 🚩 Update Notes

- [ ] **"Remember Me" Matrix Memory:** Variables (`memory`, `s`) are finally worked upon and have reached the end of development and the application has achieved a binary memory feature.
- [ ] **Enhanced Error Handling:**  This has finally rolled out and now exception catching for non-square matrices during operations like Adjoint and Cofactor generation to prevent unexpected crashes has been optimized well.

## 📖 Future Updates

- [ ] **"Cofactor Matrix Generator":** Users could generate cofactor matrices from their input matrix.
- [ ] **"Orthogonal Matrix Generator / Checker":** Users could generate and check if their matrix is orthogonal or not.
- [ ] **Eigenvalue and Eigenvector:**  Options featuring eigenvalues and eigenvectors could be developed in the future.
- [ ] **"Independence Checker:"** Users could check if their matrix is independent or not.
- [ ] **Vector Input:** More vector operations can be indroduced

---
*Built with love ♥*
