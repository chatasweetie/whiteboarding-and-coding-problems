
def convert_file_stru_dict(lst):
    """Returns a dictionary model from a list of paths
    time: O(n^2)
    space: O(n)

        >>> convert_file_stru_dict(["/foo/bar", "/foo/baz", "/doc/baz"])
        {'doc': {'baz': {...}}, 'foo': {'bar': {...}}, 'baz': {}}

        >>> convert_file_stru_dict(["/foo/bar", "/foo/baz", "/doc/baz", "/doc/bar", "/fav", "/bar/foo/fav/doc/"])
        {'fav': {}, 'doc': {'baz': {...}}, 'foo': {'bar': {...}}, 'baz': {}, 'bar': {'': {...}, 'doc': {...}, 'foo': {...}, 'fav': {...}}}
    """

    file_path = {}

    for path in lst:
        path = path[1:].split("/")
        new_dict = {}
        current = file_path
        for part in path:
            if not current.get(part):
                current[part] = new_dict
                current = current[part]

    return file_path

lst = ["/foo/bar", "/foo/baz", "/doc/baz"]


print convert_file_stru_dict(lst)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
