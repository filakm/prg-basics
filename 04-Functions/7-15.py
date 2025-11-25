#A device in a door registers people entering and leaving a room.The + sign means a person entering a room and the -- sign a person leaving a room. 
# Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:

def f(detector):
    p_in = 0
    plus = '+'
    minus = '-'
    
    for char in detector:
        if 0 <= p_in <= 2:
            if char == plus:
                p_in += 1
            elif char == minus:
                p_in -=1
    if p_in == 3:
        return True
    elif p_in < 3:
            return False
print(f("+-++-++-+---"))
