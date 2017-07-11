s, e, k = map(int, input().strip().split(' '))
count = 0
for x in range(s, e +1):
    dif = abs(x - int(str(x)[::-1]))
    if dif % k == 0:
        count += 1
print(count)