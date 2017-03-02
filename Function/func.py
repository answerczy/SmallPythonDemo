# def avg_num(a,*args):   #args 可为任意名，  * 为元组处理， **为字典表处理
#     print('平均数是：',(sum(args)+5)/(len(args)+1))
# avg_num(4,32,312,4234)
#
# def func(a,*args,**kwargs):    #**为字典表处理
#     print(a,args,kwargs)
#
# func(20,30,40,50)    #20 (30, 40, 50) {}
# func(232,44,55,name='tom',age=20)   #232 (44, 55) {'age': 20, 'name': 'tom'}
#
# emp = {'name':'jimmy','salary':434}
# func(32,423,5345,42,**emp)   #232 (44, 55) {'age': 20, 'name': 'tom'}



# x = 5
# def change_num(x):
#     x += 10
#     print(x)
#
# print(x)
# change_num(x)   #不可变类型对象函数传递副本（函数内操作不影响原始值）值传递，传递的值得副本
# print(x)


l =[1,2,3]
def changelist(x):  #传递副本  def change-list(l.copy())    def change_list(l[:])  第一个到最后一个数字
    x[0] = 99
    print(x)
print(l)
changelist(l)  #可变类型对象向函数传递对象引用（函数内操作会影响原始操作），为引用传递，传递的值的引用
print(l)