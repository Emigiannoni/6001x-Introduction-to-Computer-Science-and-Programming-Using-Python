t = (5, (1,2), [[1],[2]])

def is_int(element):

    try:

        int(element)

        respuesta = True

    except:

        respuesta = False

    return respuesta


def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 

    maximum_value = 0

    for element in t:

        if is_int(element):

            if element > maximum_value:

                maximum_value = element

        else:

            a = max_val(element)

            if a > maximum_value:

                maximum_value = a

    return maximum_value


print(max_val(t))