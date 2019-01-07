class Baginterface(object):
    """Interface for all bag types"""

    #Constructor
    def __init__(self,sourceCollection = None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        pass

    def isEmpty(self):
        """Return True if len(self) == 0,else False."""
        pass

    def __len__(self):
        """Return the number of item in self"""
        return 0

    def __str__(self):
        """Return the string implementation of self."""
        return 0

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        return None

    def __eq__(self, other):
        """Return True if self equals other,or False otherwise."""
        return False

    def clear(self):
        """makes self become empty."""
        pass

    def add(self,item):
        """Adds item to self."""
        pass

    def remove(self,item):
        """Remove item from self.
        Precondition: item is in self.Raises:KeyError if item is not in self.
        Postcondition: item is removed from self"""
        pass



