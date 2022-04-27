def count7(N):
    '''
    N: a non-negative integer
    '''

    print('Valor de N: ' + str(N))

    print('Valor de %N: ' + str(N % 10))

    if N == 0:

        return 0

    elif N % 10 == 7:

        return 1 + count7(N // 10) 

    else:

        return 0 + count7(N // 10)


N = 710783377

print('resultado final: ' + str(count7(N)))

