class Person():
    #This is the constructor
    def __init__(self, firstname, lastname, street, city, state, postcode):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city
        self.state = state
        self.postcode = postcode

    #method
        def getFirstName(self):
            return self.firstname

        def getLastName(self):
            return self.lastname

        def getStreet(self):
            return self.street

        def getCity(self):
            return self.city

        def getState(self):
            return self.state

        def getPostcode(self):
            return self.postcode

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.firstname, self.lastname, self.street, self.city, self.state, self. postcode)