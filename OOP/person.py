import datetime
import OOP.utility
class Person:

    count = 0
    people = []
    def __init__(self,name='',birthday='',gender='',salary = 0):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.get_salary = salary
        #self._salary
        #Person.count += 1 #计算实例化对象的次数
        Person.people.append(self)

    @property
    def get_salary(self):
        return self._salary1  #此处的salary1位为临时变量

    @get_salary.setter
    def get_salary(self,value):
        if value <= 0:
            self._salary1 = 0
        else:
            self._salary1 = value

    def get_age(self):
        return datetime.date.today().year - self.birthday.year #返回到当前的年份- 生日的年份

    @property    #python内置的装饰器
    def age(self):
        return datetime.date.today().year - self.birthday.year

    @age.setter #对方法进行赋值计算的时候的逻辑处理
    def age(self,value):
        raise ValueError('年龄不能进行赋值')
        # print('你赋的值是',value)
        # print('年龄不允许赋值，年龄通过生日计算')



    def say(self,word):
        print('{} 说：{}!'.format(self.name,word))

    def __str__(self):  #魔法函数
        return '<Person:{},{},{},{}>'.format(self.name,self.birthday,self.gender,self.get_salary)

        #Python3.6 return f'<Person:{self.name},{self.birthday},{self.gender}>'
    def __repr__(self):
        return '[Person:{},{},{},{}]'.format(self.name,self.birthday,self.gender,self.get_salary)


    @classmethod   #关键字定义类方法
    def print_all_people(cls):   #带参数self为实例方法
        OOP.utility.Utility.conndb()

        print(Person.people)



p1 = Person('MIKE',datetime.date(1993,8,22),'MALE',5000)
p2 = Person('tom',datetime.date(1991,2,3),'MALE',8000)
#p1.get_salary=-3434
print(p1)
# print(p1.age)
# print(Person.people)
#p1.say('i want to learn python')
Person.print_all_people()  #括号内不加实例名称



