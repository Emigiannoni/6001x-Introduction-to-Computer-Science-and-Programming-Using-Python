def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''

    result = []

    for element_i in aDict:

        counter = 0

        for element_j in aDict:

            if aDict[element_i] == aDict[element_j]:

                    counter += 1

        if counter == 1:  

            result.append(element_i)

    return result

aDict = {0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3}

print(uniqueValues(aDict))