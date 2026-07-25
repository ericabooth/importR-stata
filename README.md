# importR-stata (v2.0.0)

**A dual-bridge (R/Python) Stata command for importing R data files (.Rdata, .Rda, .Rds).**

[![Stata Version](https://img.shields.io/badge/Stata-16+-blue.svg)](https://www.stata.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

`importR` v2.0 is a major upgrade that provides a robust way to bring R datasets into Stata. It is designed to work even if R is not installed on the system, by falling back to Stata's native Python integration.  It is not practically possible to import  R data using "pure" Stata commands (like file read or Mata) because .Rdata and .RDS files are  complex, compressed binary objects that use a custom serialization format. Parsing them from
  scratch in Stata would require building a full binary decoder in Mata, which is a massive engineering undertaking. To avoid this, the "Hybrid" approach in importR first looks for R installed, if it doesn't find
  R, it will attempt to use Stata's built-in Python integration (available in Stata 16 and newer).
  This provides two paths to success:

   1. Path A (R): Uses Rscript and the haven package (best for R users).
   2. Path B (Python): Uses Stata's internal Python with the pyreadstat library (best for modern
      Stata environments).

## ✨ Features

- **Dual-Bridge Architecture:**
  - **Primary (R):** Uses `Rscript` and the `haven` package.
  - **Secondary (Python):** Uses Stata's `python` integration and the `pyreadstat` library.
- **Format Support:** Works with `.Rdata`, `.Rda`, and `.Rds`.
- **Intelligent Fallback:** Automatically detects the best available tool on your machine.

---

## 🛠️ Installation & Requirements

Install from GitHub in Stata:

```stata
net install importR, from("https://raw.githubusercontent.com/ericabooth/importR-stata/main/") replace force
discard
which importR
help importR
```

To pull the example R dataset alongside the command, `net get` the ancillary file:

```stata
net get importR, from("https://raw.githubusercontent.com/ericabooth/importR-stata/main/")
importR using example.rdata, clear
```

`net get` drops ancillary files into the current directory and lowercases the
name, so the example arrives as `example.rdata` even though the repository
stores it as `examples/example.Rdata`.

`importR` needs one of the two bridges below on the machine.

### For the R Bridge (Default)
- **R** and **Rscript** must be in your system's PATH.
- The R package **`haven`** must be installed.

### For the Python Bridge (Fallback)
- **Stata 16** or newer.
- The Python library **`pyreadstat`**. You can install it from within Stata:
  ```stata
  python pip install pyreadstat
  ```

---

## 📖 Quick Start

```stata
* The command will automatically choose the best method
importR using "data/my_results.Rdata", clear

* Works with RDS files too
importR using "data/model_fit.rds", clear
```

## 📤 Bonus Utilities: Python Standalone Tools

While `importR` is designed for Stata users, this repository also includes standalone Python scripts for converting between Stata and R formats **outside of Stata**.

### Requirements
Ensure you have the required Python libraries:
```bash
pip install pyreadstat pyreadr pandas
```

### 1. `RtoStata.py` (R → Stata)
Convert R data files (.rds, .Rdata) to Stata .dta format:
```bash
# Convert to DTA (default)
python RtoStata.py mydata.rds

# Specify Stata version (e.g., version 13)
python RtoStata.py mydata.Rdata -v 13
```

### 2. `pythontoR.py` (Stata → R)
Convert Stata .dta files into R formats (.rds or .rdata):
```bash
# Convert to RDS (default)
python pythontoR.py mydata.dta

# Convert to RData
python pythontoR.py mydata.dta --format rdata
```

---

## 👤 Author

**Eric A. Booth**
- 🏛️ Sr Researcher, Texas 2036
- 📧 [eric.a.booth@gmail.com](mailto:eric.a.booth@gmail.com)
- 🌐 [www.eric-booth.com](http://www.eric-booth.com)
- 💼 [GitHub Profile](https://github.com/ericabooth)

## 📄 License
This project is licensed under the MIT License.
