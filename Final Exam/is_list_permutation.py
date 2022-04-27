def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''

    # Check if the lists have the same number of elements:

    if len(L1) != len(L2):

        return False

    # If both lists are empty return the tuple (None, None, None):

    if len(L1) == 0:

        if len(L2) == 0:

            return (None, None, None)

    # Check if list elements appear the same number of times in both lists:

    L1_dict = {}
    L2_dict = {}

    for e in L1:

        L1_dict[e] = L1_dict.get(e,0) + 1

    for e in L2:

        L2_dict[e] = L2_dict.get(e,0) + 1    


    for key in L1_dict.keys():

        if not (key in L2_dict.keys()):

            return False

        if L1_dict[key] != L2_dict[key]:

            return False

    # element occuring the most times and how many times that element occurs

    max_value = 0

    max_key = None

    for key in L1_dict.keys():

        if L1_dict[key] > max_value:

            max_value = L1_dict[key]

            max_key = key

    # the type of the element that occurs the most times

    max_type = type(max_key)

    return (max_key, max_value, max_type)


L1 = []

L2 = []

print(is_list_permutation(L1, L2))