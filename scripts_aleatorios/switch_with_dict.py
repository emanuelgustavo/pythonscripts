# Because Python has first-class functions they can
# be used to emulate switch/case statements

#with if statements
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

#with dict
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
        }.get(operator, lambda: None)()


def test():
    print('dispatch_if, mul, 2, 3')
    print(dispatch_if('mul', 2,3))
    print('dispatch_if, add, 2, 3')
    print(dispatch_if('add', 2,3))
    print('dispatch_if, div, 2, 3')
    print(dispatch_if('div', 2,3))
    print('dispatch_if, sub, 2, 3')
    print(dispatch_if('sub', 2,3))
    
    print('dispatch_dict, mul, 2, 3')
    print(dispatch_dict('mul', 2,3))
    print('dispatch_dict, add, 2, 3')
    print(dispatch_dict('add', 2,3))
    print('dispatch_dict, div, 2, 3')
    print(dispatch_dict('div', 2,3))
    print('dispatch_dict, sub, 2, 3')
    print(dispatch_dict('sub', 2,3))
    
test()
    
