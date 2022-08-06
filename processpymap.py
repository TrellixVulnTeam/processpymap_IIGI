from tkinter.messagebox import NO


class Node:
    ingredient = ''
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    amountresulted = 0
    amountresultedqueue = []  # use this to test the math function
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
    def inputnumerics(self):
        """input the numeric data for the node"""
        self.amountonhand = int(input('How much',self.ingredient,'do you have on hand: '))
        self.amountmadepercraft = int(input('How much',self.ingredient,'do you create each time you craft it: '))
        if self.parentNode != None:
            self.amountneededpercraft = int(input('how much',self.ingredient,'do you need to create',self.parentNode.ingredient))
    def traceback(self,output = False):
        """output trail"""
        if output == True:
            print('TRAIL: ',end='')
        if self.parentNode != None:
            print(self.ingredient,'-> ',end='')
        else:
            print(self.ingredient)
        
        if self.parentNode != None:
            self.parentNode.traceback()

def recursivearithmetic(currentNode=Node):
    """ 
    A = amount on hand
    B = amount made per craft
    C = amount needed
    D = amount on hand for new node (D^P = E^C + A^P)
    E = amount resulted
    Equation for when B = 1: D = A/(B*C)
    Equation for when B > 1: = D^P = D^C * B^P + A^P (C,child & P,parent) 
    #? expected amount on Silicon Board is 1328
    """
    D = 0
    if currentNode.parentNode == None and len(currentNode.childrenNodes) > 0:
        """Node Type: Head"""
        """solve for D"""
        if len(currentNode.amountresultedqueue) == 1:
            D += currentNode.amountresultedqueue[0]
        else:
            D += min(currentNode.amountresultedqueue)
        D += currentNode.amountonhand
        currentNode.amountresulted = D

    elif currentNode.parentNode != None and len(currentNode.childrenNodes) > 0:
        """Node Type: Body"""
        """solve for D"""
        if len(currentNode.amountresultedqueue) == 1:
            D += currentNode.amountresultedqueue[0]
        else:
            D += min(currentNode.amountresultedqueue)
        D += currentNode.amountonhand
        """peform math function"""
        if (currentNode.amountmadepercraft > 1):
            currentNode.parentNode.amountresultedqueue.append(
                (D*currentNode.parentNode.amountmadepercraft)+currentNode.amountonhand)
        else:
            currentNode.parentNode.amountresultedqueue.append(
                D//(currentNode.amountmadepercraft * currentNode.amountneededpercraft))

    elif currentNode.parentNode != None and len(currentNode.childrenNodes) == 0:
        """Node Type: Endpoint"""
        """find the amount resulted and input it into a queue of children amount resulted for the direct parent"""
        currentNode.amountresulted = currentNode.amountonhand // (
            currentNode.amountmadepercraft * currentNode.amountneededpercraft)
        currentNode.parentNode.amountresultedqueue.append(
            currentNode.amountresulted)
    else:
        D = currentNode.amountonhand//(currentNode.amountneededpercraft*currentNode.amountneededpercraft)
    """recursive function call """
    if (currentNode.parentNode != None):
        recursivearithmetic(currentNode.parentNode)
    currentNode.amountresulted = D

def populate(currentNode=Node):
    """populate each node with subnodes"""
    if currentNode.parentNode != None:
        currentNode.traceback(True)
    
    if len(currentNode.childrenNodes) > 0:
        """recursive function call"""
        for i in currentNode.childrenNodes:
            populate(i)
"""beginning process"""
print('\x1B[32mbeginning process\x1B[37m')
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
"""oio"""
populate(Focusing_Array)
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')
