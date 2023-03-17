def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    h = 0
    u = len(s)
    while u>i:
        if s[i].isalpha():
            h += 1
        i += 1
    return h

print(main("Python 2022"))