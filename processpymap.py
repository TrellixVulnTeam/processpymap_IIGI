class Node:
    higher = None
    children = []
    name = ""

    def __init__(self, data="", parent=None):
        self.higher = parent
        self.name = data
        self.children = []


def populate(cur_node=Node):
    """create and input nodes into the current node's children"""
    queue = []
    pytempnode = cur_node
    """output the pointer trail (quick and dirty backward traversal)"""
    if (pytempnode.higher != None):
        print('Trail: ', end='')
    while (pytempnode.higher != None):
        print(pytempnode.name, end='')
        pytempnode = pytempnode.higher
        if (pytempnode.higher == None):
            print('')
        else:
            print(' -> ', end='')

    print('Input stuff needed to make\x1B[35m', cur_node.name, '\x1B[37m:')
    while True:
        x = input('')
        x.strip
        if len(x) == 0:
            break
        elif x == cur_node.name:
            print('\x1B[31myou already typed that in\x1B[37m')
        else:
            queue.append(x)
    """input node name"""
    for n in queue:
        """create a new node for every string in the list"""
        temp = Node(n, cur_node)
        cur_node.children.append(temp)
    if len(cur_node.children) > 0:
        """recusrively call this function"""
        for n in cur_node.children:
            populate(n)


"""beginning of main script"""
print('\x1B[32mbeginning process\x1B[37m')
py_A = input('What is the name of the item you want to create: ')
A = Node(py_A, None)
populate(A)

"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')
