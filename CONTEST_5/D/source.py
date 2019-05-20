def check_length(line):
    return len(line) >= 8

def check_unique_symbols(line):
    line = set(line)
    return len(line) >= 4

def check_anna_word(line):
    line = line.lower()
    return line.find("anna") == -1

def check_register(line):
    lowercase_exists = False
    uppercase_exists = False
    for i in line:
        if ord(i) in range(ord('a'),ord('z')+1):
            lowercase_exists = True
        if ord(i) in range(ord('A'),ord('Z')+1):
            uppercase_exists = True
    return lowercase_exists and uppercase_exists

def check_numbers(line):
    for i in line:
        if ord(i) in range(ord("0"),ord("9")+1):
            return True
    return False

line = input()
if check_length(line) and check_unique_symbols(line) and check_numbers(line) \
        and check_anna_word(line) and check_register(line):
    print("strong")
else:
    print("weak")
