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


# Create a people dictionary consisting of every person
# in the person class, then make a hash of this value.
people_dict = {}
for person in people:
    people_dict[hash(person)] = person

for k, v in people_dict.items():
    # print out the key:value pairing
    print(k, ':', v)
