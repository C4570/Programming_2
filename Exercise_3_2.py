class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)
    
def treePreOrder(tree):
    if tree == None:
            return
        
    print(tree.cargo)
    treePreOrder(tree.left)
    treePreOrder(tree.right)
        
def treeInOrder(tree):
    if tree == None:
        return
    
    treeInOrder(tree.left)
    print(tree.cargo)
    treeInOrder(tree.right)
  
def treePostOrder(tree):
    if tree == None:
        return
    
    treePostOrder(tree.left)
    treePostOrder(tree.right)
    print(tree.cargo)
  
tree = Tree(8, Tree(4, Tree(2,Tree(1), Tree(3)), Tree(7)), Tree(15, Tree(17), Tree(20,Tree(19),Tree(22))))
#        ___8___
#       /       \
#      4         15
#    /  \       /  \
#   2    7    17    20
#  / \             /  \
# 1   3          19    22
treePreOrder(tree)
print("")
treeInOrder(tree)
print("")
treePostOrder(tree)
print("")