class LinearHashTable:

    class Node:
        def __init__(self, key: int, val: str):
            self.key = key
            self.val = val

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__size = 0
        self.__bucket = [None] * capacity

    def insert(self, key: int, val: str):
        """
        Insert a new key-value pair 
        """

        hashIndex: int = self.__exist(key)

        if hashIndex != -1:
            self.__bucket[hashIndex].val = val
            return

        hashIndex = self.__hash(key)

        while self.__bucket[hashIndex] != None and self.__bucket[hashIndex].key != -1:
            hashIndex += 1
            hashIndex = hashIndex % self.__capacity

        new_node = self.Node(key, val)
        self.__bucket[hashIndex] = new_node

        self.__size += 1
        if self.size() >= self.capacity() // 2:
            self.__table_doubling()

    def remove(self, key: int):
        """
        Remove a key-value pair if the key is found, else do nothing.
        """
        hashIndex = self.__exist(key)
        if hashIndex == -1:
            return

        self.__bucket[hashIndex].key = -1
        self.__size -=1

    def get(self, key: int) -> str:
        """
        Get value in hash. Return None if the value not found
        """
        hashIndex = self.__exist(key)

        if hashIndex == -1:
            return None

        return self.__bucket[hashIndex].val

    def __exist(self, key: int):
        """
        Find position of the key in bucket
        If not found, return -1        
        """
        hashIndex: int = self.__hash(key)
        while self.__bucket[hashIndex] != None and self.__bucket[hashIndex].key != key:
            hashIndex += 1
            hashIndex = hashIndex % self.__capacity

        if self.__bucket[hashIndex] != None and self.__bucket[hashIndex].key == key:
            return hashIndex

        return -1

    def __hash(self, key: int) -> int:
        return key % self.__capacity

    def __table_doubling(self) -> None:
        tmp = self.__bucket
        self.__bucket = [None] * self.__capacity * 2
        self.__size = 0
        self.__capacity *= 2
        for node in tmp:
            if node == None or node.key == -1:
                continue

            self.insert(node.key, node.val)
            

    def capacity(self) -> int:
        return self.__capacity

    def size(self) -> int:
        return self.__size
