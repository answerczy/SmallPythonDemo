score =50
if score > 90:
    print('youxiu')
elif score >80:
    print('lianghao')
elif score < 60:
    print('bujike')
else:
    print('jige')


lang = 'kr'
greeing = {'cn':'你好','en':'hello','ru':'dada'}

print(greeing.get(lang,'bucunzai'))
