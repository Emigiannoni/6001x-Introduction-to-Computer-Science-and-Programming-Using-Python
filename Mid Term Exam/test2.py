def lessThan4(aList):
    '''
    aList: a list of strings
    '''

    lenght = []

    results = []

    for word in aList:

        lenght.append(len(word))

    for i in range(len(lenght)):

        if lenght[i] < 4:

            results.append(aList[i])

    return results

aList = ["apple", "cat", "dog", "banana"]

print(lessThan4(aList))
