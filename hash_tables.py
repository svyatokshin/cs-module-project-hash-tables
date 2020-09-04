my_arr = ["hi", "world", "how", "are", "you", "lorem", "ipsum", "set"]

# Search for an element in this arr
##


# O(n) -- linear search
def find_element(arr, el):
    for thing in arr:
        if thing == el:
            return True

    return False

# Or if we sorted, binary search!
# O(log n)

# Which Big O complexities are faster than log n?
# Constant time! O(1)
# if we increase the input, we still take number of steps to find what we're looking for

# def magic_fun_find_index(arr, el):
#     return el_index

# idx = magic_fun_find_index(my_arr, "set") ## 7
# my_arr[idx] # ta-da

# hash tables == arrays + hashing function

# Write a function that will take a string and return a number


def len_hash(str):
    return len(str)


# BAD: A lot of collisions
len("sad") == len("was")
len("ball") == len("hats")

# Good:
# Fast
# Deterministic

# We could map letters to numbers, but that's already been done!
# ASCII was the first mapping of letters to number
# UTF-8 is ASCII on steroids, designed to work with ASCII but be universal
# use .encode()

## a: 1
## a: 2


def UTF8_hash(str):
    # for letter in str:
    #   val = ord(letter)
    #   total += val
    total = 0
    utf_bytes = str.encode()
    for byte in utf_bytes:
        total += byte

    return total


print(UTF8_hash("sad"))
print(UTF8_hash("was"))

# but we will still have collisions
UTF8_hash("dad")
UTF8_hash('add')

# A hash function: takes string, give back number
# operate on the bytes that make up the string
# Deterministic

# To improve our hash functions, make output more unique!
# SHA256

# Hash function + array!!
# how to map the output of our hash function to an index in an array?

# my_arr2 = [None] * 20
# print(my_arr2)

# idx = UTF8_hash('supercalifragilisticexpialidocious')  # 3643
# print(idx)

# how to turn result of hash function into usable index?
# modulo the hash with len(my_arr2)

# Modulo demonstration
# modulo returns from 0 to len(list) - 1

# "take it modulo", "modulo it", "mod it"
# "modding"

# Use modulo with hash (output of hashing function) to get usable index

# we can now combine hash function and array

my_arr2 = [None] * 20

our_hash = UTF8_hash('supercalifragilisticexpialidocious')  # 3643
idx = our_hash % len(my_arr2)

my_arr2[idx] = 'Mary Poppins'

# print(my_arr2)

# 'get'
our_hash = UTF8_hash('supercalifragilisticexpialidocious')
idx = our_hash % len(my_arr2)

val = my_arr2[idx]
print(val)

# key value store
# 'supercali..' is the key
# 'Mary Poppins" is the value

# Hash table in programming languages?
# Python: dictionary
# JS: Object
# Hash map
# Map

# Pseudocode for put
# 1. Hash the key
# 2. Take the hash and mod it with len of array
# 3. Go to index and put in value

# Pseudocode for get
# 1. Hash the key
# 2. Take the has and mod it with the len of array
# 3. Go to index and get out the value

# Time complexity?
# same for get and put
# Linear in length of string/key
# Constant time in length of array <----- This is what we pay attention to
# O(1)


# Collision
key1 = 'dad'
key2 = 'add'

# Get
get_hash = UTF8_hash(key1)
idx3 = get_hash % len(my_arr2)


# Put 1
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'

print(my_arr2[idx3])


# Put 2
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = 'whats up yall'

print(my_arr2[idx3])


# Even when we use our hash function with modulo, we get collisions
# To be solved later

# We wrote our own hash function, what about Python's hash()?
# Many different hash functions! Can also hash()

# When used with hash tables, hashing function should be FAST
# Why? we want O(1), and a lot of lookups

# Other uses of hash functions
# passwords!!
# Encryption/decryption

# password ---> Hashing function ---> hashed_password
# password --> Hashing function ---> hash === hashed_password ??


# SHA-256 has never had a collision
# can use the output (hash) as a fingerprint for your string
my_string = "Dear everybody, how are you? I write to you ..."
