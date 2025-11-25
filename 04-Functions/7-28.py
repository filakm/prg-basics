#The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the 
# number of dice rolled the most times in a row. Sample result:
def f(dice):
    if not dice:
        return None

    max_run_length = 0
    current_run_length = 0
    longest_run_face = None
    current_face = None
    
    for face in dice:
        if face == current_face:
            current_run_length += 1
        else:
            if current_run_length > max_run_length:
                max_run_length = current_run_length
                longest_run_face = current_face
            current_face = face
            current_run_length = 1
    
    # Check the last run in the sequence
    if current_run_length > max_run_length:
        longest_run_face = current_face
        
    return int(longest_run_face)

print(f("5233165554211"))