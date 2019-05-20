String = input()
Length = int(input())
ListOfSubstrings = []
FrequencyList = []
OutputList = []
for i in range(len(String) - Length + 1):
    Substring = String[i: i + Length]
    if Substring in ListOfSubstrings:
        FrequencyList[ListOfSubstrings.index(Substring)] += 1
    else:
        FrequencyList.append(1)
        ListOfSubstrings.append(Substring)
for i in range(len(FrequencyList)):
    if FrequencyList[i] > 1:
        OutputList.append(ListOfSubstrings[i])
OutputList.sort()
print(OutputList)
