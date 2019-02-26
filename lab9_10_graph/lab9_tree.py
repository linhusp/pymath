# b1
class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def in_order(root):
    if root:
        in_order(root.left)
        print("%s " % root.value, end="")
        in_order(root.right)

def pre_order(root):
    if root:
        print("%s " % root.value, end="")
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print("%s " % root.value, end="")


root_tree = Tree('A')
root_tree.left = Tree('B')
root_tree.left.right = Tree('D')
root_tree.left.right.left = Tree('G')
root_tree.left.right.right = Tree('H')
root_tree.left.right.right.left = Tree('J')
root_tree.right = Tree("C")
root_tree.right.left = Tree("E")
root_tree.right.left.right = Tree("I")
root_tree.right.left.right.left = Tree("K")
root_tree.right.left.right.right = Tree("L")
root_tree.right.right = Tree("F")

in_order(root_tree)
print()

pre_order(root_tree)
print()

post_order(root_tree)
print()

#b2
