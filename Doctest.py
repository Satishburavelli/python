def add(a,b):
    """
    Returns the sum of a and b
    >>> add(5,3)
    8
    >>> add(8,3)
    11
    >>> add(2.3,23)
    25.3
    """
    return a+b
if __name__ == "__main__":
    import doctest
    doctest.testmod()