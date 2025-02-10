from ds.tree import TreeNode

def dfs(root: TreeNode, target) -> TreeNode | None:
    if root is None:
        return None

    if root.val == target:
        return root

    for child in root.children:
        found = dfs(child, target)
        if found is not None:
            return found

    return None


if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children[0].children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))

    if dfs(root, 5) is not None:
        print('Found')
    else:
        print('Not found')