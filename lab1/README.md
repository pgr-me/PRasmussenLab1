# Peter Rasmussen, Lab 1

This Python package converts prefix statements into their postfix equivalents using stacks as the
underlying data structure.

## Getting Started

The package is designed to be executed as a module from the command line. The user must specify the
input and output file paths, as illustrated below.

```shell
python -m path/to/lab1 -i path/to/input_file.txt -o path/to/output_file.txt
```

Optionally, the user may specify whether to include numerals as acceptable operand symbols. **Please
note that only single-digit numerals (0-9) are supported in this implementation**. Additionally, the
user may specify a file header that is prepended to the outputs. The example below illustrates usage
of the optional arguments.

```shell
python -m path/to/lab1 -i path/to/in_file.txt -o path/to/out_file.txt -n True -f "Your Header"
```

A summary of the command line arguments are below.

Positional arguments:

    -i, --in_file       Input File Pathname
    -o, --out_file      Output File Pathname

Optional arguments:

    -h, --help          Show this help message and exit
    -f, --file_header   Input custom file header above output file
    -n, --use_numerals  Include numerals 0-9 among accepted operands

## Features

* Array-based stack that uses a pre-allocated array size
* Error handling to invalid prefix expressions, type errors, and value errors
* Options to parse single-digit numerals and write custom output file header
* Time and space complexity statistics appended to end of output file

## Input and Output Files

The ```resources/``` directory contains a set of input files and outputs generated by running the
module using the default optional arguments. ```required_input.txt``` is included in this directory
along with its output, ```required_output.txt```. Every other input / output pair in ```resources```
follows this naming convention.

## Example Output File

An example of the output for a three-line input is shown below.

    # Peter Rasmussen, Lab 1
    # Input file: /path/to/required_input.txt
    # Output file: /path/to/required_output.txt

    Line 1: Prefix: -+ABC, Postfix: AB+C-
    Line 2: Prefix: -A+BC, Postfix: ABC+-
    Line 3: Prefix: /A+BC +C*BA  , Postfix: PrefixSyntaxError('Column 11: Too few operators, ...

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Complexity outputs
    Function: convert_prefix_input	Time (ns): 10375000	Loops: 3
    Function: convert_prefix_stack	Time (ns): 7775000	Loops: 9
    Function: _convert_prefix_stack	Time (ns): 7190000	Loops: 8

Header statements make up the first four lines of the output file. Prefix processing outputs are
listed line by line thereafter. Each line of prefix output begins with the line number of the
corresponding prefix expression. Then, the original prefix statement is echoed. Finally, The postfix
expression is written. Below the conversion outputs are complexity outputs: time and number of
loops, a crude proxy for space complexity.

Prefix statements with syntax errors are not converted into postfix. Instead, an error message
encapsulated in PrefixSyntaxError object is written to in lieu of a postfix expression.

## Licensing

This project is licensed under the MIT license.
