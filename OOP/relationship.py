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
    def __init__(self,name,skills):
        self.name = name
        self.skills = skills

    def __repr__(self):
        return '<Developer:{}>'.format(self.name)


    def develop_project(self,project):
        print('{} is developing {}'.format(self.name,project))


if __name__ == '__main__':
    d = Developer('tom',['python','sql','flask'])
    print(d)

    p1 = project('OA','DEV02',date(2017,3,4))
    d.develop_project(p1)


