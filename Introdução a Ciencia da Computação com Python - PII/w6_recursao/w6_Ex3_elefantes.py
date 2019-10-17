def incomodam(n):
    if n == 1:
        return 'incomodam '
    if n > 1:   
        return 'incomodam ' + incomodam(n-1)
    
def elefantes(n, string=''):
    if n < 0:
        return ''
    else:
        if n == 1:
            string += ('Um elefante incomoda muita gente\n') 
            return string
        else:            
            string += ('{} elefantes '.format(n) + 'incomodam muito gente\n')
            string += ('{} elefantes '.format(n) + incomodam(n) + 'muito mais\n')
            return string + elefantes(n-1)
        
print(elefantes(3))