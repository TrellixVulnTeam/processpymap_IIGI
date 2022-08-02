class Node:
    """stores data for data trees of composing of just instances of this class"""
    parent = None
    children = []
    name = ''

    def __init__(myself, A='', B=None):
        """default constructor for instance"""
        myself.name = A
        myself.parent = B
    def __del__(myself):
        """default deconstructor for instance"""
        print('Bye bye',myself.name)
def nani_tentative(nani = Node):
    """add nodes into children's list"""
    string_input = []
    print('What ingredients do you need to create\x1B[35m',nani.name,'\x1B[37mleave blank to stop inputting: ')
    while (True):
        x = input('')
        if len(x) == 0:
            break;
        else:
            string_input.insert(0,x)
    if not len(string_input) == 0:
        for string in string_input:
            ariana = Node(string,nani)
            nani.children.insert(0,ariana)
        for node in nani.children:
            nani_tentative(node)
"""beginning of main script"""
head = Node('Narieles')
nani_tentative(head)
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')
