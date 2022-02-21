class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printdata = self.head
        while printdata is not None:
            print(printdata.data)
            printdata = printdata.next

    def insert_at_begining(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = n

    def insert_between(self, middle, data):
        if not isinstance(middle, Node):
            raise RuntimeError("Must be type Node")
        if middle is None:
            raise RuntimeError("Node is absent") 

        n = Node(data)
        n.next = middle.next
        middle.next = n

    def remove(self, data):
        head = self.head
        if head is not None:
            if head.data == data:
                self.head = head.next
                head = None
                return
        while(head is not None):
            if head.data == data:
                break
            prev = head
            head = head.next
        
        if head == None:
            return
        
        prev.next = head.next
        head = None

ll = LinkedList()
ll.head = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")

ll.head.next = n2
n2.next = n3

ll.insert_at_begining("Sun")
ll.insert_at_end("Sat")
ll.insert_between(n3, "Thu")

ll.printlist()

print("===")

ll.remove("Thu")
ll.printlist()