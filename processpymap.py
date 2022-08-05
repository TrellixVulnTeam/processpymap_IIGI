from re import A
from tkinter import N


class Node:
    ingredient = ""
    amountonhand = 0
    amountpercraft = 0
    amountneededpercraft = 0
    prevNode = None
    nextNode = []

    def __init__(self, A='', B=None):
        """default constructor"""
        self.ingredient = A
        self.prevNode = B
        self.amountonhand = -1
        self.amountpercraft = -1
        self.amountneededpercraft = -1

    def joo(self):
        for j in self.nextNode:
            print(j)


def populate(A=Node):
    i = ''
    l = []
    """subingredients"""
    print('Type in ingredients needed to make',A.ingredient,':')
    while (True):
        i = input('')
        if len(i) == 0: 
            break
        elif len(i) > 0 and len(l) > 0:
            repeated = False
            for j in l:
                repeated = i == j
                if repeated:
                    break
            if repeated:
                print('')
            else:
                l.append(i)
    if len(l) > 0:
        for m in l:
            B = Node(m,A)
            A.nextNode.append(B)
"""beginning of main script"""
print('\x1B[32mbeginning process\x1B[37m')
a = Node('Node A')
populate(a)
"""terminating process"""
print('\x1B[31mterminating process\x1B[37m')
