"""Peter Rasmussen, Lab 1, stack.py"""
# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse

from lab1.prefix_converter import PrefixConverter

# Parse arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--in_file", "-i", type=Path, help="Input File Pathname")
arg_parser.add_argument("--out_file", "-o", type=Path, help="Output File Pathname")
arg_parser.add_argument(
    "--use_numerals", "-n", default=False, type=bool, help="Include numerals as accepted operands"
)
arg_parser.add_argument(
    "--file_header",
    "-f",
    default="Peter Rasmussen, Lab 1",
    type=str,
    help="Include numerals as accepted operands",
)
args = arg_parser.parse_args()

# Declare in_path, out_path, use_numerals, and file_header variables
in_path = Path(args.in_file)
out_path = Path(args.out_file)
use_numerals = args.use_numerals
file_header = args.file_header

# Instantiate prefix converter object and convert file of prefix strings to postfix equivalents
prefix_converter = PrefixConverter(in_path, out_path, use_numerals, file_header)
prefix_converter.convert_prefix_input()
prefix_converter.write_output()