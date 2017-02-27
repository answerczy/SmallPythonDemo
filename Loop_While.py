# i = 0
# while i >=1:
#     print('{}的平方值是：{}'.format(i,i**2))
#     i -=1
# name = ['tom','jerry','mike']
# while i < len(name):
#     print(name[i])
#     i += 1
# while True:
#     x = input("请输入一个数字：")
#     if x == 'stop':
#         break
#    x = int(x)
#     print('{}的平方是：{}'.format(x,x**2))


# x = 0
# while x <10:
#     x += 1
#     if x == 1:
#         break
#     print(x)
# else:
#     print('loop end!')



# stu = ['tom','jerry','mike']
# flag = False
# i = 0
# while i < len(stu):
#     if 'j' in stu[i]:
#         flag = True
#         pass
#     i += 1
# if(flag):
#     print('yes')
# else:
#     print('no')

i = 0
stu = ['tom','jerry','mike']
while i < len(stu):
    if 'e' in stu[i]:
        break
    i += 1
else:
    print('no word')
