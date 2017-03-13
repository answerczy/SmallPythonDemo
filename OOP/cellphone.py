class Cellphone:
    def __init__(self,brand,price=0.0):
        self.brand = brand
        self.price = price

    def __repr__(self):
        return '<Cellphone:{}>'.format(self.brand)  #控制台输出对象

    def __str__(self):
        return '[Cellphone:{}]'.format(self.brand) #控制台print返回的字符串

    def on(self):
        print('{}手机开机了.....'.format(self.brand))

    def send_message(self,to,message):
        print('{}给{}发送短信，短信内容是：{}'.format(self.brand,to,message))

    def __add__(self, other):
        return self.price+ other.price   #运算符重载

c1 = Cellphone('nokia',4500.3)
c1.on()
c1.send_message('jim','i want to study python!')
c2 = Cellphone('IPHONE',4343)

print(c1+c2)
c1

Cellphone.on(c1) #通过类调用的时候传入实例对象