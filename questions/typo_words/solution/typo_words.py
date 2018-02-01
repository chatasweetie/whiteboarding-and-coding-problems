vocabulary = ["apple", "berry", "cherry", "dherry", "wheiry"]


def file_contents(filename):
    """Returns the file's data as a string"""

    with open(filename) as f:
        file_data = f.read()
    f.close()

    return file_data


def construct_word_array_file_file(filename):
    """Returns a dic of words from file
    words['sorted string'] = [words that contain same letters]

    """
    data = file_contents(filename)
    data = data.split()
    print len(data)

    return data

def create_typo_vocabular(words):
    """Returns a dict of one typo word with all the possible words
    example "c*ts" : ["cats", "cots"]
    """

    master_typo_vocabular = {}

    for word in words:
        for i in range(len(word)):
            new_word = word[:i] + "*" + word[i+1:]
            master_typo_vocabular.setdefault(new_word, []).append(word)

    return master_typo_vocabular


def is_word(word):
    """Returns all possible words with one letter change

        >>> print is_word("cats")
        ['bats', 'eats', 'Mats', 'cass', 'cate']
    """

    all_possible_words = []
    for i in range(len(word)):
        new_word = word[:i] + "*" + word[i+1:]
        if master_typo_vocabular.get(new_word):
            all_possible_words.extend(master_typo_vocabular.get(new_word))
    if all_possible_words:
        return all_possible_words
    return False

vocabulary = construct_word_array_file_file('words.txt')

master_typo_vocabular = create_typo_vocabular(vocabulary)
print is_word("apple")


#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"

