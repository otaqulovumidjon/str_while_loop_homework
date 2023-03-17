def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    h = 0
    u = len(s)
    while u>i:
        if s[i].isupper():
            h += 1
        i += 1
    return h

print(main("CodeschoolUz")) 