# This section is used to import libraries that are used in the code.
from person import Person
import time

# These are the small, medium and large data files that we will be reading as our sample
fileref = open("smallData.dat", "r") # r is for read
# fileref = open("mediumData.dat", "r") # r is for read
# fileref = open("largeData.dat", "r") # r is for read

# The next section reads in the data, then transforms the data into
# a readable version that Python can handle.
lines = fileref.readlines()

firstname = ''
lastname = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    if ',' in line:
        lastname, firstname = line.strip().split(', ')
        continue
    elif line[0].isdigit():
        street = line.strip()
        continue
    else:
        my_list = (line.strip().split('\t'))
        if len(my_list) > 1:
            #print(my_list)
            city, state, postcode = my_list
            continue

    person = Person(firstname, lastname, street, city, state, postcode)
    people.append(person)

# Here we define the Bubble Sort algorithm.


def bubbleSort(people):
    n = len(people)
    print("Number of people:")
    print(n)
    print("Time Taken:")
# Traverse through the entire array of elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # If the element found is greater than the next in line, swap it
            if people[j].firstname > people[j+1].firstname:
                people[j], people[j+1] = people[j+1], people[j]

# Define the merge sort algorithm.
#


def mergeSort(people):
    if len(people) >1:
        mid = len(people)//2  # this finds the mid point of the array
        L = people[:mid]  # then divides the array in 2
        R = people[mid:]  # and names them Left [L] and Right [R]

        # Perform merge sort on both halves of the dataset
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy the data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].lastname < R[j].lastname:
                people[k] = L[i]
                i += 1
            else:
                people[k] = R[j]
                j += 1
            k += 1

        # Continue sorting the data until the entirety of L is sorted
        while i < len(L):
            people[k] = L[i]
            i += 1
            k += 1

        # Continue sorting the data until the entirety of R is sorted
        while j < len(R):
            people[k] = R[j]
            j += 1
            k += 1


# The following function takes the last element as a pivot
# then places it at its correct position in a sorted array.
# It then places all smaller (than pivot) to the left, and
# places all high elements (than pivot) to the right.


def partition(people,low,high):
    i = (low-1)  # index of smaller element
    pivot = people[high].lastname  # pivot

    for j in range(low, high):
        # if current element is smaller than, or equal to the pivot
        if people[j].lastname <= pivot:
            # increment index of smaller element
            i = i+1
            people[i],people[j] = people[j],people[i]

    people[i+1], people[high] = people[high],people[i+1]
    return i + 1

# This function implements QuickSort
# arr[] --> array to be sorted,
# low --> starting index
# high --> ending index

low = 0
high = len(people)-1

#  Function to do the QuickSort
#  This utilizes the partition function above


def quickSort(people, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at the correct place
        pi = partition(people, low, high)
        # separately sort elements before and after partition
        quickSort(people, low, pi-1)
        quickSort(people, pi+1, high)


def pythonSort(people):
    # This sort method utilises the default python sorting algorithm
    # It is case sensitive so some data is difficult to parse.
    people.sort(key=lambda person: person.lastname.upper(), reverse=False)
    for person in people:
        print(person)


# Conduct the time comparison:

# Bubble sort time comparison
#start = time.perf_counter()
#bubbleSort(people)
#end = time.perf_counter()
#bubbleSortTime = end - start
#print(bubbleSortTime)

# Merge sort time comparison
#start = time.perf_counter()
#mergeSort(people)
#end = time.perf_counter()
#mergeSortTime = end - start
#print(mergeSortTime)

# Quick sort time comparison
#start = time.perf_counter()
#quickSort(people, low, high)
#end = time.perf_counter()
#quickSortTime = end - start
#print(quickSortTime)

# Python sort time comparison
start = time.perf_counter()
pythonSort(people)
end = time.perf_counter()
pythonSortTime = end - start
print(pythonSortTime)

# Output to a .csv file for use in the searching people section.
outfile = open('smallData.csv', 'w')

for person in people:
    outfile.write(str(person) + '\n')
outfile.close()


