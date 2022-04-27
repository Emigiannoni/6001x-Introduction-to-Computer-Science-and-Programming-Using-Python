class myDict(object):

    """ Implements a dictionary without using a dictionary """

    def __init__(self):
    
        """ initialization of your representation """
        
        self.key = []

        self.value = []

        
    def assign(self, k, v):
        
        """ k (the key) and v (the value), immutable objects  """
        
        if not (k in self.key):

            self.key.append(k)

            self.value.append(v)

        else:

            i = self.key.index(k)
            
            self.value[i] = v

        
    def getval(self, k):

        """ k, immutable object  """

        try:

            i = self.key.index(k)

            return self.value[i]

        except:

            raise KeyError("Key doesn't in the dictionary")


        
    def delete(self, k):
        
        """ k, immutable object """   
        
        try:

            i = self.key.index(k)

            self.key.pop(i)

            self.value.pop(i)

        except:

            raise KeyError("Key doesn't in the dictionary")


d1 = myDict()

d1.assign(1,2)
d1.assign(3,4)
d1.assign(3,5)
print(d1.getval(3))

