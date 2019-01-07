from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    """An array-based bag implementation"""


    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        AbstractCollection.__init__(self,sourceCollection)


    def __str__(self):
        """Return the string implementation of self."""
        return "{" + ",".join(map(str, self)) + "}"

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True





