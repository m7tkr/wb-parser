# python oop


class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # this is class var, so access it appropriately

    def __init__(self, first, last, pay):
        # runs every time new instance created

        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1
        # self.num_of_emps is not suitable
        # due to num_of_emps has to stay constant to this class

    @property  # propery getter to access like an attribute, not method
    def fullname(self):  # don't forget to include self
        return f"{self.first} {self.last}"

    @fullname.setter  # able to set fullname as a setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}@{self.last}.sa"

    def apply_raise(self):  # self is autopassed into instance
        # self.raise_amount also works
        # above usage gives ability to change single instance values

        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):   # cls is convention
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):  # cls is auto passed into func

        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # use static w/in class if you don't use class or inst vari
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):

    # 1st checks Developer __init__
    # 2nd goes to Employee
    # this is called MRO (method resolution order)

    raise_amount = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)  #also availbale / multipar
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)  #also availbale / multipar

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp1 = Employee('mhmmd', 'slmn',  5000)
emp2 = Employee('abkr', 'omar',  6000)

emp_str_1 = 'slmn-fysl-2000'
emp_str_2 = 'srh-frhd-1100'

dev1 = Developer('rmzn', 'hmmd', 2000, 'Python')
dev2 = Developer('asad', 'bashr', 3000, 'Java')

mgr1 = Manager('mhmd', 'ryd', 7000, [dev1])

# -------------------
emp1.fullname = 'fysl ahmd'
print(emp1.fullname)

# emp1.first = 'frhd'
#
# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())
# -------------------

# -------------------
# print(len(emp1))  # __len__ method
# print(emp1 + emp2)  # here __add__ is used
#
# print(1 + 2)
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# print(repr(emp1))
# print(str(emp1))
#
# print(emp1.__repr__())
# print(emp1.__str__())

# print(emp1)
# -------------------
# -------------------

# -------------------
# print(isinstance(mgr1, Manager))  # dev and mgr will give false
# print(issubclass(Manager, Employee))  # checks classes

# mgr1.add_emp(dev2)
# mgr1.remove_emp(dev1)
# mgr1.print_emps()

# print(dev2.prog_lang)
# dev1.apply_raise()
# print(dev1.pay)

# print(help(Developer))  # check for MRO

# print(dev1.email)
# -------------------

# -------------------
# import datetime
# my_date = datetime.date(2002, 11, 30)
#
# print(Employee.is_workday(my_date))

# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_2.email)
#
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, 'some', pay)
# print(new_emp_1.email)

# Employee.set_raise_amount(1.12)
# Employee.raise_amount = 1.12  # same as above
# emp1.set_raise_amount(1.17)  # changes apply to the class

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# -------------------

# -------------------
# emp1.first = 'mhmmd'
# emp1.second = 'slmn'
# emp1.email = 'mhmmd@slmn.sa'

# emp2.first = 'abkr'
# emp2.second = 'slmn'
# emp2.email = 'abkr@slmn.sa'

# Employee.fullname(emp1)  # same as below
# emp1.fullname()  # same as above
# print(emp1.fullname())
# -------------------

# -------------------
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(Employee.__dict__)  # Employee class has raise_amount in dict
# print(emp1.__dict__)  # check emp1 doen't have raise_amount
#
# Employee.raise_amount = 1.05  # changes raise amount of every instamce
#
# emp1.raise_amount = 1.1  # changes raise_amount only of emp1 instance
# print(emp1.__dict__)  # new method of raise_amount created after above exe
#
# print(Employee.raise_amount)  # checks class scope first, then global
# print(emp1.raise_amount)  # 1st check emp1 instance, then class scope
# print(emp2.raise_amount)

# print(Employee.num_of_emps)
# -------------------
