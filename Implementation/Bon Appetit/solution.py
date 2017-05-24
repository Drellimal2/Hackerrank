n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
bill = int(input())
if (s-a[k])/2 == bill:
    print("Bon Appetit")
else:
    print(bill - (s-a[k])//2)