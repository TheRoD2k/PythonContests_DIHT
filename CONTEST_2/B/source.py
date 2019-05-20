N = input()
a = N
b = N
found = False
while not found:
    if int(a[0]) + int(a[1]) + int(a[2]) == \
            int(a[3]) + int(a[4]) + int(a[5]):
        print(a)
        found = True
    else:
        if int(b[0]) + int(b[1]) + int(b[2]) == \
                int(b[3]) + int(b[4]) + int(b[5]):
            print(b)
            found = True
    a = str(int(a) - 1)
    for i in range(len(a), 6):
        a = "0" + a
    b = str(int(b) + 1)
    for i in range(len(b), 6):
        b = "0" + b
