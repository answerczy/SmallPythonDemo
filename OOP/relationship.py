from datetime import date

#类间关系依赖
class project:
    def __init__(self,name,team,start_date):
        self.name = name
        self.team = team
        self.start_date = start_date

    def __repr__(self):
        return '<Project:{}>'.format(self.name)


class Developer:
    def __init__(self,name,skills,department):
        self.name = name
        self.skills = skills
        self.department = department
        self.department.employees.append(self)

    def __repr__(self):
        return '<Developer:{}>'.format(self.name)


    def develop_project(self,project):
        print('{} is developing {}'.format(self.name,project))

class Department:
    def __init__(self,name,manager,tel):
        self.name = name
        self.manager = manager
        self.tel = tel
        self.employees = []
    def __repr__(self):
        return ('<Department:{}>'.format(self.name))

if __name__ == '__main__':

    dpt = Department('技术部','mike',8888)
    print(dpt)

    d = Developer('tom',['python','sql','flask'],dpt)
    d = Developer('mike',['Django','sql'],dpt)
    print(dpt.employees)
    # print(d)
    # print(d.department.tel)
    # p1 = project('OA','DEV02',date(2017,3,4))
    # d.develop_project(p1)


