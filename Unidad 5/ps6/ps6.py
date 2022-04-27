import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string).
        '''

        # ciphering lowercase letters

        lowercase = string.ascii_lowercase

        shitf_dict_lower = {}

        i = 0

        for letter in lowercase:

            shitf_dict_lower[letter] = i

            i += 1

        for key in shitf_dict_lower:

            if (shitf_dict_lower[key] + shift) < len(lowercase):

                shitf_dict_lower[key] = lowercase[shitf_dict_lower[key] + shift]

            else:

                shitf_dict_lower[key] = lowercase[shitf_dict_lower[key] + shift - 26]



        # ciphering uppercase letters

        uppercase = string.ascii_uppercase

        shitf_dict_upper = {}

        i = 0

        for letter in uppercase:

            shitf_dict_upper[letter] = i

            i += 1

        for key in shitf_dict_upper:

            if (shitf_dict_upper[key] + shift) < len(uppercase):

                shitf_dict_upper[key] = uppercase[shitf_dict_upper[key] + shift]

            else:

                shitf_dict_upper[key] = uppercase[shitf_dict_upper[key] + shift - 26]


        shitf_dict_lower.update(shitf_dict_upper)

        shift_dict = shitf_dict_lower

        return  shift_dict



    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        message = self.message_text

        ciph_message = []

        shift_dict = self.build_shift_dict(shift)

        for character in message:

            if character in shift_dict.keys():

                ciph_message.append(shift_dict[character])

            else:

                ciph_message.append(character)


        StrA = "".join(ciph_message)

        return StrA




class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''

        Message.__init__(self, text)

        self.shift = shift

        self.encrypting_dict = self.build_shift_dict(shift)

        self.message_text_encrypted = self.apply_shift(shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''

        return self.shift


    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''

        dict_copy = self.encrypting_dict.copy()

        return dict_copy


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        self.shift = shift

        self.encrypting_dict = self.build_shift_dict(shift)

        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text

        self.valid_words = load_words(WORDLIST_FILENAME)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        valid_words_counter = {}

        # inicializa el diccionario:

        for i in range(27):

            valid_words_counter[i] = 0

        # ejecuta apply_shift usando como shift cada key del diccionario:

        for i in range(27):

            decrypted_message = self.apply_shift(26 - i)

            decrypted_word_list = decrypted_message.split(' ')

            counter = 0

            for word in decrypted_word_list:

                if is_word(self.valid_words, word):

                    counter += 1

            valid_words_counter[i] = counter

        for key in valid_words_counter.keys():

            if key == 0:

                best = valid_words_counter[0]

            elif valid_words_counter[key] > best:

                best = valid_words_counter[key]
            
        for key, value in valid_words_counter.items():
                
                if best == value:
                    
                    shift_value = key

                    break

        decrypted_message = self.apply_shift(26 - shift_value)

        if (26 - shift_value) < 26:

            answer = (26 - shift_value, decrypted_message)

        else:

            answer = (0, decrypted_message)

        return answer




#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


def decrypt_story():

    text = get_story_string()

    message = CiphertextMessage(text)

    decrypted_message = message.decrypt_message()

    print(decrypted_message)


decrypt_story()