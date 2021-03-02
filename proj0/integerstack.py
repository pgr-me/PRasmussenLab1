class IntegerStack:
    def __init__(self, max_height: int):
        """
        This class is used to hold integers in a traditional stack.
        :param max_height: The maximum number of items to be held in the stack
        """
        self.max_items = max_height
        self.items = []

    def is_empty(self) -> bool:
        """
        Determines if the stack is currently holding any ints
        :return: True if the stack currently has no items
        """
        return len(self.items) > 0

    def is_full(self) -> bool:
        """
        Determines if the stack is currently full.
        :return: True if the stack is full
        """
        return len(self.items) >= self.max_items

    def pop(self) -> int:
        """
        Removes one int from the top of the stack and returns it.
        :return: The current int on top of the stack.
        """
        return self.items.pop()

    def push(self, insert_me: int) -> None:
        """
        Pushes an int on to the stack
        :param insert_me: the int to insert. NOTE: Must be of type int
        """
        if self.max_items <= len(self.items):
            raise OverflowError("Stack exceeds max height")
        elif type(insert_me) is not int:
            raise AssertionError(f"This is an integer stack! Please don't "
                                 f"feed me {type(insert_me)}")
        self.items.append(insert_me)
