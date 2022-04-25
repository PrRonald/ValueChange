stringToChange = "A+B+C*Y" #<string input

valuesTochanges = ["+", "*"] 
valuesToReplaces = ["|", "&"]

#count the elements in the list for parameters that replace method take
ValueOne = len(valuesTochanges) - 1 
ValueTow = len(valuesToReplaces) - 1

for i in valuesTochanges:

    #replace method, the argument are the ValueOne and ValueTow
    newString = stringToChange.replace(valuesTochanges[ValueOne],valuesToReplaces[ValueTow])
    count = len(valuesTochanges) - 1

    # when the list of the change value and replace value end this condition end the for loop
    if count < 0:  
        break

print(newString)

#investigae a desktop aplication for manage
#evalue the error and solve error inputs