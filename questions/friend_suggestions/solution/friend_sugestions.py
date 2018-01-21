import user


def to_get_list_of_users_to_be_displayed(User):
    """Returns list of potential friends for user"""

    current_friends = User.get_friends()
    current_friends = set(current_friends)

    friends_of_friends = []

    for person in current_friends:
        friends_of_friends.extend(person.get_friends())

    friends_of_friends = set(friends_of_friends)

    possible_friends = friends_of_friends - current_friends

    return list(possible_friends)

friend_recommendations = to_get_list_of_users_to_be_displayed(user.people[0])


def to_get_list_of_users_to_be_displayed_better_version(User):
    """Returns list of potential friends for user"""

    current_friends = user.people[0].get_friends()

    friends_of_friends = []

    for person in current_friends:
        friends_of_friends.extend(person.get_friends())

    voting_friends = {}

    for person in friends_of_friends:
        voting_friends[person] = voting_friends.get(person, 0) + 1

    # threshold is a magical number that is the minimum number of connects
    # a user should have to be recommend (should be dynamic)
    threshold = len(current_friends) / 15

    possible_friends = []
    for person in voting_friends:
        if person not in current_friends and voting_friends[person] > threshold:
            possible_friends.append(person)

    return possible_friends


friend_recommendations_better_version = to_get_list_of_users_to_be_displayed_better_version(user.people[0])
