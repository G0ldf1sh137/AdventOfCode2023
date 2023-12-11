INPUT_FILE = './test.txt'

node = dict()

class Node:
    def __init__(self, txt: str) -> None:
        split_idx = txt.find('->')
        self.connection = txt[:split_idx - 1].split()
        if len(self.connection) == 1:
            self.val = int(self.connection[0])
        else:
            self.val = None

    def __str__(self) -> str:
        return f'{self.connection} = {self.val}'

with open(INPUT_FILE) as DATA:
    file_data = DATA.read().splitlines()

for n in file_data:
    split_idx = n.rfind(' ')
    node_key = n[split_idx + 1:]
    node[node_key] = Node(n)

    print(node_key, '=', node[node_key])