# importr-stata (v2.0.3)

**A dual-bridge (R/Python) Stata command for importing R data files (.Rdata, .Rda, .Rds).**

[![Stata Version](https://img.shields.io/badge/Stata-16+-blue.svg)](https://www.stata.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

`importr` v2.0 is a major upgrade that provides a robust way to bring R datasets into Stata. It is designed to work even if R is not installed on the system, by falling back to Stata's native Python integration.  It is not practically possible to import  R data using "pure" Stata commands (like file read or Mata) because .Rdata and .RDS files are  complex, compressed binary objects that use a custom serialization format. Parsing them from
  scratch in Stata would require building a full binary decoder in Mata, which is a massive engineering undertaking. To avoid this, the "Hybrid" approach in importr first looks for R installed, if it doesn't find
  R, it will attempt to use Stata's built-in Python integration (available in Stata 16 and newer).
  This provides two paths to success:

   1. Path A (R): Uses Rscript and the haven package (best for R users).
   2. Path B (Python): Uses Stata's internal Python with the pyreadr library (to read the R
      file) and pyreadstat (to write the .dta) (best for modern Stata environments).

## ✨ Features

- **Dual-Bridge Architecture:**
  - **Primary (R):** Uses `Rscript` and the `haven` package.
  - **Secondary (Python):** Uses Stata's `python` integration with the `pyreadr` and `pyreadstat` libraries.
- **Format Support:** Works with `.Rdata`, `.Rda`, and `.Rds`.
- **Intelligent Fallback:** Automatically detects the best available tool on your machine.

---

## 🛠️ Installation & Requirements

Install from GitHub in Stata:

```stata
net install importr, from("https://raw.githubusercontent.com/ericabooth/importR-stata/main/") replace force
discard
which importr
help importr
```

To pull the example R datasets alongside the command, `net get` the ancillary files:

```stata
net get importr, from("https://raw.githubusercontent.com/ericabooth/importR-stata/main/")
importr using importr_example.rdata, clear
importr using importr_example.rds, clear
```

`net get` drops the two example files, `importr_example.rdata` and
`importr_example.rds`, into the current directory.

`importr` needs one of the two bridges below on the machine.

### For the R Bridge (Default)
- **R** and **Rscript** must be in your system's PATH.
- The R package **`haven`**. If it is missing, the bridge installs it from CRAN
  (`install.packages("haven")`) before converting, which needs an internet
  connection and writes to your R library.

### For the Python Bridge (Fallback)
- **Stata 16** or newer.
- The Python libraries **`pyreadr`** and **`pyreadstat`**, installed into the
  Python that `python query` reports. `python pip` is not a Stata command, so
  run pip from a terminal:
  ```bash
  /path/to/that/python3 -m pip install pyreadr pyreadstat
  ```
  When the Python bridge cannot run, `importr` prints this command with the
  right path.

---

## 📖 Quick Start

```stata
* The command will automatically choose the best method
importr using "data/my_results.Rdata", clear

* Works with RDS files too (detected from the extension; the rds option forces it)
importr using "data/model_fit.rds", clear
importr using "data/model_fit.dat", clear rds

* What was read
display r(nobs) " obs, " r(nvars) " vars from " r(filename) " (object " r(object) ")"
```

Options: `clear` replaces the data in memory (without it, changed data in
memory stop `importr` with `r(4)`); `rds` treats the file as an RDS file.

Stored results: `r(nobs)`, `r(nvars)`, `r(filename)`, and, for `.Rdata`/`.Rda`
files, `r(object)`, the name of the object read. A file with several objects
gives the first data frame by name (C-locale order), the same with either
bridge.

## 📤 Bonus Utilities: Python Standalone Tools

While `importr` is designed for Stata users, this repository also includes standalone Python scripts for converting between Stata and R formats **outside of Stata**.

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

## Changelog

- **2.0.3 (9 Nov 2026):** changed data in memory without `clear` now give `r(4)` instead of a misleading "needs R or pyreadr" error; the install advice prints a pip command to run in a terminal (`python pip` is not a Stata command); both bridges take the same object from a multi-object `.Rdata` file and report it in `r(object)`. `RtoStata.py` now uses `pyreadr.read_r()` (it called `read_rds()`/`read_rdata()`, which pyreadr does not provide).
- **2.0.2 (Aug 2026):** bridge subroutines are rclass; each bridge is attempted in turn; Windows paths.

## 👤 Author

**Eric A. Booth**
- 🏛️ Sr Researcher, Texas 2036
- 📧 [eric.a.booth@gmail.com](mailto:eric.a.booth@gmail.com)
- 🌐 [www.eric-booth.com](http://www.eric-booth.com)
- 💼 [GitHub Profile](https://github.com/ericabooth)

## 📄 License
This project is licensed under the MIT License.
