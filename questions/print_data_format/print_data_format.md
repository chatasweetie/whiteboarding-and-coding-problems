#Are Anagrams?
Write the method pretty_print_data that takes a list of dictionaries and prints the data in a bullet style:


Given the following data:
data = [
{"owner" : "Joe", "owned_thing": "Addepar", "value": "100 shares"},
{"owner" : "Joe", "owned_thing": "Joe's 401k", "value": "100%"},
{"owner" : "Joe", "owned_thing": "Lonsdale Trust", "value": "50%"},
{"owner" : "Lonsdale Trust", "owned_thing": "Google", "value": "1000 shares"},
{"owner" : "Lonsdale Trust", "owned_thing": "Berkshire", "value": "82 shares"},
{"owner" : "Lonsdale Trust", "owned_thing": "Facebook", "value": "400 shares"},
{"owner" : "Lonsdale Trust", "owned_thing": "Microsoft", "value": "430 shares"},
{"owner" : "Lonsdale Trust", "owned_thing": "Caterpillar", "value": "100 shares"},
{"owner" : "Joe's 401k", "owned_thing": "Goldman Sachs", "value": "200 shares"},
{"owner" : "Joe's 401k", "owned_thing": "Microsoft", "value": "330 shares"},
{"owner" : "Joe's 401k", "owned_thing": "Addepar", "value": "220 shares"},
{"owner" : "Joe's 401k", "owned_thing": "Tree House", "value": "100%"},
{"owner" : "Lonsdale Trust", "owned_thing": "Lonsdale Holdings", "value": "33%"},
{"owner" : "Lonsdale Holdings", "owned_thing": "Beachfront Property", "value": "100%"},
{"owner" : "Lonsdale Holdings", "owned_thing": "Widgets Inc", "value": "50%"}
]

Print the following:

Joe
    -Addepar
    -Joe's 401k
        -Goldman Sachs
        -Microsoft
        -Addepar
        -Tree House
    -Lonsdale Trust
        -Google
        -Berkshire
        -Facebook
        -Microsoft
        -Caterpillar
       -Lonsdale Holdings
            -Beachfront Property
            -Widgets Inc


Explain the time and space complexity of your algorithm.


###Solutions

[Jessica's Solution - Python 2.7](https://github.com/chatasweetie/Algorithms-Whiteboarding/tree/master/questions/print_data_format/solution/print_data_format.py)
