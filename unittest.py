class Node:
    ingredient = ''
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    amountresulted = 0
    amountresultedqueue = [] #use this to test the math function
    """address nodes"""
    parentNode = None
    childrenNodes = []

    def __init__(self, I='', P=None, on_hand=0, made_per_craft=0, needed_per_craft=0):
        """Default Node Constructor"""
        self.ingredient = I
        self.parentNode = P
        if (self.parentNode != None):
            self.parentNode.childrenNodes.append(self)
        self.amountresulted = 0
        self.amountneededpercraft = needed_per_craft
        self.amountmadepercraft = made_per_craft
        self.amountonhand = on_hand
        self.childrenNodes = []
        self.amountresultedqueue = [] 
            
    
def searchforendpoints(a=Node):
    """search for endpoint nodes"""
    if len(a.childrenNodes) == 0:
        recursivearithmetic(a)
    else:
        for b in a.childrenNodes:
            if (isinstance(a, Node)):
                searchforendpoints(b)

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
        D = currentNode.amountresulted
        currentNode.parentNode.amountresultedqueue.append(D)
    """recursive function call """
    currentNode.amountresulted = D
    if (currentNode.parentNode != None):
        recursivearithmetic(currentNode.parentNode)
def printresultedamount(subjectNode = Node):
    searchforendpoints(subjectNode)
    print(subjectNode.ingredient,'amount resulted:',subjectNode.amountresulted)
"""beginning program"""
print('\x1B[32mBeginning Process\x1B[37m')
"""create nodes"""
#! (A:amount on hand ,B:amount mader per craft,C:amount needed per craft)
Focusing_Array = Node('Focusing Array',None,1,1,0)
Advanced_Alloy = Node('Advanced Alloy',Focusing_Array,8,1,2)
Crystal = Node('Crystal',Focusing_Array,640,1,2)
Plasmic_Crystal = Node('Plasmic Crystal',Focusing_Array,41,2,2)
Quantum_Processor = Node('Quantum Processor',Focusing_Array,20,2,1)
Zerchesium_Bar = Node('Zerchesium Bar',Advanced_Alloy,548,1,1)
Zerchesium_Ore = Node('Zerchesium Ore',Zerchesium_Bar,2,1,2)
Protocite_Bar = Node('Protocite Bar',Advanced_Alloy,277,1,1)
Protocite_Ore = Node('Protocite Ore',Protocite_Bar,2,1,2)
Penumbrite_Shard = Node('Penumbrite Shard',Advanced_Alloy,86,1,1)
Penumbrite_Ore = Node('Penumbrite Ore',Penumbrite_Shard,2,1,2)
Lead = Node('Lead',Advanced_Alloy,251,1,1)
Crystal_Plant_Seed = Node('Crystal Plant Seed',Crystal,100,1,1)
Blood_Rock = Node('Blood Rock',Plasmic_Crystal,1000,1,50)
Blood = Node('Blood',Blood_Rock,23,1,1)
Lava = Node('Lava',Blood_Rock,404,1,1)
Silicon_Board = Node('Silicon Board', Quantum_Processor, 310, 1, 4)  
Copper_Wire = Node('Copper Wire', Silicon_Board, 492, 9, 1)
Silicon = Node('Silicon', Silicon_Board, 1000, 1, 1)
Copper_Bar = Node('Copper Bar', Copper_Wire, 1000, 1, 1)
Copper_Ore = Node('Copper Ore', Copper_Bar, 2, 1, 2)
Sand = Node('Sand', Silicon, 901, 1, 50)
printresultedamount(Focusing_Array)
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')