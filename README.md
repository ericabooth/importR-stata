# importR-stata

**A simple Stata bridge for importing R data files (.Rdata, .Rda, .Rds).**

[![Stata Version](https://img.shields.io/badge/Stata-16+-blue.svg)](https://www.stata.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

`importR` is a Stata command that automates the process of bringing R-native data into your Stata environment. It handles the heavy lifting of background conversion, allowing you to treat R files as if they were native Stata datasets.

## ✨ Features

- **Format Support:** Works with `.Rdata`, `.Rda` (workspaces), and `.Rds` (single objects).
- **Automated Bridge:** Uses `Rscript` and the `haven` package to ensure high-fidelity conversion.
- **Easy Workflow:** Simply provide the filename, and `importR` does the rest.

---

## 🛠️ Prerequisites

To use this package, you must have:
1. **R** installed on your system.
2. **Rscript** in your system's PATH.
3. The R **`haven`** package (the command will attempt to install it automatically if it's missing).

---

## 📖 Quick Start

```stata
* Import a standard R workspace
importR using "data/my_results.Rdata", clear

* Import a single R object file
importR using "data/model_fit.rds", clear
```

---

## ⚙️ Options

| Option | Description |
| :--- | :--- |
| `using` | Path to the R data file. |
| `clear` | Clears Stata memory before import. |
| `rds`   | Force RDS mode (useful if the file lacks an extension). |

---

## 👤 Author

**Eric A. Booth**
- 📧 [eric.a.booth@gmail.com](mailto:eric.a.booth@gmail.com)
- 🌐 [www.eric-booth.com](http://www.eric-booth.com)
- 💼 [GitHub Profile](https://github.com/ericabooth)

## 📄 License
This project is licensed under the MIT License.
