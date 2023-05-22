def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    else:
        if a >= c:
            return a
        elif c >= b:
            return b
        else:
            return c
