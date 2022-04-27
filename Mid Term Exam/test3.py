def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''

    count_values = {}

    result = []

    def obtenerkey(number, mydict):

        for key, value in mydict.items():
        
            if number == value:
                
                return key

    for key in aDict:

        if aDict[key] not in count_values:

            count_values[aDict[key]] = 0

    for key in aDict:

        count_values[aDict[key]] +=1

    for number in count_values:

        if count_values[number] == 1:

            key = obtenerkey(number, aDict)

            result.append(key)



aDict = {8: 1, 0: 4, 1: 1, 5: 2, 9: 4}

print(uniqueValues(aDict))