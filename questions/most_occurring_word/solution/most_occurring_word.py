def clean_word(word):
    """Cleans punctuation and lower cases words

        >>> clean_word("Banana")
        'banana'
        >>> clean_word("River,")
        'river'
        >>> clean_word("boat!")
        'boat'
    """

    word = word.lower()
    punctuation = {"?", "!", ",", "."}
    if word[-1] in punctuation:
        word = word[:-1]

    return word


def word_count_dic(string):
    """Convertns string into dict[word] = Number of time word appears

        >>> word_count_dic("How much wood would a wood chuck chuck if a wood chuck could chuck wood?")
        {'a': 2, 'wood': 4, 'would': 1, 'could': 1, 'chuck': 4, 'how': 1, 'much': 1, 'if': 1}
    """

    message = string.split()

    word_counts = {}

    for raw_word in message:
        word = clean_word(raw_word)
        word_counts[word] = word_counts.setdefault(word, 0) + 1

    return word_counts


def most_occuring_word(message):
    """Returns the word(s) that occure the most in a message

        >>> raw_message = "How much wood would a wood chuck chuck if a wood chuck could chuck wood?"
        >>> print most_occuring_word(raw_message)
        ['wood', 'chuck']

        >>> raw_message2 = "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?"
        >>> print most_occuring_word(raw_message2)
        ['fuzzy']
    """

    word_counts = word_count_dic(message)

    max_num = 0
    max_word = []

    for key in word_counts:
        if word_counts[key] == max_num:
            max_word.append(key)
            continue
        if word_counts[key] > max_num:
            max_word = []
            max_num = word_counts[key]
            max_word.append(key)

    return max_word

raw_message = "How much wood would a wood chuck chuck if a wood chuck could chuck wood?"
print most_occuring_word(raw_message)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
