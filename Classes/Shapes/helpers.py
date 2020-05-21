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

def checkProperty(value,single=False):
    """
    Checks an input for (int,float). Returns a boolean.
    If a list of arguments provided, checks each argument
    in list for type (int,float)
    """
    if isinstance(value,(tuple,list)) and not single:
        for item in value:
            if isinstance(item,(tuple,list)):
                raise Exception(f"Argument of type {type(item)} not allowed.")
            checkProperty(item)
        return
    if not isinstance(value,(int,float)):
        raise Exception("Property must be set to (int,float)")
    if value <= 0:
        raise Exception("Property can't be set <= 0")
    