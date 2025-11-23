def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100
def cm_to_i(n):
    return n*2.54
def f_i_to_cm(n,m):
    return n*30 + m*2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'3cm = {cm_to_i(3)}inches')
    print(f'5 feet and 6 inches = {f_i_to_cm(5,6)}cm')
