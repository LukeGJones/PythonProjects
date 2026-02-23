intext = str(input("Enter: "))
textList = []
outtext = ""
for i in range(len(intext)):
    textList.append(intext[i])

letter = 0
while letter < (len(textList)):
    if(textList[letter].isalpha() == False and textList[letter].isspace() == False): #Remove the second condition to remove spaces too
        textList.pop(letter)
        letter -= 1
    letter += 1

for i in range(len(textList)):
    outtext = outtext + str(textList[i])
print(outtext)