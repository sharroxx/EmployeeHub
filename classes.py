class Employee:  # main class
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):  # to input instance attributes
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property  # property decorator to convert said method to an attribute
    def fullname(self):  # to return the full name of the employee
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    @property  # property decorator to convert said method to an attribute
    def email(self):  # to return the email address of the employee
        return '{}.{}@company.com'.format(self.first, self.last)

    def apply_raise(self):  # to incremet the salary of the employee by a said percent
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):  # used to compute string representation the employee details
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):  # returns the full name and the email
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):  # to add one employees pay with another(operator overloading)
        return self.pay + other.pay

    def __len__(self):  # to find length of fullname(operator overloading even though len is a built in function)
        return len(self.fullname())


class Developer(Employee):  # subclass of Employee
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay) Another way to call init function
        self.prog_lang = prog_lang


class Manager(Employee):  # another subclass of employee

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):  # to add employee to the list of employees under the manager
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):  # to remove employee to the list of employees under the manager
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):  # to print the list of employees under the manager
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('john', 'wick', 600000)

dev_1 = Developer('sharvesh', 'srinivasan', 50000, 'python')
dev_2 = Developer('test', 'user', 60000, 'java')

mgr_1 = Manager('sue', 'smith', 90000, [dev_1])

emp_1.fullname = 'Corey Schafer'

print(emp_1.email)

del emp_1.fullname

print(emp_1.email)
