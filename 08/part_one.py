
class Node:
    def __init__(self, children_count, metadata_count, metadata):
        self.children_count = children_count
        self.metadata_count = metadata_count
        self.metadata = metadata

def recursive_find_children(tree, children=[]):
    tree = [int(x) for x in tree]
    header = tree[0:2]

    if len(tree) == 0:
        return children

    children_count, metadata_count = header
    import pdb; pdb.set_trace()

    if children_count > 0:
        return recursive_find_children(tree[2:], children)
    else:
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
    import pdb; pdb.set_trace()


main()
