def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    a = 0
    u = len(s)
    while u>i:
        if s[i].isdigit():
            a += 1
        i += 1
    return a

print(main("python 2022")) 