"""Create a class Student with the attributes such as id, name, address, admission year, level, section. 
Instantiate the object of class to take input for all the attributes and display the output."""

class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.address = ""
        self.admission_year = ""
        self.level = ""
        self.section = ""

    def input_data(self):
        self.id = input("Enter Student ID: ")
        self.name = input("Enter Student Name: ")
        self.address = input("Enter Address: ")
        self.admission_year = input("Enter Admission Year: ")
        self.level = input("Enter Level (e.g., 11, 12, etc.): ")
        self.section = input("Enter Section: ")

    def display_data(self):
        print("\n--- Student Details ---")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Example usage
if __name__ == "__main__":
    student = Student()
    student.input_data()
    student.display_data()
