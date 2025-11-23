def month(n):
    result = ''
    if n == 1:
        result = 'Januaru'
    elif n == 2:
        result = 'Febuary'
    elif n == 3:
        result = 'March'
    elif n == 4:
        result = 'April'
    elif n == 5:
        result = 'May'
    elif n == 6:
        result = 'June'
    elif n == 7:
        result = 'July'
    elif n == 8:
        result = 'August'
    elif n == 9:
        result = 'September'
    elif n == 10:
        result = 'October'
    elif n == 11:
        result = 'November'
    elif n == 12:
        result = 'December'
    return result
def main():
    x=5
    print(f'month number {x} is {month(x)}')
if __name__ == "__main__":
    main()