import functools
scores = [55,78,66,56,90,89,77]

# scores = [i + 2 for i in scores]
# print(scores)

#遍历出数组每个元素加3   map()函数使用
result = []
for x in scores:
    result.append(x+3)
print(scores)
print(result)

def fun(y):
    return y+2

for s in map(fun,scores):
    print(s)

print (map(lambda x: x % 2, range(7)))



print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
