Keys = list(input())
Letters = list(input())
Dict = {}
if len(Keys) <= len(Letters):
    for i in range(len(Keys)):
        Dict[Keys[i]] = Letters[i]
else:
    for i in range(len(Letters), len(Keys)):
        Dict[Keys[i]] = None
    for i in range(len(Letters)):
        Dict[Keys[i]] = Letters[i]
print(list(sorted(Dict.items())))
