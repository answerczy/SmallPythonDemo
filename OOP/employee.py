"""
类的继承
支持多继承
"""

class Employee:
    def __init__(self,name,department,title,salary):
        self.name = name
        self .department =department
        self.title =title
        self.salary = salary

    def __repr__(self):
        return '<员工：{}>'.format(self.name)

    def working(self):
        print('{} is working on ...'.format(self.name))

class Developer(Employee):
    def __init__(self,name,department,title,salary,skills):
        Employee.__init__(self,name,department,title,salary)
        self.skills = skills

    def coding(self):
        print('Developer {} is coding....'.format(self.name))

    def working(self):
        super().working()   #super此处要加括号
        print('developer is working on...')

class Accountant(Employee):
    def __init__(self,name,department,title,salary,certification):
        Employee.__init__(self,name,department,title,salary)
        self.certification = certification

    def acounting(self):
        print('财务人员{}正在记账'.format(self.name))


if __name__ == '__main__':
    d = Developer('Tom','dev02','sr engineer',8000,['python','oracle','java'])
    print(d.name)
    d.working()
    d.coding()

    a = Accountant('marry','finance','senior AC',12000,'registration')
    print(a.certification)
    a.working()
    a.acounting()