class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return None

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    if node is  None:
        return
    in_order_traversal(node.left)
    in_order_traversal(node.right)
    print(node.data)
    return node

# pre_order_traversal(node1)
# in_order_traversal(node1)
#
# post_order_traversal(node1)
def pre_order_traversal_with_stack(node):
    """

    :param node: 树的根节点
    :return:
    """
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right

# pre_order_traversal_with_stack(node1)


from queue import Queue


def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)

level_order_traversal(node1)