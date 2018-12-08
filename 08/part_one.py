class Node:
    def __init__(self, children_count, metadata_count, metadata):
        self.children_count = children_count
        self.metadata_count = metadata_count
        self.metadata = metadata

def recursive_find_children(tree, children=[]):
    tree = [int(x) for x in tree]
    header = tree[0:2]
    children_count, metadata_count = header

    min_size = len(header) + (children_count * len(header)) + metadata_count
    if len(tree) == 0 or len(tree) < min_size:
        return children

    if children_count > 0:
        # Branch
        branch_children = recursive_find_children(tree[2:],[])
        # adds itself as a child
        total_child_size = 0
        for child in branch_children:
            size = len(child.metadata) + 2
            total_child_size += size

        self_node_end_idx = 1 + (total_child_size) + metadata_count
        self_metadata_start_idx = self_node_end_idx - metadata_count + 1
        node = Node(children_count, metadata_count, tree[self_metadata_start_idx:self_node_end_idx + 1])
        children.append(node)
        children += branch_children
        return children
    else:
        # Leaf
        metadata_start_idx = 2
        if metadata_count == 0:
            metadata_idx_diff = 0
        else:
            metadata_idx_diff = (metadata_count - 1)
            metadata_end_idx = metadata_start_idx + metadata_idx_diff
            node = Node(children, metadata_count, tree[metadata_start_idx:metadata_end_idx + 1])
            children.append(node)

        tree_remainder = tree[(metadata_end_idx + 1):]
        if len(tree_remainder) > 0:
            return recursive_find_children(tree_remainder, children)
        else:
            return children


def main():
    tree = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")
    children = recursive_find_children(tree)
    metadata_sum = 0
    for child in children:
        for metadatum in child.metadata:
            metadata_sum += metadatum

    print(metadata_sum)


main()
