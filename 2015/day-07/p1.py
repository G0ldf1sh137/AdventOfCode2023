INPUT_FILE = './test.txt'

class Node:
    def __init__(self, txt: str) -> None:
        self.val = None
        split_idx = txt.find('->')
        self.connection = txt[:split_idx - 1].split()
        if len(self.connection) == 1:
            self._identity(self.connection[0])
        elif self.connection[1] == 'AND':
            self._and(self.connection[0], self.connection[2])
        elif self.connection[1] == 'OR':
            self._or(self.connection[0], self.connection[2])
        elif self.connection[1] == 'LSHIFT':
            self._lshift(self.connection[0])
        elif self.connection[1] == 'RSHIFT':
            self._rshift(self.connection[0])
        elif self.connection[0] == 'NOT':
            self._not(self.connection[1])
        else:
            self.val = None

    def __str__(self) -> str:
        return f'{self.connection} = {self.val}'
    
    def _identity(self, n1: str):
        if n1.isdecimal():
            self.val = int(self.connection[0])
        else:
            self.val = nodes[n1].val
    
    def _and(self, n1: str, n2: str):
        if n1 in nodes and nodes[n1].val and n2 in nodes and nodes[n2].val:
            self.val = nodes[n1].val & nodes[n2].val
        else:
            self.val = None

    def _or(self, n1: str, n2: str):
        if n1 in nodes and nodes[n1].val and n2 in nodes and nodes[n2].val:
            self.val = nodes[n1].val | nodes[n2].val
        else:
            self.val = None

    def _lshift(self, n1: str):
        if n1 in nodes and nodes[n1].val:
            self.val = nodes[n1].val << int(self.connection[2])
        else:
            self.val = None

    def _rshift(self, n1: str):
        if n1 in nodes and nodes[n1].val:
            self.val = nodes[n1].val >> int(self.connection[2])
        else:
            self.val = None
    
    def _not(self, n1: str):
        if n1 in nodes and nodes[n1].val:
            self.val = ~ nodes[n1].val
        else:
            self.val = None


nodes: dict[str, Node] = dict()

with open(INPUT_FILE) as DATA:
    file_data = DATA.read().splitlines()

for n in file_data:
    split_idx = n.rfind(' ')
    node_key = n[split_idx + 1:]
    nodes[node_key] = Node(n)

    print(node_key, '=', nodes[node_key])
