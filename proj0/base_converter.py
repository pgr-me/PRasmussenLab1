from proj0.integerstack import IntegerStack


class BaseConverter:
    def __init__(self, num_digits: int):
        """
        Creates a BaseConverter object
        :param num_digits: Number of digits allowed for conversion result
        """
        self.num_digits = num_digits

    def decimal_to_bin(self, dec_num: int) -> str:
        """
        Convert Decimal numbers to binary numbers.
        :param dec_num: The decimal number to convert
        :return: The bit patter of the 32-bit binary number.
        """
        int_stack = IntegerStack(self.num_digits)
        next_num = dec_num
        total_bits = 0
        while next_num > 0:
            # Note python scopes to functions, not loops
            remainder = next_num % 2
            int_stack.push(remainder)
            total_bits += 1
            next_num //= 2

        binary_buffer = ""
        for i in range(total_bits):
            binary_buffer += f"{int_stack.pop()}"
        return binary_buffer
