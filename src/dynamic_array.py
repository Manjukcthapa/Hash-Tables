class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
             '''
        Insert object before index.
        '''
        # Check if there's room in our storage
        if self.count >= self.capacity:
            # If not, return an error
            self.double_size()

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
       #Insert our value
        self.storage[index] = value
        #Increment count
        self.count += 1

    def append(self, value):
        if self.count == self.capacity:
            self.double_size()

        self.count += 1
        self.storage[self.count - 1] = value

    def double_size(self):
         # Double storage size
        self.capacity *= 2
        new_storage = [None] * self.capacity
         # Copy old items to new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # Point storage to the new storage
        self.storage = new_storage

        arr = DynamicArray(8)
        arr.insert(0, "z")
        arr.insert(0, "y")
        arr.insert(0, "x")
        arr.insert(0, "w")
        print(arr.storage)
        arr.append("a")
        arr.append("b")
        arr.append("c")
        arr.append("d")
        print(arr.storage)
        arr.append(1)
        arr.append(2)
        arr.append(3)
        arr.append(4)
        print(arr.storage)