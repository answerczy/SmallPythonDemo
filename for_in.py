name = ['tom','jerry','mike']
#name = 'www.baidu.com'
#name = ('bibi',3.232,[32,32,'stu'],(3,4))
# names =[i + '\n' for i in name]
# print(names)
# for i in name:
#     print(i)

# emp = {'name':'tom','salary':4324,'age':49}
# for k,v in emp.items():
#     print(k, v)


#同时遍历序列和打印下标
for i,s in enumerate(name):
    print(i,s)

# for i in range(len(name)):
#     print(i,name[i])

# i = 0
# for x in name:
#     print(i,x)
#     i += 1