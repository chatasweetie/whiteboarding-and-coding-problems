def file_contents(filename):
    """Returns the file's data as a string"""

    with open(filename) as f:
        file_data = f.read()
    f.close()

    return file_data


def clean_sort_word(word):
    """Returns word lower case and sorted

        >>> clean_sort_word('bevaa')
        'aabev'

        >>> clean_sort_word('Cetonia')
        'aceinot'
    """

    word = word.lower()
    sorted_word = sorted(word)
    sorted_word = "".join(sorted_word)

    return sorted_word


def construct_word_dic_file_file(filename):
    """Returns a dic of words from file
    words['sorted string'] = [words that contain same letters]

    """
    data = file_contents('words.txt')
    data = data.split()
    words = {}
    for word in data:
        sorted_word = clean_sort_word(word)
        words.setdefault(sorted_word, []).append(word)

    return words


def anagrams_of(word):
    """Returns all anagrams for a word

        >>> anagrams_of('ains')
        ['anis', 'nais', 'nasi', 'Nias', 'sain', 'sina']

        >>> anagrams_of('aceinot')
        ['acetoin', 'aconite', 'anoetic', 'antoeci', 'Cetonia']
    """

    sorted_word = clean_sort_word(word)

    words = WORD_DIC.get(sorted_word)

    if not words:
        return False

    return words

WORD_DIC = construct_word_dic_file_file('words.txt')

anagrams_of('ains')

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
