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
    amountresultedqueue = [] #use this to test the math function

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
        self.amountresultedqueue = [] #use this to test the math function
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
        recursivearithmetic(a)
    else:
        for b in a.childrenNodes:
            if (isinstance(a, Node)):
                searchforendpoints(b)
    a.traceback()

def recursivearithmetic(currentNode = Node):
    """ 
    A = amount on hand
    B = amount made per craft
    C = amount needed
    D = amount on hand for new node (D^P = E^C + A^P)
    E = amount resulted
    Equation for when B = 1: D = A/(B*C)
    Equation for when B > 1: = D^P = D^C * B^P + A^P (C,child & P,parent) 
    #? expected amount is 1328
    """  
    D = 0
    if currentNode.parentNode == None and len(currentNode.childrenNodes) > 0:       #?  head node
        """solve for D"""
        if len(currentNode.amountresultedqueue) ==1:
            D += currentNode.amountresultedqueue[0]
        else:
            D += min(currentNode.amountresultedqueue)
        D += currentNode.amountonhand 
        currentNode.amountresulted = D
    elif currentNode.parentNode != None and len(currentNode.childrenNodes) > 0:     #?  body node
        """solve for D"""
        if len(currentNode.amountresultedqueue) ==1:
            D += currentNode.amountresultedqueue[0]
        else:
            D += min(currentNode.amountresultedqueue)
        D += currentNode.amountonhand     
        """peform math function"""
        if (currentNode.amountmadepercraft > 1):
           currentNode.parentNode.amountresultedqueue.append((D*currentNode.parentNode.amountmadepercraft)+currentNode.amountonhand)
        else:
            currentNode.parentNode.amountresultedqueue.append(D//(currentNode.amountmadepercraft * currentNode.amountneededpercraft))
    elif currentNode.parentNode != None and len(currentNode.childrenNodes) == 0:    #?  endpoint node
        """find the amount resulted and input it into a queue of children amount resulted for the direct parent"""
        currentNode.amountresulted = currentNode.amountonhand // (currentNode.amountmadepercraft * currentNode.amountneededpercraft)
        currentNode.parentNode.amountresultedqueue.append(currentNode.amountresulted)
    """recursive function call """
    if (currentNode.parentNode != None):
        recursivearithmetic(currentNode.parentNode)
    currentNode.amountresulted = D

"""beginning program"""
print('\x1B[32mBeginning Process\x1B[37m\n')
"""create nodes"""
        #! (A:amount on hand ,B:amount mader per craft,C:amount needed per craft)
Silicon_Board = Node('Silicon Board', None, 310, 1, 4)  
Copper_Wire = Node('Copper Wire', Silicon_Board, 492, 9, 1)
Silicon = Node('Silicon', Silicon_Board, 1000, 1, 1)
Copper_Bar = Node('Copper Bar', Copper_Wire, 1000, 1, 1)
Copper_Ore = Node('Copper Ore', Copper_Bar, 2, 1, 2)
Sand = Node('Sand', Silicon, 901, 1, 50)
searchforendpoints(Silicon_Board)
print(Silicon_Board.ingredient,'amount resulted:', Silicon_Board.amountresulted)
print(Silicon.ingredient,'amount resulted:', Silicon.amountresulted)
"""terminating process"""
print('\x1B[31mI love you Narieles 💞\nI love you so freaking much you make me happy everyday!\x1B[37m')