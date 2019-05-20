a = input().split()
for i in range(1, int(a[0]) + 1):
    for j in range(1, int(a[1]) + 1):
        print(i*j, end=" ")
    print()
