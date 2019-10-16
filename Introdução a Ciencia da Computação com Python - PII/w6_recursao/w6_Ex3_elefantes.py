def incomodam(n):
    if n < 0:
        return ''
    if n > 0:
        if n == 1:
            return 'incomoda '    
        return 'incomodam ' + incomodam(n-1)
    
print(incomodam(5))