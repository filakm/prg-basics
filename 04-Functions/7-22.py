#A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:

def f(name):
    words = str(name).split()

    acronym = [word[0].upper() for word in words if word]
    return "".join(acronym)

print(f("Internet of Things"))