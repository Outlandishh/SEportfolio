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


class Node:

    # Initiate the function
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Function to sort and insert new data. This will sort alphabetically based on first name.
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data.firstname < self.data.firstname:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.firstname > self.data.firstname:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the binary tree to the console
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


# Build the node and insert the persons from the people list stated above
root = Node(people[0])
for person in people:
    root.insert(person)

# Test that the tree is inserting correctly by adding additional people to the list
root.insert(Person('Jeremy', 'Landolfo', '19 Ivy Leaf rd', 'PAKENHAM', 'VIC', '3810'))
root.insert(Person('Cos', 'Chiera', '123 Fake Street', 'FRANKSTON', 'VIC', '3199'))
root.PrintTree()
