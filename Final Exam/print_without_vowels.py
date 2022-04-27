def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    s2_list = []

    for letter in s:

    	if not (letter in vowels):

    		s2_list.append(letter)

    s2 = "".join(s2_list)

    print(s2)


print_without_vowels('This is great!')

print_without_vowels('')

print_without_vowels('a')

