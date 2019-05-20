def check_if_poly(line):
    for i in range(0, len(line)//2):
        if line[i] != line[len(line)-1-i]:
            return False
    return True

def remove_first_symbol(line):
    new_line = ""
    for i in range(1, len(line)):
        new_line += line[i]
    return new_line

def find_minimum_addition(line):
    addition = line[::-1]
    answer = len(line)
    for i in range(len(line)+1):
        if check_if_poly(line + addition):
            answer = len(line)-i
        addition = remove_first_symbol(addition)
    return answer

line = input()
answer = min(find_minimum_addition(line), find_minimum_addition(line[::-1]))
print(answer)
