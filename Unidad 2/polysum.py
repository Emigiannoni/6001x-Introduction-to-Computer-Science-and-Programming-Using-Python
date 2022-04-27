def polysum(n, s):
    '''
    n = int, number of sides of the polygon
    s = int or float, length of each side
    Returns the sumum of the area and square of the perimeter of the regular polygon.
    '''
    from math import tan, pi
    
    def area(n, s):
    
        return (.25 * n * s * s) / (tan(pi / n))
    
    def perimeter(n,s):
    
        return n * s
        
    return round(area(n,s) + perimeter(n,s)**2, 4)