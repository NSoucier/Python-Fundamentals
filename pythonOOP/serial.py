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
        """Create serial number starting from 'start'"""
        self.start = start - 1
        self.next = start - 1
    
    def __repr__(self):
        """Show representation"""
        return f'<SerialGenerator start={self.start+1} next={self.start + 2}>'
    
    def generate(self):
        """Generates next sequential number"""
        self.next += 1
        return self.next
    
    def reset(self):
        """Resets sequence back to start"""
        self.next = self.start
        
    
    

