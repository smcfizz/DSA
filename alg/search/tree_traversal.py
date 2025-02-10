from ds.tree import TreeNode

def in_order(root: TreeNode):
    """
    In-order traversal: Left -> Root -> Right
    This implementation is generalized for any n-ary tree. The root is processed after the first half of its children.
    """
    if root is None:
        return

    q = root.children.copy()
    root_idx = len(q) // 2
    q.insert(root_idx, root)
    for i in range(len(q)):
        if i == root_idx:
            print(q[i].val)
            continue
        in_order(q[i])

def pre_order(root: TreeNode):
    """
    Pre-order traversal: Root -> Left -> Right
    This implementation is generalized for an n-ary tree. Child nodes are stored in an array and processed in order.
    """
    if root is None:
        return

    print(root.val)
    for child in root.children:
        pre_order(child)

def post_order(root: TreeNode):
    """
    Post-order traversal: Left -> Right -> Root
    Generalized for an n-ary tree. Child nodes are stored in an array and processed in reverse order.
    """
    if root is None:
        return

    for child in reversed(root.children):
        post_order(child)

    print(root.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children[0].children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))

    print('In-order:')
    in_order(root)

    print('Pre-order:')
    pre_order(root)

    print('Post-order:')
    post_order(root)