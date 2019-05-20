N = int(input())
a = 0
b = 1
if N == 0:
    print(a)
else:
    if N == 1:
        print(b)
    else:
        for i in range(2, N+1):
            c = b
            b += a
            a = c
        print(b)
