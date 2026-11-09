#!/usr/bin/env python3
"""
RtoStata.py - Convert R data files (.rds, .Rdata, .Rda) to Stata .dta format.
Author: Eric A. Booth <eric.a.booth@gmail.com>
Version: 1.0.1 (uses pyreadr.read_r; picks the first data frame by name)
"""

import os
import argparse
import sys

def convert_r_to_stata(input_file, output_file=None, version=14):
    try:
        import pyreadr
        import pyreadstat
        import pandas as pd
    except ImportError:
        print("Error: Missing required libraries. Please run: pip install pyreadstat pyreadr pandas")
        sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # 1. Read R file
    print(f"Reading R file: {input_file}...")
    ext = os.path.splitext(input_file)[1].lower()
    
    try:
        # pyreadr.read_r reads .rds, .Rdata and .Rda and returns a dict of
        # data frames (an .rds file gives a single entry keyed None)
        result = pyreadr.read_r(input_file)
        if ext == '.rds':
            df = result[None]
        else:
            # Same rule as importr: the first data frame by name
            names = sorted(k for k in result.keys() if k is not None)
            if not names:
                raise ValueError("no data frame found in the file")
            obj_name = names[0]
            df = result[obj_name]
            print(f"Extracted object: '{obj_name}'")
    except Exception as e:
        print(f"Error reading R file: {e}")
        sys.exit(1)

    # 2. Determine output filename if not provided
    if not output_file:
        base = os.path.splitext(input_file)[0]
        output_file = f"{base}.dta"

    # 3. Write Stata file
    print(f"Converting to Stata .dta (version {version})...")
    try:
        pyreadstat.write_dta(df, output_file, version=version)
    except Exception as e:
        print(f"Error writing Stata file: {e}")
        sys.exit(1)

    print(f"Successfully created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert R data (.rds, .Rdata) to Stata .dta")
    parser.add_argument("input", help="Path to the input R file")
    parser.add_argument("-o", "--output", help="Path to the output Stata .dta file (optional)")
    parser.add_argument("-v", "--version", type=int, default=14, 
                        help="Stata version for the .dta file (default: 14)")

    args = parser.parse_args()
    convert_r_to_stata(args.input, args.output, args.version)
