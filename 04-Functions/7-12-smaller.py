def f(n):
    if n <= 0:
        return ""
    asterisk = "*" *n
    return "/".join(asterisk)

print(f(4))