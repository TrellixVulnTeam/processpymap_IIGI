import traceback


class Node:
    ingredient = ''
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    amountresulted = 0
    """address nodes"""
    parentNode = None
    childrenNodes = []
    childrenNodes_amountresultedqueue = [] #use this to test the math function

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
        self.childrenNodes_amountresultedqueue = [] #use this to test the math function
    def traceback(self): #? utlility method 
        """prints out a path of node names through their parent's pointer addresses"""
        if self.parentNode == None and len(self.childrenNodes) > 0:                 #head node
            print('\x1B[32m',self.ingredient,'-\x1B[33m>\x1B[37m ',end='')
        elif self.parentNode != None and len(self.childrenNodes) > 0:               #body node
            print('\x1B[36m',self.ingredient,'-\x1B[32m>\x1B[37m ',end='')
        elif self.parentNode != None and len(self.childrenNodes) == 0:              #endpoint
            print('\x1B[35m',self.ingredient,'-\x1B[36m>\x1B[37m ',end='')
        
        if (self.parentNode != None):
            self.parentNode.traceback()
        else:
            print('NONE')
    
def searchforendpoints(a=Node):
    """search for endpoint nodes"""
    if len(a.childrenNodes) == 0:
        print('found endpoint')
        recursivearithmetic(a)
    else:
        for b in a.childrenNodes:
            if (isinstance(a, Node)):
                searchforendpoints(b)
    a.traceback()


def recursivearithmetic(currentNode=Node):
    """ 
    A = amount on hand
    B = amount made per craft
    C = amount needed
    D = amount on hand for new node (D^P = E^C + A^P)
    E = amount resulted
    Equation for when B = 1: D = A/(B*C)
    Equation for when B > 1: = D^P = D^C * B^P + A^P (C,child & P,parent)
    """
    numlist = []  # use this number to find minimum result amounted
    if currentNode.parentNode == None and len(currentNode.childrenNodes) > 0:       # head node
        print('\x1B[32m',currentNode,'\x1B[37m')
        """perform math"""
        for childNode in currentNode.childrenNodes:
            if currentNode.amountmadepercraft == 1:
                E = round(childNode.amountonhand // (childNode.amountmadepercraft * childNode.amountneededpercraft)) 
            else: #todo finish this later 
                E = round((childNode.amountonhand*currentNode.amountneededpercraft)+currentNode.amountonhand)
            numlist.append(E)
            currentNode.amountresulted = min(numlist)
    elif currentNode.parentNode != None and len(currentNode.childrenNodes) > 0:     # body node
        print('\x1B[33m',currentNode,'\x1B[37m')
        """perform math"""
        for childNode in currentNode.childrenNodes:
            if currentNode.amountmadepercraft == 1:
                E = round(childNode.amountonhand // (childNode.amountmadepercraft * childNode.amountneededpercraft))
            else: #todo finish this later 
                E = round((childNode.amountonhand*currentNode.amountneededpercraft)+currentNode.amountonhand)
            numlist.append(E)
            currentNode.amountresulted = min(numlist)
            currentNode.parentNode.amountonhand += (currentNode.amountresulted)
    elif currentNode.parentNode != None and len(currentNode.childrenNodes) == 0:    # endpoint node
        print('\x1B[31m',currentNode,'\x1B[37m')
        """perform math"""
        recursivearithmetic(currentNode.parentNode)
    else:                                                                           # single node in tree
        print('\x1B[36mUNKNOWN\x1B[37m-\x1B[34m', type(currentNode), '\x1B[37m')
        """recursive function call"""

    #a.amountresulted = min(mypynumlist)
    if currentNode.parentNode != None:
        recursivearithmetic(currentNode.parentNode)


# ? expected amount is 1328, copper wire should use the new one and silicon uses the old math formula
"""beginning program"""
print('\x1B[32mBeginning Process\x1B[37m\n')
"""create nodes"""
        #! (A:amount on hand ,B:amount mader per craft,C:amount needed per craft)
Silicon_Board = Node('Silicon Board', None, 310, 1, ) #!leave out the four (310,1,4) 
Copper_Wire = Node('Copper Wire', Silicon_Board, 492, 9, 1)
Silicon = Node('Silicon', Silicon_Board, 1000, 1, 1)
Copper_Bar = Node('Copper Bar', Copper_Wire, 1000, 1, 1)
Copper_Ore = Node('Copper Ore', Copper_Bar, 2, 1, 2)
Sand = Node('Sand', Silicon, 901, 1, 50)
searchforendpoints(Silicon_Board)
print('Silicon Boards amount resulted:', Silicon_Board.amountresulted)
"""terminating process"""
print('\x1B[31mI love you Narieles 💞\nI love you so freaking much you make me happy everyday!\x1B[37m')
