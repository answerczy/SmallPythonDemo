def hello():
    print('hello python!')
hello()

gretting = lambda :print('hello lambda')  #lambda表达式返回一个function对象 要执行加括号，名称可选
print(type(gretting))
gretting()

action = lambda a,b:a+b  #冒号左边写参数，右边是返回值，不用return关键字。
print(action(2,4))


#平方与立方之和
def fun(x):
    print(x**2 +x**3)
fun(4)

def fucti(x):
    f1 = lambda x:x**2
    f2 = lambda x:x**3
    print(f1(x)+f2(x))
fucti(3)


# 依次打印加减乘除
a ,b =5,6
func_list = [lambda x,y:x+y,lambda x,y:x-y,lambda x,y:x*y,lambda x,y:x/y]
for i in func_list:
    print(i(a,b))

#通过操作符打印加减乘除

operation = 's'
bb = 55
cc =44
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
action = {
    'a':add,
    's':subtract,
    'm':lambda x,y:x*y,
    'd':lambda x,y:x/y
}

print(action.get(operation,add)(bb,cc))

#使用传入的操作函数进行计算
def calculate(bb,cc,ff):
    return ff(bb,cc)
print('---------',calculate(bb,cc,add))   #--------- 99
print('---------',calculate(bb,cc,lambda bb,cc:bb*cc ))   #--------- 2420