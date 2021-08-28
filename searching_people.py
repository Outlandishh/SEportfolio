from person import Person
import time

# fileref = open("smallData.csv", "r")  # r is for read
# fileref = open("mediumData.csv", "r")  # r is for read
fileref = open("largeData.csv", "r")  # r is for read

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


def linearSearch(people, searchString):
    for i in range (len(people)):
        if people[i].lastname == searchString:
            return print(people[i])
    return -1


linearSearch(people, 'Pezzini')


def binarySearch(people, searchString):
    first = 0
    last = len(people)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if people[mid].lastname == searchString:
            index = mid
        else:
            if searchString < people[mid].lastname:
                last = mid - 1
            else:
                first = mid + 1
    return print(people[index])


binarySearch(people, 'Pennyworth')


def pythonSearch(people, searchString):
    for person in people:
        if searchString in person.lastname:
            return print(person)
    return -1


pythonSearch(people, 'Palmer')



print("\n")
start = time.perf_counter()
linearSearch(people, 'Pezzini')
end = time.perf_counter()
linearSearchTime = end - start
print("LINEAR search time is: ")
print(linearSearchTime)

print("\n")
start = time.perf_counter()
binarySearch(people, 'Pennyworth')
end = time.perf_counter()
binarySearchTime = end - start
print("BINARY search time is: ")
print(binarySearchTime)

print("\n")
start = time.perf_counter()
pythonSearch(people, 'Palmer')
end = time.perf_counter()
pythonSearchTime = end - start
print("PYTHON search time is: ")
print(pythonSearchTime)
