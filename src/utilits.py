### Imports
# Standard library

# Third-party libraries

# Local files


def convert_to_float(string: str) -> float:
    """
    Convert a string to a float.
    
    e.x. given the strin `"0,282"`, then `convert_to_float` will return the float `0.282`.
    
    Parameters
    ----------
    string : str
        The string which will be converted to a float
        
    Returns
    -------
    float
        The converted string
    
    Raises
    ------
    ValueError
        If the input string cannot be converted to a float.

    """
    try:
        return float(string.replace(",", "."))
    except ValueError:
        raise ValueError(f"Could not convert '{string}' to float.")