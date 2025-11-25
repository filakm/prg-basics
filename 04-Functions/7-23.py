#A valid password should consist of at least six characters and each character appears only once in the password.
# Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

def f(password):
    if len(password) >= 6:
        count = 0
        while count <=0:
            for char in password:
                if str(password).count(char) > 1:
                    count +=1
            if count > 0:
                return False
            else:
                return True
                

    else:

        return False
    
print(f('666666'))

#f("ax15") returns False
#f("book123") returns False
##f("A2water3") returns True
#("qwerty") returns True
#f(""