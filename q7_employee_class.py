"""Write a program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary. 
Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. 
Allow the user of your program to see the list of employees and their details as well. Try to use the concept of try/except too in the program"""

import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [
            self.empid,
            self.name,
            self.address,
            self.contact_number,
            self.spouse_name,
            self.number_of_child,
            self.salary
        ]

def write_employee_to_file(employee, filename="employees.csv"):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee.to_list())
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_employees_from_file(filename="employees.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            print("\n--- Employee List ---")
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Contact: {row[3]}, "
                      f"Spouse: {row[4]}, Children: {row[5]}, Salary: {row[6]}")
    except FileNotFoundError:
        print("No employee data found yet.")
    except Exception as e:
        print(f"Error reading file: {e}")

def get_employee_input():
    try:
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        contact_number = input("Enter Contact Number: ")
        spouse_name = input("Enter Spouse Name: ")
        number_of_child = int(input("Enter Number of Children: "))
        salary = float(input("Enter Salary: "))
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except ValueError:
        print("Invalid input! Please enter the correct data types.")
        return None

def main():
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            emp = get_employee_input()
            if emp:
                write_employee_to_file(emp)
                print("Employee added successfully.")
        elif choice == '2':
            read_employees_from_file()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
