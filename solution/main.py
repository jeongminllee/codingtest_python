class Node :
    def __init__(self, data) :
        self.data = data
        self.children = []

    def __repr__(self) :
        return f'Node({self.data}, children={len(self.children)})'

def build_tree(nodes, parent_nodes) :
    node_dict = {i: Node(i) for i in nodes}
    root = None

    for node, parent in zip(nodes, parent_nodes) :
        if node == parent :
            root = node_dict[node]

        else :
            node_dict[parent].children.append(node_dict[node])
    return root


nodes = [1, 2, 3, 4, 5, 6, 7]
parent_nodes = [1, 1, 1, 2, 1, 2, 6]
print(build_tree(nodes, parent_nodes))
