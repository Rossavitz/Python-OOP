"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Starts generator at default 0, start is 0, next is 0 as we haven't called it to be 1 yet."""
        self.start = start
        self.next = start

    def generate(self):
        """Adds 1 to next and returns next - 1. ie 0 + 1, return 0 as its the first number."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """reset the generator to default start"""
        self.next = self.start
