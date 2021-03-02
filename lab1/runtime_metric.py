"""Peter Rasmussen, Lab 1, stack.py"""

class RuntimeMetric:
    def __init__(self, size: int, time_ns: float):
        """
        Holds data to determine Big-O runtime metrics.
        :param size: Size of the problem
        :param time_ns: Duration of the solution
        """
        self.size = size
        self.time = time_ns

    def get_runtime(self) -> float:
        """
        Fetches the time it took to solve the problem.
        :return: The time measured in nanoseconds
        """

        return self.time

    def get_size(self) -> int:
        """
        Fetches the size of the problem.
        :return: A size that is determined by the way the problem is stated.
        """
        return self.size
