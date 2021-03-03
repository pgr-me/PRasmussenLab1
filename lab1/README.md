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

Please refer to the ```__main__.py``` module for more information on using arguments.

## Features

* 
* Option to parse single-digit numerals

## Licensing
This project is licensed under the MIT license.
