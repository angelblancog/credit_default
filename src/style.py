def highlight_fraud(val: str):
    """Show potential fraud in red, Normal in green, and Dangerous zone in yellow.

    Args:
        val (str): The value in the 'Result' column.

    Returns:
        str: CSS style string specifying the text color.
    """    
    if val == 'Potential fraud':
        color = 'red'
    elif val == 'Normal':
        color = 'green'
    elif val == 'Danger zone':
        color = 'orange'
        
    return f'color: {color}'