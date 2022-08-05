from re import search
from typing import Optional
from xml.etree.ElementInclude import include


class Node:
    ingredient = ''
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    amountresulted = 0
    """address nodes"""
    parentNode = None
    childrenNodes = []

    def __init__(self, I='', P=None, A=0, B=0, C=0):
        """Default Node Constructor"""
        self.ingredient = I
        self.parentNode = P
        if (self.parentNode != None):
            self.parentNode.childrenNodes.append(self)
        self.amountresulted = 0
        self.amountneededpercraft = C
        self.amountmadepercraft = B
        self.amountonhand = A
        self.childrenNodes = []


def searchforendpoints(a=Node):
    """search for endpoint nodes"""
    if len(a.childrenNodes) == 0:
        print('found endpoint')
        recursivearithmetic(a)
    else:
        for b in a.childrenNodes:
            if (isinstance(a, Node)):
                searchforendpoints(b)


def recursivearithmetic(a=Node):
    """ 
    A = amount on hand
    B = amount made per craft
    C = amount needed
    D = amount on hand for new node (D^P = E^C + A^P)
    E = amount resulted
    Equation for when B = 1: D = A/(B*C)
    Equation for when B > 1: = D^P = D^C * B^P + A^P (C,child & P,parent)
    """
    mypynumlist = []  # use this number to find minimum result amounted
    if a.parentNode == None and len(a.childrenNodes) > 0:       # head node
        print('head node:\x1B[32m', a, '\x1B[37m')
        """perform math"""
    elif a.parentNode != None and len(a.childrenNodes) > 0:     # body node
        print('body node:\x1B[33m', a, '\x1B[37m')
        """perform math"""
    elif a.parentNode != None and len(a.childrenNodes) == 0:    # endpoint node
        print('endpoint node:\x1B[31m', a, '\x1B[37m')
        """perform math"""
    else:# single node in tree
        print('\x1B[36mUNKNOWN\x1B[37m-\x1B[34m', type(a), '\x1B[37m')
        """recursive function call"""
    if a.parentNode != None:
        a.parentNode.amountneededpercraft += a.amountneededpercraft
        recursivearithmetic(a.parentNode)


# ? expected amount is 1328, copper wire should use the new one and silicon uses the old math formula
"""beginning program"""
print('\x1B[32mBeginning Process\x1B[37m\n')
"""create nodes"""
Silicon_Board = Node('Silicon Board', None, 310, 1, 4)
Copper_Wire = Node('Copper Wire', Silicon_Board, 492, 9, 1)
Silicon = Node('Silicon', Silicon_Board, 1000, 1, 1)
Copper_Bar = Node('Copper Bar', Copper_Wire, 1000, 1, 1)
Copper_Ore = Node('Copper Ore', Copper_Bar, 2, 1, 2)
Sand = Node('Sand', Silicon, 901, 1, 50)
searchforendpoints(Silicon_Board)
print('Silicon Boards amount resulted:', Silicon_Board.amountresulted)
"""terminating process"""
print('\x1B[31mI love you Narieles 💞\x1B[37m')
