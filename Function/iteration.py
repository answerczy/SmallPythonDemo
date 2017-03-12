scores = [22,3,4,55,34,21,43]
i = iter(scores)
while True:
    try:
        s = next(i)  #h或者使用 s=i.__next__()
    except StopIteration:
        break
    print(s)