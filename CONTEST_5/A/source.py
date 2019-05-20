def print_peng(N):
    peng_pattern = [r"   _~_    ",
                    r"  (o o)   ",
                    r" /  V  \  ",
                    r"/(  _  )\ ",
                    r"  ^^ ^^   "]
    for line in peng_pattern:
        print(line*N)

N = int(input())
print_peng(N)
