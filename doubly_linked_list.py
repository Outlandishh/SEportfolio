from person import Person

fileref = open("smallData.csv", "r")  # r is for read
#fileref = open("mediumData.csv", "r")  # r is for read
#fileref = open("largeData.csv", "r")  # r is for read

lines = fileref.readlines()

firstname = ''
lastname = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    firstname, lastname, street, city, state, postcode = line.strip().split(', ')
    person = Person(firstname, lastname, street, city, state, postcode)
    people.append(person)


# create a linked list node
class Node:

    # this is a constructor to create new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Class to create Doubly Linked List:
class DoublyLinkedList:
    # Constructor for a doubly linked list
    def __init__(self):
        self.head = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node the front of list
    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        #5. move the head to point to the new node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        # 1. Check if the given prev_node is None
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        # 2. allocate new node
        # 3. put in the data
        new_node = Node(new_data)

        # 4. Make new of the new node as next of prev node
        new_node.next = prev_node.next

        # 5. Make prev_node as previous of new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_nodes' next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)

        # 3. This new node is going to be the last node,
        # so make next of it as Node
        new_node.next = None

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next is not None:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last

        return

    # This function prints contents of the linked list
    # starting from the given node
    def printList(self, node):

        print("\nTraversal in forward direction")
        while node is not None:
            # print(" % d" % node.data,)
            print(node.data)
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last is not None:
            # print(" % d % last.data,)
            print(last.data,)
            last = last.prev


listOne = DoublyLinkedList()

for person in people:
    listOne.append(person)

print("\n\nCreated DLL using traverse method: ",)
listOne.printList(listOne.head)

################################

listTwo = DoublyLinkedList()

for person in people:
    listTwo.push(person)

print("\n\nCreated DLL using the push method: ",)
listTwo.printList(listTwo.head)
