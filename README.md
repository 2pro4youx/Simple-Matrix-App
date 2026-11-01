# 🌙 Nightly Matrix App (GUI Edition) ♣♥

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-required-orange)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-purple)
![License](https://img.shields.io/badge/license-MIT-green)

A sleek, Tokyo Night-inspired desktop GUI application for evaluating, generating, and solving mathematical matrices. Built with Python's Tkinter and NumPy, this **Nightly Pro Edition** upgrades the original CLI experience into a compact Bento-grid dashboard featuring a multi-color terminal, an interactive pop-up cell editor, an algebraic system solver, and an integrated memory manager for rapid chain calculations.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage & Input Formatting](#-usage--input-formatting)
- [The Memory System](#-the-memory-system)
- [Operations Guide](#-operations-guide)
- [Update Notes](#-update-notes)
- [Future Updates](#-future-updates)

## ✨ Features

- **Bento-Grid "Nightly" UI:** A modern dark-mode interface featuring a color-coded terminal output console, custom dark scrollbars, dynamic focus borders, and inline clear buttons (`✕`).
- **Interactive Visual Grid Editor (`⊞`):** Prefer not to type brackets? Click the `⊞` icon inside Matrix A or Matrix B to open a pop-up spreadsheet-style grid with arrow-key navigation, two-way sync, and instant presets ($2\times2$, $3\times3$, $3\times1$, Identity, Random, and Zeros).
- **Matrix Memory Manager:** Save the output of your latest calculation into active memory and load it back into Matrix A or Matrix B with a single click.
- **Comprehensive Matrix Analysis:** Perform scalar/matrix arithmetic, determinants, inversions, transpositions, adjoints, cofactors, rank calculations, orthogonality checks, and linear independence checks.
- **Symmetry Suite:** Check symmetry, convert non-symmetric matrices (with a confirmation safeguard for skew-symmetric matrices), or randomly generate symmetric and skew-symmetric matrices of any size.
- **Algebraic System Solver:** Automatically formats coefficient and constant matrices into human-readable linear equations ($ax + by + cz = d$) and solves for all variables.

## 📋 Prerequisites

- **Python 3.10+**
- **NumPy:** Used for core linear algebra and matrix calculations.
- **Tkinter:** Python's standard GUI package (included with standard Windows/macOS Python installations; Linux users may need to install `python3-tk` via their package manager).

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

The top card of the application houses three input fields: **Matrix A (or Coeff)**, **Matrix B (or Const)**, and **Scalar / Gen Size**. You can enter matrices using either the visual pop-up grid or standard Python list syntax.

### 1. Using the Visual Grid Editor (`⊞`)
Click the **`⊞`** button on the right side of the **Matrix A** or **Matrix B** input bar to launch the pop-up Grid Editor:
- Set your desired **Rows** and **Cols** (from $1\times1$ up to $8\times8$) or click a quick shape preset (**2×2**, **3×3**, **3×1**).
- Navigate smoothly between cells using your keyboard's **Arrow Keys** or **Tab**.
- Use quick-fill tools (**Identity (I)**, **Random**, **Zeros**) to populate cells automatically.
- Click **Apply to Input ✓** (or press `Enter`) to write the formatted matrix directly into the input bar.

### 2. Direct List Input (`ast.literal_eval`)
If typing directly into the input bar, use standard Python list-of-lists syntax:

- **$3\times3$ Matrix:** `[[1, 2, 3], [2, 3, 4], [3, 4, 5]]`
- **$2\times2$ Matrix:** `[[1, 2], [3, 4]]`
- **$1\times3$ Row Vector:** `[[1, 2, 3]]`
- **$3\times1$ Column Vector (Constants):** `[[1], [2], [3]]`

> **Pro Tip:** Click the `✕` button inside any input box (or at the top-right of the Terminal Output panel) to clear its contents immediately.

## 💾 The Memory System

Located in the top-right panel, the Memory System lets you chain operations without retyping results:

1. **Save Output:** After running any matrix operation or generator, click this button to store the resulting matrix in active memory. The status indicator will update to display the saved matrix's shape (e.g., `MEM: (3, 3)`).
2. **Load → A / Load → B:** Click either button to paste your stored matrix directly into **Matrix A** or **Matrix B** for your next calculation.

## 🧮 Operations Guide

### 1. Basic Operations (Case 2)
- **Scalar (`Matrix A` & `Scalar`):**
  - **A + S** / **A - S:** Adds or subtracts the scalar along the main diagonal using an identity matrix ($A \pm S \cdot I$).
  - **A \* S:** Multiplies every element in Matrix A by the scalar.
- **Vector / Matrix (`Matrix A` & `Matrix B`):**
  - **A + B** / **A - B:** Element-wise addition and subtraction (requires matching dimensions).
  - **A @ B:** Matrix multiplication / dot product (requires inner dimensions to match).

### 2. Advanced Operations (Case 3 — Uses `Matrix A`)
Each operation also outputs an **Extras** summary (Singularity, Symmetry, and Determinant):
- **Determinant:** Computes $\det(A)$ rounded to 4 decimal places.
- **Singularity:** Checks whether $\det(A) = 0$.
- **Transpose:** Flips Matrix A over its main diagonal ($A^T$).
- **Inverse:** Computes the multiplicative inverse ($A^{-1}$) if non-singular.
- **Adjoint:** Computes $\text{adj}(A) = \det(A) \cdot A^{-1}$.
- **Cofactor:** Computes the cofactor matrix ($\text{adj}(A)^T$).
- **Rank:** Calculates the rank of the matrix via SVD.
- **Orthogonal?:** Checks if $A \cdot A^T = I$.
- **Independent?:** Checks if the column count equals the matrix rank.

### 3. Symmetry Operations (Case 3.4)
- **Check Sym:** Evaluates whether **Matrix A** is Symmetric ($A = A^T$), Skew-Symmetric ($A = -A^T$), or neither.
- **Make Sym:** Converts **Matrix A** via element-wise multiplication ($A \odot A^T$). Includes an interactive confirmation prompt if a Skew-Symmetric matrix is detected.
- **Gen Sym / Gen Skew-Sym:** Reads an integer $N$ from the **Scalar / Gen Size** field and generates a random $N \times N$ Symmetric or Skew-Symmetric matrix.

### 4. Algebraic Solver (Case 4 — `A = Coeff`, `B = Const`)
- **Linear Eq:** Formats **Matrix A** and **Matrix B** into a system of linear equations ($a, b, c, \dots$) in the terminal and solves for the unknown vector using `np.linalg.solve(A, B)`. *(Requires a square, non-singular coefficient matrix A).*
- **Quadratic / Cubic:** Reserved module triggers currently marked as *Under Development*.

## 🚩 Update Notes

- [x] **"Remember Me" Matrix Memory:** Memory variables are fully integrated into the GUI, allowing instant saving and loading into Matrix A or Matrix B.
- [x] **Interactive Visual Grid Editor (`⊞`):** Added a pop-up cell-by-cell matrix editor with two-way input synchronization, arrow-key navigation, and preset generators.
- [x] **Cofactor, Orthogonality & Independence Checkers:** Dedicated operations rolled out in the Advanced Operations panel.
- [x] **Linear Equation Presenter & Solver:** Added symbolic equation formatting (`linp`) and linear system solving under Algebraic Operations.
- [x] **Enhanced Error Handling:** Optimized exception catching for non-square and singular matrices across Adjoint, Cofactor, Inverse, and Linear Solver routines to prevent crashes.

## 📖 Future Updates

- [ ] **Quadratic & Cubic Function Solvers:** Complete the remaining polynomial solvers in the Algebraic Operations module.
- [ ] **Eigenvalues and Eigenvectors:** Add spectral decomposition tools to the Advanced Operations panel.
- [ ] **Orthogonal Matrix Generator:** Allow users to randomly generate orthogonal matrices alongside the existing checker.
- [ ] **Expanded Vector Operations:** Introduce cross products, unit vector normalization, and projection tools.

---
*Built with love ♣♥*
