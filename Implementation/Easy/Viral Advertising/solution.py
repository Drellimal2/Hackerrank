a = int(input().strip())
r = 2
l = 4
for i in range(1, a):
    h = (l//2) * 3
    r += h//2
    l = h
print(r)