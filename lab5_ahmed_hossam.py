import psycopg2

# Database connection parameters
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "2022",
    "host": "localhost",
    "port": "5432"
}


def db_connect():
    return psycopg2.connect(**DB_PARAMS)


def create_employee_table():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            age INTEGER,
            department VARCHAR(100),
            salary REAL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


class Employee:
    all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        Employee.all_employees.append(self)
        self.insert_to_db()

    def insert_to_db(self):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employee (first_name, last_name, age, department, salary)
            VALUES (%s, %s, %s, %s, %s)
        ''', (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()
        cursor.close()
        conn.close()

    def transfer(self, new_department):
        self.department = new_department
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employee
            SET department = %s
            WHERE first_name = %s AND last_name = %s
        ''', (new_department, self.first_name, self.last_name))
        conn.commit()
        cursor.close()
        conn.close()

    def fire(self):
        if self in Employee.all_employees:
            Employee.all_employees.remove(self)
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM employee
            WHERE first_name = %s AND last_name = %s
        ''', (self.first_name, self.last_name))
        conn.commit()
        cursor.close()
        conn.close()

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, "
              f"Department: {self.department}, Salary: {self.salary}")

    @staticmethod
    def list_employees():
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        print("\nEmployees in database:")
        for row in rows:
            print(row)
        cursor.close()
        conn.close()


class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        self.managed_department = managed_department
        super().__init__(first_name, last_name, age, department, salary)

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, "
              f"Department: {self.department}, Salary: Confidential, "
              f"Manages: {self.managed_department}")


################################################################

def command_interface():
    create_employee_table()
    print("Welcome to the Employee Management System!")

    while True:
        print("\nMenu:")
        print("add - Add new employee or manager")
        print("list - List all employees")
        print("q - Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            role = input("If manager press 'm', if employee press 'e': ").strip().lower()
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))

            if role == 'e':
                emp = Employee(first_name, last_name, age, department, salary)
                print("Employee added.")
            elif role == 'm':
                managed_department = input("Managed Department: ")
                mgr = Manager(first_name, last_name, age, department, salary, managed_department)
                print("Manager added.")
            else:
                print("Invalid role. Please enter 'e' or 'm'.")

        elif choice == "list":
            Employee.list_employees()

        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# To run:
# command_interface()

