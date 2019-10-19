def incomodam(n):
    if n < 0:
        return ''
    if n == 1:
        return 'incomodam '
    if n > 1:   
        return 'incomodam ' + incomodam(n-1)
    
def elefantes(n, music=''):
    '''
    if n <= 0:
        return ''
    else:
        if n == 1:
            music += ('Um elefante incomoda muita gente\n')
            return music
        else:            
            music += ('{} elefantes '.format(n) + 'incomodam muita gente\n')
            music += ('{} elefantes '.format(n) + incomodam(n) + 'muito mais\n')
            return music + elefantes(n-1)
    '''
    #by LUCCAS ESPER KLOTZ
    if n < 0:
        return ''
    if n < 1:
        return 'a'
    if n == 1:
        return "Um elefante incomoda muita gente\n"    
    return elefantes(n-1) + str(n) + " elefantes " +  incomodam(n) + "muito mais\n" + str(n) + " elefantes incomodam muita gente\n"
    
#print(elefantes(3))
