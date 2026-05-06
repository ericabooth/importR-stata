{smcl}
{* May2026}{...}
{hline}
help for {hi:importR}
{hline}

{title:Import R data files into Stata}

{p 4 8 2} 
{cmd:importR}
{cmd:using} {it:filename}
[{cmd:,} {cmd:clear} {cmd:rds}]

{title:Description}

{p 4 4 2}
{cmd:importR} provides a simple bridge to import R data files into Stata. It supports 
{cmd:.Rdata}, {cmd:.Rda}, and {cmd:.Rds} formats. 

{p 4 4 2}
The command works by calling {cmd:Rscript} in the background, loading the R object, 
and converting it to a Stata-compatible format using the R {cmd:haven} package.

{title:Requirements}

{p 4 8 2}
1. {cmd:R} must be installed on your system. {p_end}
{p 4 8 2}
2. {cmd:Rscript} must be available in your system's PATH. {p_end}
{p 4 8 2}
3. The R {cmd:haven} package is required (the script will attempt to install it 
automatically if missing). {p_end}

{title:Options}

{p 4 8 2}
{cmd:clear} clears any data currently in Stata's memory before importing. {p_end}

{p 4 8 2}
{cmd:rds} specifies that the source file is an RDS file. This is usually detected 
automatically from the file extension. {p_end}

{title:Examples}

{p 4 4 2}Import an R workspace file:{p_end}
{p 8 12 2}{cmd:. importR using "mydata.Rdata", clear}{p_end}

{p 4 4 2}Import a single R object file:{p_end}
{p 8 12 2}{cmd:. importR using "results.rds", clear}{p_end}

{title:Author}

{p 4 4 2}Eric A. Booth{break} 
         eric.a.booth@gmail.com{break}
         {browse "http://www.eric-booth.com"}

{title:Also see}

{p 4 8 2}On-line:  help for {help import}, {help shell}
