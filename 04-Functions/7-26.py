#Define a function f(text) that returns the given text with all 
# characters separated by a dash sign. 
# Example:

def f(text):
    txt = str(text).split()
    if text == "":
        return text
    for char in txt:
        split = "-".join(char)
    return split

print(f('dame'))