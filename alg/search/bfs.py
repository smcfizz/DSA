from ds.tree import TreeNode


def bfs(root: TreeNode, target) -> TreeNode | None:
    if root is None:
        return None

    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node.val == target:
            return node
        for child in node.children:
            q.append(child)

    return None


if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children[0].children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))

    if bfs(root, 4):
        print('Found')
    else:
        print('Not found')