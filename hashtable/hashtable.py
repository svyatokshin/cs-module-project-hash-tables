class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.data = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return self.capacity
        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        := means "set left variable equal to right side"

        Python < 3.4 uses FNV
        """

        # Your code here
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        # algorithm fnv-1 is
        # hash := FNV_offset_basis do
        hashed_result = FNV_offset_basis
        key_bytes = key.encode()
        # for each byte_of_data to be hashed
        for byte in key_bytes:
            #     hash := hash × FNV_prime
            hashed_result = hashed_result * FNV_prime
        #     hash := hash XOR byte_of_data
            hashed_result = hashed_result ^ byte

        # return hash
        return hashed_result

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.

        # Your code here
    {
        unsigned long hash = 5381;
        int c;

        while (c = *str++)
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
    }
    """
        # Pseudo Code
        # make a variable equal to 5381
        hashed_result = 5381
        # iterate over the bytes of our key
        key_bytes = key.encode()
        # for each byte,
        for byte in key_bytes:
            # shift the variable and add it and add the byte
            hashed_result = ((hashed_result << 5) + hashed_result) + byte
            # the << 5 adds 5 0's in binary, helps create a super random number

        return hashed_result

        # hash = 5381

        # for c in key:
        #     hash = (hash * 33) + ord(c)
        # return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # 1. Hash the key
        # 2. Take the hash and mod it with len of array
        idx = self.hash_index(key)
        # 3. Go to index and put in value
        self.data[idx] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # find index for given key
        idx = self.hash_index(key)
        # assign data back to None
        self.data[idx] = None

        # if key:
        #     idx = self.hash_index(key)
        #     self.data[idx] = None
        #     return
        # else:
        #     print("No such value exists")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # 1. Hash the key
        # 2. Take the has and mod it with the len of array
        # 3. Go to index and get out the value

        if key:
            idx = self.hash_index(key)
            value = self.data[idx]
            return value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
