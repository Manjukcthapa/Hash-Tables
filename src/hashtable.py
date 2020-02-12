# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # here we find the index of the node which by using '_hash_mod' we create an 
        # integer of the key which will be the index on the list where we want to insert it
        index = self._hash_mod(key)
        # then we retrieve any preexisting node location before inserting it which should be None or occupied
        current = self.storage[index]
           
        # Try to find node already allocated with the same key
        while (current is not None and current.key is not key): #collision
            last = current
            current = last.next

        # If a node is found with the same key
        if (current is not None):
            current.value = value
        # if a node is not found
        else:
            # then we create a node pair using "LinkedPair" using the key and value
            pair = LinkedPair(key, value)
            pair.next = self.storage[index]
            self.storage[index] = pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # here we find the index of the node which by using '_hash_mod' we create an 
        # integer of the key which will be the index on the list where we want to insert it
        index = self._hash_mod(key)
        # then we retrieve any preexisting node location before inserting it which should be None or occupied
        last = None
        current = self.storage[index]

        # While the node isn't located, keep traversing
        while (current is not None and current.key is not  key):
            last = current
            current = current.next
        # If the key couldn't be found
        if (self.storage[index] is None):
            print("Error! Couldn't find key.")
        # if it is found
        else:
            # Removing the first element in the linkedlist
            if (last is None):
                self.storage[index] = current.next
            else:
                last.next = current.next
    
    


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass
      
        # so we find the node here we start with it's index
        index = self._hash_mod(key)
        # then we find the node
        node = self.storage[index]
        # if the node is not none meaning it exists
        while node is not None:
            # But we have to make sure the key matches the key of the retrieved peraminter
            if node.key == key:
                # if it doesn't then return it
                return node.value
                # if not then we just continue on the list
                # if it doesn't exist then we get nothing don't feel like returning anything 
            node = node.next
       


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
     
        self.capacity *= 2  # double the capacity
        old_storage = self.storage
        # create new hashtable/array with the increased capacity
        self.storage = [None] * self.capacity
        # for each bucket in new_storage array
        for each_bucket in old_storage: 
         # create iterator for each bucket 
            curr_bucket = each_bucket 
            # while we still have elements in our buckets
            while curr_bucket:  
                self.insert(curr_bucket.key, curr_bucket.value)
                curr_bucket = curr_bucket.next
   
    



if __name__ == "__main__":

    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
