class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.values = []
        self.children = []
        self.next = None

class BPlusTree:
    def __init__(self, t=3):
        self.root = BPlusTreeNode(leaf=True)
        self.t = t

    def search(self, key, node=None):
        if node is None:
            node = self.root
        if node.leaf:
            for i, k in enumerate(node.keys):
                if k == key:
                    return node.values[i]
            return None
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            return self.search(key, node.children[i])

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == (2*self.t - 1):
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        if node.leaf:
            if key in node.keys:
                idx = node.keys.index(key)
                for doc, freq in value.items():
                    node.values[idx][doc] = node.values[idx].get(doc, 0) + freq
            else:
                i = 0
                while i < len(node.keys) and key > node.keys[i]:
                    i += 1
                node.keys.insert(i, key)
                node.values.insert(i, value)
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            if len(node.children[i].keys) == (2*self.t - 1):
                self.split_child(node, i)
                if key >= node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def split_child(self, parent, index):
        t = self.t
        node = parent.children[index]
        new_node = BPlusTreeNode(leaf=node.leaf)
        mid = t - 1
        if node.leaf:
            new_node.keys = node.keys[mid:]
            new_node.values = node.values[mid:]
            node.keys = node.keys[:mid]
            node.values = node.values[:mid]
            new_node.next = node.next
            node.next = new_node
            parent.keys.insert(index, new_node.keys[0])
            parent.children.insert(index + 1, new_node)
        else:
            new_node.keys = node.keys[mid+1:]
            new_node.children = node.children[mid+1:]
            parent.keys.insert(index, node.keys[mid])
            parent.children.insert(index + 1, new_node)
            node.keys = node.keys[:mid]
            node.children = node.children[:mid+1]

def print_bptree(node, level=0):
    indent = "    " * level
    if node.leaf:
        print(f"{indent}Leaf: {list(zip(node.keys, node.values))}")
    else:
        print(f"{indent}Internal: {node.keys}")
        for child in node.children:
            print_bptree(child, level + 1)
