'''
class person
'''

class Person:
    def __init__(self, name, surname, age, sex, children):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.childrens = self.children_name(children)

    def children_name(self, children_quantity):
        childrens = {}            
        for i in range(children_quantity):
            children = {}
            children_name = ''
            children_surname = ''
            children_name = input('Type de name of your children {}: '.format(i))
            children_surname = input('Type de surname of your children {}: '.format(i))
            children['name'] = children_name
            children['surname'] = children_surname
            childrens[i] = children
            
        return childrens
