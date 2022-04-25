stringToChange: str = str(input('the string is -> '))
valueTochange: str = str(input('introduce value to change -> '))
valuesTochanges = []
valuesToReplaces = []

searchValue = stringToChange.find(valueTochange)

if searchValue == -1:
    print("Value is not in the string")

elif searchValue > -1:
    ValueReplace: str = str(input('introduce the value replace -> '))

valuesTochanges[:0] = valueTochange
valuesToReplaces[:0] = ValueReplace

print(valuesTochanges)
print(valuesToReplaces)

ValueOne = len(valuesTochanges) - 1
print(ValueOne)
ValueTow = len(valuesToReplaces) - 1
print(ValueTow)

for i in valuesTochanges:

    newString = stringToChange.replace(valuesTochanges[ValueOne],valuesToReplaces[ValueTow])
    count = len(valuesTochanges) - 1
    if count < 0:
        break

print(newString)