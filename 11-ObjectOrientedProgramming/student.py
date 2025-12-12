# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.index = 0
def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.index = 123456
    student2.name = "Olivia"
    student2.age = 21
    student2.index = 654321
    student3.age = 20
    student3.name = "Morgan"
    student3.index = 987654

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, index number: {student1.index}, {student1.age} years old')
    print(f'{student2.name}, index number: {student2.index} {student2.age} years old')
    print(f'{student3.name}, index number:{student3.index}, {student3.age} years old')

if __name__ == "__main__":
    main()