from datetime import  datetime
# def hello():
#     print('codeclassroom.com')
#     print('python learning')
#     print('Copyright')
# hello()
# print('-'*20)
# hello()

# def Hello():
#     print('hello')
#     return '111'
# print(Hello())  #打印Hello()函数返回的结果，即return的结果,b不返回值，打印None

# def get_current_time():
#     print(datetime.now())
# get_current_time()
# #返回平方
# def sqare(x):
#     return x **2
# print('平方值是：{}'.format( sqare(21)))
# print('平方值是：',sqare(23))

#
#函数变量的作用域只存在函数本地的范围
# x = 5      #global
# def func():
#     global x  #声明此处的x为全局的变量x
#     x = 100   #函数内的变量不影响全局变量，local
#     print(x+10)
# print(x)    # 5
# func()      #110
# print(x)    #5

#函数的嵌套
#
#def fun_a():
#     y = 100
#     def fun_b():
#         nonlocal y #嵌套函数内层函数使用外层函数的变量，使用nonlocal进行声明
#         y = 99
#         print(y+5)
#     print(y) #100
#     fun_b()  #104
#     print(y)  #100
# fun_a()

# #带参位置函数
# def Hello(a,b,c):
#     print('a={} b={} c={}'.format(a,b,c))
#
# Hello(1,45,2)
# Hello(c=6,a=33,b=22)
# #带参默认值参数
# def fun_c(a,b,c=11):   #位置参数和默认值参数
#     print('a={} b={} c={}'.format(a,b,c))
# fun_c(22,11)

#任意参数  平均值计算
# def avg_number(a,*args):     #args 当做元组处理
#     return (a+sum(args))/(len(args)+1)
# print('%.2f'%(avg_number(1,33,42,11,32,12)))
# print('{:12.2f}'.format(avg_number(43,23,53,64,33,13,53)))

def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
print(outer(5,4))

