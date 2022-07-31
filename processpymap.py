class node:
    usedtocreate = None
    createdfrom = []
    """stores data within each part of the structure"""
    ingredient = ''
    def __init__(myself,ingredient_name = '\x1B[32mmonty python\x1B[37m',next = None):
        myself.usedtocreate = next
        myself.ingredient = ingredient_name 
    def __del__(myself):
        print('deleted',myself.ingredient,'from the tree')
"""begininng of main script"""
Z = input('What is the name of the item you want to create: ')
head = node(Z,None)

"""terminating process"""
print('terminating process')
