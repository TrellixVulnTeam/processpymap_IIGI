class node:
    usedtocreate = None
    createdfrom = []
    """stores data within each part of the structure"""
    ingredient = ''
    amountonhand = 0.00
    amountmadepercraft = 0.00
    amountneededpercraft = 0.00

    def __init__(myself, ingredient_name='', next=None):
        """default constructor"""
        myself.usedtocreate = next
        myself.ingredient = ingredient_name
        myself.amountonhand = 0.00
        myself.amountmadepercraft = 0.00
        myself.amountneededpercraft = 0.00
    def __del__(myself):
        """default deconstructor"""
        print('deleted', myself.ingredient, 'from the tree')
    def baz_tentative(myself,parent_ingredient = ''):
        """setter for numeric variables"""
        #todo test this out 
        if not len(parent_ingredient) == 0:
            myself.amountneededpercraft = float(input('What is the amount of',myself.ingredient,'needed to create',parent_ingredient,': '))
            myself.amountneededpercraft = round(myself.amountneededpercraft, [0])
        myself.amountonhand = float(input('What is the amount of',myself.ingredient,'that you have on hand: '))
        myself.amountonhand = round(myself.amountonhand, [0])
        myself.amountmadepercraft = float(input('What is the amount of',myself.ingredient,'made per craft: '))
        myself.amountmadepercraft = round(myself.amountmadepercraft, [0])

def foo_tentative(foo_Node=node):
    """add subingredient nodes to A"""
    print('What items do you need to create\x1B[35m', foo_Node.ingredient,
          '\x1B[37m,leave your input blank to stop inputting')
    foo_nodelist = [] #list for nodes
    
    while (True):
        input_string = input('')
        if (len(input_string) == 0):
            break
        else:
            foo_nodelist.insert(0, input_string)
    if len(foo_nodelist) > 0:
        for Node in foo_nodelist:
            temp = node(Node, foo_Node)
            foo_Node.createdfrom.insert(0, temp)
        for subingredient in foo_Node.createdfrom:
            foo_tentative(subingredient)


"""begininng of main script"""
Z = input('What is the name of the item you want to create: ')
head = node(Z, None)
foo_tentative(head)
"""terminating process"""
print('\x1B[31mtermiating process\x1B[37m')
