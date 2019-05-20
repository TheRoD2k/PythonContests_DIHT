N = int(input())

for i in range(1, N + 1):
    if i % 15 == 0:
        print("Fizz Buzz", end="")
    else:
        if i % 3 == 0:
            print("Fizz", end="")
        else:
            if i % 5 == 0:
                print("Buzz", end="")
            else:
                print(i, end="")
    if i < N:
        print(", ", end="")
