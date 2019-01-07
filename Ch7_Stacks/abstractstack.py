from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """An abstract stack implementation"""
    def __init__(self,sourceCollection = None):
        AbstractCollection.__init__(self,sourceCollection)

    def add(self,item):
        """Adds item to self"""
        self.push(item)




