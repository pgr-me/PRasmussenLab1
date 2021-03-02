from sys import stderr
from typing import TextIO
from time import time_ns
from lab1.base_converter import BaseConverter
from lab1.runtime_metric import RuntimeMetric


def human_readable_binary_string(binary_string: str) -> str:
    """
    Takes a string of bits and separates it out into sets of 4 and pads it
    to at least 32 bits, or an multiple of 8 if larger.
    :param binary_string: The binary string to make 'human readable'
    :return: A more easily read binary string
    """
    if len(binary_string) < 32:
        # pad the binary_string to be 32 bits wide:
        padding = 32 - len(binary_string)
    else:
        padding = 8 - len(binary_string) % 8

    binary_string = "0" * padding + binary_string

    spaced_binary_string = ""
    # Print a space between each set of 4 bits
    for i in range(len(binary_string) // 4):
        offset = i * 4
        spaced_binary_string += binary_string[offset:offset + 4] + " "
    # remove trailing space
    return spaced_binary_string.strip()


def convert_value(value: int) -> (str, RuntimeMetric):
    """
    Converts a decimal value into a human readable binary string.
    :param value: Integer value in base 10 to convert
    :return: Metrics on algorithm performance
    """
    converter = BaseConverter(32)
    start_time = time_ns()
    binary_string = converter.decimal_to_bin(value)
    end_time = time_ns()
    metric = RuntimeMetric(value, end_time-start_time)
    spaced_binary_string = human_readable_binary_string(binary_string)
    return spaced_binary_string, metric


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads decimal values from an input file and writes them as binary to an
    output file.
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    """
    total_conversions = 0
    next_line = input_file.readline()
    metrics = []
    while next_line is not None and next_line != "":
        try:
            value = int(next_line)
        except ValueError:
            print(f'Error parsing "{next_line} for integer', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

        if value < 0:
            output_file.write("Negative number\n")
            a = 67
        elif value >= 2 ** 32:
            output_file.write("Over 32 Bits\n")
        else:
            output_binary_string, runtime_metric = convert_value(value)
            output_file.write(output_binary_string)
            output_file.write('\n')
            metrics.append(runtime_metric)
            total_conversions += 1


    output_file.write("\n")
    for metric in metrics:
        output_file.write(f"{metric.get_size()} = "
                          f"{metric.get_runtime()}ns\n")
    output_file.write("\n")
