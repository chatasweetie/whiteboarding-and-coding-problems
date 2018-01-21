
data = [
        {   "owner": "Joe", 
            "owned_thing": "Addepar",
            "value": "100 shares",
        },
        {   "owner": "Joe",
            "owned_thing": "Joe's 401k",
            "value": "100%",
        },
        {   "owner": "Joe",
            "owned_thing": "Lonsdale Trust",
            "value": "50%",
        },
        {   "owner": "Lonsdale Trust",
            "owned_thing": "Google",
            "value": "1000 shares",
        },
        {   "owner": "Lonsdale Trust",
            "owned_thing": "Berkshire",
            "value": "82 shares",
        },
        {   "owner": "Lonsdale Trust",
            "owned_thing": "Facebook",
            "value": "400 shares",
        },
        {   "owner": "Lonsdale Trust",
            "owned_thing": "Microsoft",
            "value": "430 shares",
        },
        {   "owner" : "Lonsdale Trust",
            "owned_thing": "Caterpillar",
            "value": "100 shares",
        },
        {   "owner" : "Joe's 401k",
            "owned_thing": "Goldman Sachs",
            "value": "200 shares",
        },
        {   "owner" : "Joe's 401k",
            "owned_thing": "Microsoft",
            "value": "330 shares",
        },
        {   "owner" : "Joe's 401k",
            "owned_thing": "Addepar",
            "value": "220 shares",
        },
        {   "owner" : "Joe's 401k",
            "owned_thing": "Tree House",
            "value": "100%",
        },
        {   "owner" : "Lonsdale Trust",
            "owned_thing": "Lonsdale Holdings",
            "value": "33%",
        },
        {   "owner" : "Lonsdale Holdings",
            "owned_thing": "Beachfront Property",
            "value": "100%",
        },
        {   "owner" : "Lonsdale Holdings",
            "owned_thing": "Widgets Inc",
            "value": "50%",
        }
]


def pretty_print(data, key="Joe", depth=1):
    """Prints data in bullet style"""
    for item in data[key]:
        space = "\t" * depth
        print space + "- {}".format(item)
        if data.get(item):
            pretty_print(data, item, depth+1)


def pretty_print_data(data):
    """Prints data in a bullet style

        >>> pretty_print_data(data)
        Joe
            - Addepar
            - Joe's 401k
                - Goldman Sachs
                - Microsoft
                - Addepar
                - Tree House
            - Lonsdale Trust
                - Google
                - Berkshire
                - Facebook
                - Microsoft
                - Caterpillar
                - Lonsdale Holdings
                    - Beachfront Property
                    - Widgets Inc
    """
    simple_data = {}

    for dic in data:
        simple_data.setdefault(dic["owner"], []).append(dic["owned_thing"])

    print "Joe"
    pretty_print(simple_data)


pretty_print_data(data)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"

