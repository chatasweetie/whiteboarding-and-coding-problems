import random

class User(object):
    """A simple User object"""

    def __init__(self, name):
        self.name = name
        self.friends = set()

    def __repr__(self):
        """A prettier way of printing our User"""

        return """<User | {} >""".format(self.name)

    def make_friends(self, friend):
        """Adds the two user's to their friends list"""

        self.friends.add(friend)
        friend.friends.add(self)

    def get_friends(self):
        """Returns list"""
        list_friends = list(self.friends)

        return list_friends

people = []

# from a file of names, making User objects
f = open("names.txt")
for name in f:
    name = name.strip()
    user = User(name)
    people.append(user)

# making friends, clustering with the first 10 people
for person in people:
    person.make_friends(people[random.randrange(0, 10)])
    person.make_friends(people[random.randrange(0, 10)])
    person.make_friends(people[random.randrange(0, 10)])
    person.make_friends(people[random.randrange(0, 10)])
    person.make_friends(people[random.randrange(0, 10)])
    person.make_friends(people[random.randrange(0, 100)])
    person.make_friends(people[random.randrange(0, 100)])
