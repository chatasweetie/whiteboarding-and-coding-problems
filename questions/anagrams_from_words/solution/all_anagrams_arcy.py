#Anagrams from Words

# Write a method anagrams_of that returns an array of all the anagrams of an input string. 
# There is a file called `words.txt` that contains ~235,000 words. 

# Explain the time and space complexity of your algorithm.

# **Examples:**
def anagrams_of(string):
    """
    >>> anagrams_of('tghin')
    ['night', 'thing']
    >>> anagrams_of('ains')
    ['anis', 'nais', 'nasi', 'Nias', 'sain', 'sina']
    >>> anagrams_of('llleee')
    []
    >>> anagrams_of('yoabrked')
    ['keyboard']
    
    Pseudocode:
    Sort the input string.
    Read the file `words.txt`
    Create an empty list called `anagrams` to store the anagrams
    Read each line in the file, lower case and sort the string
    If the sorted string is equal to the sorted input string, 
    append the line to the `anagrams` list
    Return the `anagrams` list

    Assumptions: 
    - All words are alphabetic characters
    - No empty strings
    - No duplicates
    """
    sorted_string = sorted(string.lower()) # O(m log m)
    anagrams = []
    with open('words.txt', 'r') as file: # O(n)
        for line in file:
            word = line.strip() # Remove newline characters
            sorted_line = sorted(word.lower()) # O(k log k)
            if sorted_string == sorted_line:
                anagrams.append(word)
    return anagrams

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")

# Time Complexity: O(m log m + n * k log k)
# Space Complexity: ???