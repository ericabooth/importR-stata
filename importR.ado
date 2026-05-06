*! importR - import R data files (.Rdata, .Rda, .Rds) into Stata
*! Eric A. Booth <eric.a.booth@gmail.com>
*! Version 1.0.0 : May 2026

program define importR, rclass
    version 16
    syntax using/ [, Replace CLEAR RDS]

    *-- Extension Check
    loc ext = lower(substr(`"`using'"', -6, .))
    loc is_rds = 0
    if strpos("`ext'", ".rds") loc is_rds = 1
    if "`rds'" != "" loc is_rds = 1

    *-- File Validation
    cap confirm file `"`using'"'
    if _rc {
        di as err "File `using' not found."
        exit 601
    }

    *-- Check for R installation
    qui cap shell Rscript --version
    if _rc {
        di as err "Rscript not found in system path. Please ensure R is installed and Rscript is in your PATH."
        exit 111
    }

    *-- Prep Temporary Files
    tempfile dtafile rscript
    loc dtafile : subinstr local dtafile "\\" "/", all
    
    *-- Build R Script
    tempname fh
    qui file open `fh' using "`rscript'", write text replace
    
    file write `fh' "if (!require('haven')) install.packages('haven', repos='https://cloud.r-project.org/')" _n
    
    if `is_rds' {
        file write `fh' "df <- readRDS('`using'')" _n
    }
    else {
        file write `fh' "load('`using'')" _n
        file write `fh' "df <- get(ls()[1])" _n // Grabs the first object loaded
    }
    
    file write `fh' "if (!is.data.frame(df)) df <- as.data.frame(df)" _n
    file write `fh' "haven::write_dta(df, '`dtafile'', version = 14)" _n
    
    file close `fh'

    *-- Run R Bridge
    di as txt "Bridging to R to convert data..."
    qui shell Rscript "`rscript'"
    
    *-- Check results
    cap confirm file "`dtafile'"
    if _rc {
        di as err "R conversion failed. Ensure the 'haven' package is available in R and the file is a valid R data object."
        exit 198
    }

    *-- Import to Stata
    loc use_opt = cond("`clear'" != "", "clear", "")
    use "`dtafile'", `use_opt'
    
    *-- Reporting
    di as smcl _n "{text}Successfully imported {res}`using'{text} into Stata."
    di as txt "Observations: " as res _N
    di as txt "Variables:    " as res c(k)

    *-- Return values
    return local filename "`using'"
    return scalar nobs = `_N'
    return scalar nvars = c(k)
end
