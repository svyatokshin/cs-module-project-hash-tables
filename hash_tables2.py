# Review Project
# code our hash functions
# Collisions: how to handle
# Stretch goal: hash function applications

# In general, crypto is hard
# takes any string as input
# Deterministic
# Non-reversible

# May have to generate a "secret" that the function use to hash/encrypt

# COLLISIONS
# How should we handle?
# Disallow it?
# Open addressing: Linear probing, quadratic probing

# Linked list aka chaining
# We're gonna make an array of linked lists
# data structure composition

buckets = [None] * 8

buckets = [
    None,
    Node('food', 'bar'), - -> Node('foooz', 'fub') - -> Node('zug', 'ixq')
    None,
    Node('quux', 'baz'),
    None,
    None,
    None,
    None,
]
put('foo', 'bar')  # 'foo' hashes to index 1
put('quux', 'baz')  # index 3
put('foooz', 'fub')  # 'foooz' hashes to index 1
put('zug', 'ixq')  # 'zug' hashes to index 1

get('fooz')  # go to index 1, iterate through and find the same key, return value 'fub'

# time cost of iterating? O(n)????

# storing key is a bad idea if you're hashing passwords
# but for a hash table it's okay


# Put
# hash your key, mod by len of your array to get your idx
# If idx is None, put your Node there
# If not None, iterate through
# If same key is found, overwrite
# If not, append to head or tail

# Get
# hash your key, mod by len of your array to get your idx
# If idx is None, return None
# If Idx isn't None, iterate through and find matching key and return the value

class None:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, val):
        # assign a cur_node
        cur_node = self.head
    # while cur_node is not None
        while cur_node is not None:
            # check the value
            #   if self.value = val
            if val = cur_node.value:
                #   return self.val
                return cur_node.value
    #   else cur_node = cur_node.next
        else cur_node = cur_node.next

    def add_to_tail(self, val):
        """
        Check if we have a head
        If so, find the tail and add a node

        """

        # start with head
        # if head is None, make a node and add it
        if self.head is None:
            self.head = Node(val)
        else:
            # otherwise, iterate through and find the tail
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.next = Node(val)


ll = LinkedList()
n1 = Node(3)
ll.head = n1

ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)


# Load Factor
0 | -> D
1 | -> H -> I -> J
2 | -> A
3 | -> C -> K -> L -> O -> P
4 | -> G -> Q -> R -> S
5 | -> B -> M
6 | -> E -> N
7 | -> F

# 19/8 == 2.375
# number of elements / number of buckets

# load factor < 0.7
# if load factor is < 0.2, using unnecessary amounts of memory

# Double the backing array!
# Then copy everything over
# Go through every bucket (aka index in your array)
# Go Through every node in the linked list (which lives in that bucket)

# That's O(n) but we don't resize very often
# hash it and mod it by the size of your array
