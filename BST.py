# Binary Search Tree

class Node:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        """
        Insert value iterating through either child if exists
        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
            return
        pos = self.root
        while pos:
            if value < pos.value:
                if pos.left is not None:
                    pos = pos.left
                else:
                    pos.left = Node(value)
                    return
            elif value > pos.value:
                if pos.right is not None:
                    pos = pos.right
                else:
                    pos.right = Node(value)
                    return
            else:  # value already exists
                return

    def delete(self, value):
        """
        Total of 3 scenarios :
            1. When node is leaf
            2. When node has either of child
            3. When node have both of its children

        :param value:
        :return:
        """
        prev = None
        pos = self.root
        while pos is not None and pos.value != value:
            """Iterating to the node to delete"""
            prev = pos
            if value < pos.value:
                pos = pos.left
            else:
                pos = pos.right
        if pos is None: return  # return if tree was empty
        if pos.left is None or pos.right is None:
            """Covering case 1 & 2 both"""
            new_node = None
            if pos.left is None:  # checking if either child exists
                new_node = pos.right
            else:
                new_node = pos.left
            if prev is None: pos = new_node  # if root node is value then making the only existing child as root
            if pos == prev.left:  # checking which pointer to unlink
                prev.left = new_node
            else:
                prev.right = new_node
        else:
            """Covering case 3"""
            parent = None
            tmp = pos.right  # temporary subtree
            while tmp.left is not None:  # iterating to smallest node on the right subtree
                parent = tmp
                tmp = tmp.left
            if parent is None:  # if true than promote the right subtree
                pos.right = tmp.right
            else:  # else promote the right subtree from left subtree
                parent.left = tmp.right
            pos.value = tmp.value  # finally copy the node value (which was unlinked) to the deleted one

    def inorder(self):
        """
        Steps:
            1. Append locations of nodes till left most child is reached
            2. Append popped locations value and iterate to right child
            3. Go to Step 1
        :return:
        """
        pos = self.root
        tmp, bst = [], []
        while True:
            if pos is not None:  # keep appending till end is reached on left most
                tmp.append(pos)  # appending location of nodes
                pos = pos.left
            elif tmp:  # check if tmp list is not empty
                pos = tmp.pop()
                bst.append(pos.value)
                pos = pos.right  # covering the right child when exists
            else:  # when tmp list empty and right most child is reached
                break
        return str(bst)

    def __str__(self):
        return str(self.inorder())

 
def test():
    bt = BST()
    l = [6, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
    for i in l:
        bt.add(i)

    print(bt)


if __name__ == "__main__":
    test()
