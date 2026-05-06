#!/usr/bin/env python3
"""
pythontoR.py - Convert Stata .dta files to R .Rds or .Rdata formats.
Author: Eric A. Booth <eric.a.booth@gmail.com>
Version: 1.0.0
"""

import os
import argparse
import sys

def convert_stata_to_r(input_file, output_file=None, format='rds'):
    try:
        import pyreadstat
        import pyreadr
        import pandas as pd
    except ImportError:
        print("Error: Missing required libraries. Please run: pip install pyreadstat pyreadr pandas")
        sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # 1. Read Stata file
    print(f"Reading Stata file: {input_file}...")
    df, meta = pyreadstat.read_dta(input_file)

    # 2. Determine output filename if not provided
    if not output_file:
        base = os.path.splitext(input_file)[0]
        output_file = f"{base}.{format.lower()}"

    # 3. Write R file
    print(f"Converting to R {format.upper()} format...")
    if format.lower() == 'rds':
        pyreadr.write_rds(output_file, df)
    else:
        # Default to .Rdata / .Rda
        # pyreadr writes RData as a dictionary where key is the R object name
        df_name = os.path.basename(os.path.splitext(output_file)[0])
        pyreadr.write_rdata(output_file, df, df_name=df_name)

    print(f"Successfully created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Stata .dta to R (.rds or .Rdata)")
    parser.add_argument("input", help="Path to the input Stata .dta file")
    parser.add_argument("-o", "--output", help="Path to the output R file (optional)")
    parser.add_argument("-f", "--format", choices=['rds', 'rdata'], default='rds', 
                        help="Output format: rds (default) or rdata")

    args = parser.parse_args()
    convert_stata_to_r(args.input, args.output, args.format)
