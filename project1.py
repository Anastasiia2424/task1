# За заданим бінарним деревом напишіть функцію, яка повертає суму значень цього дерева.
import random

class Node:
    def __init__(self, l=None, r=None, v=0) -> None:
        self.left = l
        self.right = r
        self.value = v

def get_tree(max=50):
    nodes = [Node(v=random.randint(-100, 100)) for i in range(max + 1)]

    tree = Node()
    for i in range(max):
        sight = random.choice(['l', 'r'])
        val = random.randint(-100, 100)
        vall = random.randint(0, max)
        if sight == 'l':
            tree = Node(l=tree, r=nodes[vall], v=val)
        else:
            tree = Node(l=nodes[vall], r=tree, v=val)
    return tree

tree1 = get_tree(5)
tree2 = get_tree(10)
tree3 = get_tree(50)

def solution1(tree: Node):    
    if tree is None: 
        return 0
    return tree.value + solution1(tree.left) + solution1(tree.right)



def test_func1():
    print(solution1(tree1))
    print(solution1(tree2))
    print(solution1(tree3))


if __name__ == "__main__":
    test_func1()