class node:
    parent = None
    children = []
    """single data node of ingredient data tree"""
    ingredient = ""
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    isheadnode = True
    def __init__(myself,nodename = "",next = None):
        """default constructor for node"""
        myself.ingredient = nodename
        myself.parent = next
        myself.isheadnode = not myself.parent == None
    def __del__(myself):
        """default deconstructor for node"""
        print('Destroying Node',myself.ingredient)
    def bar_tentative(myself):
        """setter for amountmade per craft and amount on hand"""
        print(myself.ingredient)
        pass
    def foo_tentative():
        """figures out the amount resulted the tree"""
        print('pass')
        pass
    def baz_tentative():
        """search for endpoints of this data tree then perform foo_tentative()"""
        pass
def foo_tentative(foo_node = node):
    """populuate children nodes"""
    print('what ingredients do you need to create',foo_node.ingredient)
    inputqueue = []
    foo_input = ""
    while True:
        """input loop for ingredients in parent node"""
        foo_input = input('INPUT: ')
        if len(foo_input) == 0:
            break
        else:
            inputqueue.insert(0,foo_input)
    if len(inputqueue) > 0:
        for string in inputqueue:
            """create and populate children for the parent node"""
            foo_tempnode = node(string,foo_node)
            foo_node.children.insert(0,foo_tempnode)
        for newnode in foo_node.children:
            """recursive call for populating nodes"""
            foo_tentative(newnode)
    

        
head = node
head.ingredient = 'head'
foo_tentative(head)
"""terminating process"""
print('terminating process')
