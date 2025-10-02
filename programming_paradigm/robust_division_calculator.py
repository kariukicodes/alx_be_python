def safe_divide(numerator, denominator):
    try:
        # convert inputs to floats (may raise ValueError)
        num = float(numerator)
        den = float(denominator)
        try:
            result = num / den  # may raise ZeroDivisionError
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
