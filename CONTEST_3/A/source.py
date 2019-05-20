Input = input().split()
FrequencyList = []
ListOfWords = []
for i in range(len(Input)):
    if Input[i].lower() in ListOfWords:
        FrequencyList[ListOfWords.index(Input[i].lower())] += 1
    else:
        ListOfWords.append(Input[i].lower())
        FrequencyList.append(1)
print(max(FrequencyList) / len(Input))
