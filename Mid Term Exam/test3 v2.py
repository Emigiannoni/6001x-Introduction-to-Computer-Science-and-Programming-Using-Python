def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    maped_values = []

    result = []

    for element in aDict:

        if aDict[element] not in maped_values:

            maped_values.append(aDict[element])

            counter = 0

            for elements in aDict:

                if element == elements:

                    counter += 1

            if counter == 1:  

                result.append(element)

    return result

aDict = {8: 1, 0: 4, 1: 1, 5: 2, 9: 4}

print(uniqueValues(aDict))