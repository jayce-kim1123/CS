class Node:
    def __init__(self, data, pointer=None):
        self.data    = data
        self.pointer = pointer

def AddNewNode(data):
    node = head               # 리스트의 head부터 시작
    while node.pointer:       # 현재 변수 node의 pointer가 있을 때만
        node = node.pointer   # 다음 노드를 새로 node라는 변수에 할당
    node.pointer = Node(data) # 다음 노드가 없다면 새 노드 생성

node1 = Node(1) # node1의 data는 1
node2 = Node(2) # node2의 data는 2

node1.pointer = node2 # node1의 pointer는 node2
head  = node1 # 리스트의 head는 node1

print(node1.data)
print(node1.pointer)
print(node1.next.data)
