N = int(input())
answer = 1

for i in range(N):
    isSimple = False
    while not isSimple:
        answer += 1
        isSimple = True
        for j in range(2, int(answer**0.5) + 1):
            if answer % j == 0:
                isSimple = False
print(answer)
