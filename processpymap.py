class Node:
    """stores data for data trees of composing of just instances of this class"""
    parent = None
    children = []
    name = ''
    amountonhand = 0.00
    amountpercraft = 0.00
    amountneededpercraft = 0.00
    def __init__(myself, A='', B=None):
        """default constructor for instance"""
        myself.name = A
        myself.parent = B
        myself.amountonhand = 1.00
        myself.amountpercraft = 0.00
        myself.amountneededpercraft = 1.00
    def __del__(myself):
        """default deconstructor for instance"""
        print('Bye bye',myself.name)
    def ariana_tentative(myself,parentingredient = ""):
        """function to input numeric input"""
        myself.amountonhand = int(input('Amount on hand: '))
        myself.amountpercraft = int(input('Amount created per craft: '))
        if not len(parentingredient) == 0:
            myself.amountneededpercraft = int(input('Amount need per craft',parentingredient,': '))
def nani_tentative(nani = Node):
    """add nodes into children's list"""
    string_input = []
    py_A = nani.name
    print('What ingredients do you need to create\x1B[35m',py_A,'\x1B[37mleave blank to stop inputting: ')
    while (True):
        x = input('')
        if len(x) == 0:
            break;
        else:
            string_input.insert(0,x)
            """check for duplicates"""
            #todo add script to check for duplicate inputs 
    if not len(string_input) == 0:
        for string in string_input:
            ariana = Node(string,nani)
            """input numeric data here"""
            #ariana.amountonhand = int(input('Amount on hand for ',ariana.name,': '))
            #ariana.amountpercraft = int(input('Amount created per craft',ariana.name,': '))
           #ariana.amountneededpercraft = int(input('Amount need per craft',py_A,': '))
            nani.children.insert(0,ariana)
        for node in nani.children:
            nani_tentative(node)
"""beginning of main script"""
head = Node('Narieles')
nani_tentative(head)
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')