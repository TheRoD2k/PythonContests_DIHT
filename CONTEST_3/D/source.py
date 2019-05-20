String = input()
StringOfSymbols = ""
Check = False
for i in range(len(String)):
    if String[i] not in StringOfSymbols:
        StringOfSymbols += String[i]
    else:
        Check = True
        break
print(Check)
