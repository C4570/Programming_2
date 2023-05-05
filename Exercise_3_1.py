class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)
    
    def nodos(self):
        cont = 1
        if self.left != None:
            cont += self.left.nodos()
        if self.right != None:
            cont += self.right.nodos()
        return cont
    
tree = Tree(8, Tree(2, Tree(4,Tree(7), Tree(3)), Tree(-3)), Tree(15, Tree(17), Tree(20,Tree(22),Tree(0))))
print(tree.nodos())