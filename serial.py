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

    def __init__(self, start):
        """ Initialize the generator and set start/next """
        self.start = self.next = start

    def __repr__(self):
        """ Show the representation of SerialGenerator"""
        return f'<SerialGenerator start={self.start} next={self.next}>'

    def generate(self):
        """ Return the next number in the sequence """
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """ Reset the number to what start was inisialized as"""
        self.next = self.start
        


