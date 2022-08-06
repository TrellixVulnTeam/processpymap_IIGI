class Node:
    ingredient = ''
    amountonhand = 0
    amountneededpercraft = 0
    amountmadepercraft = 0
    amountresulted = 0
    amountresultedqueue = []  # use this to test the math function
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
        A = eval(input('How much \x1B[33m' +  str(self.ingredient) + '\x1B[37m do you have on hand: '))
        B = 0
        while B == 0:
            B = int(input('How much \x1B[33m' +  str(self.ingredient) + '\x1B[37m do you create each time you craft it: ')) 
            
        C = 1
        self.amountonhand = A
        self.amountmadepercraft = B
        if self.parentNode != None:
            C = int(input('How much \x1B[33m' + str(self.ingredient) + '\x1B[37m do you need to create \x1B[34m' + str(self.parentNode.ingredient) +'\x1B[37m:'))
            self.amountneededpercraft = C
    def traceback(self, output=False):
        """output trail"""
        if output == True:
            print('TRAIL: ', end='')
        if self.parentNode != None:
            print(self.ingredient, '-> ', end='')
        else:
            print('\x1B[35m', self.ingredient, '\x1B[37m')

        if self.parentNode != None:
            self.parentNode.traceback()
    def searchforendpoints(self):
        """search for endpoint nodes"""
        if len(self.childrenNodes) > 0:
            for childNode in self.childrenNodes:
                childNode.searchforendpoints()
        else:
            recursivearithmetic(self)
    def returnresultedamount(self):
        self.searchforendpoints()
        return self.amountresulted


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
        D = currentNode.amountonhand//(currentNode.amountneededpercraft *
                                       currentNode.amountneededpercraft)
    """recursive function call """
    if (currentNode.parentNode != None):
        recursivearithmetic(currentNode.parentNode)
    currentNode.amountresulted = D


def populate(currentNode=Node):
    """populate each node with subnodes"""
    inputqueue = []
    if currentNode.parentNode != None:
        currentNode.traceback(True)
    print('What ingredients do you need to create',currentNode.ingredient,': ')
    while True:
        i = input('')
        if (len(i) > 0):
            inputqueue.append(i)
        else:
            break
    if len(inputqueue) > 0:
        for nodeName in inputqueue:
            temp = Node(nodeName,currentNode)
            temp.inputnumerics()
    if len(currentNode.childrenNodes) > 0:
        """recursive function call"""
        for newNode in currentNode.childrenNodes:
            populate(newNode)


"""beginning process"""
print('\x1B[32mbeginning process\x1B[37m')
itemname = input('What is the name of the item you want to create: ')
head = Node(itemname, None)
head.inputnumerics()
populate(head)
print('The amount of',head.ingredient,'possible for you to create with all these values is: \x1B[32m',head.returnresultedamount())
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')
