class TreeNode[T]:
    """
    A simple n-ary tree node
    """
    def __init__(self, val: T):
        self.val = val
        self.children = []
        self.parent = None

    def __str__(self):
        return str(self.val)


def print_tree(root: TreeNode):
    if root is None:
        return
    print(root.val)
    for child in root.children:
        print_tree(child)

if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children[0].children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))

    print_tree(root)