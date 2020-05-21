"""
A collection of helper functions for the Shapes module.
"""

def checkInput2D(values):
        """
        Checks an input for type (list,tuple), and checks elements in either
        for (int,float). Returns a boolean.
        """
        if isinstance(values, (list,tuple)):
            if len(values) > 2:
                return False
                
            check = []

            for item in values:
                check.append(isinstance(item,(int,float)))

            return all(check)
        else:
            return False
