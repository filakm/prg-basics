#A sentence is an ordered group of words separated by spaces. 
# Define a function f(sentence) that returns a sentence with spaces removed. Sample result:

def f(sentence):
    # Replace all occurrences of ' ' with '' (an empty string)
    return str(sentence).replace(' ', '')
print(f("integrated development environment"))