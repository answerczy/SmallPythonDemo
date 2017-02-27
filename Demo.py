# score =50
# if score > 90:
#     print('youxiu')
# elif score >80:
#     print('lianghao')
# elif score < 60:
#     print('bujike')
# else:
#     print('jige')
#
#
# lang = 'kr'
# greeing = {'cn':'你好','en':'hello','ru':'dada'}
#
# print(greeing.get(lang,'bucunzai'))
num = [1,22,4,65,31,32,6,7,3,20]
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
    print(num)