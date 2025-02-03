class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Pointer to the next node
        
    # @staticmethod
    def display(self,node):
        current = node
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node2.display(node1)
node3.display(node1)



