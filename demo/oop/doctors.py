from abc import ABC, abstractmethod


class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print('Name:', self.name)
        print('Dept:', self.dept)

    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def show(self):
        super().show()
        print('Salary:', self.salary)

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def show(self):
        super().show()
        print('Visits:', self.visits)
        print('Charge:', self.charge)

    def getsalary(self):
        return self.visits * self.charge


rd = ResidentDoctor("Dr. Deans", "Ortho", 500000)
rd.show()

cd = Consultant("Dr. James", "Card", 10, 2000)
cd.show()

print(rd.getsalary(), cd.getsalary())
