
# 1. Create a simple hash function
def simple_hash(key):
    key_str = str(key)        
    hash_value = 0            
    for char in key_str:     
        hash_value += ord(char)  
    return hash_value % 10    


# 2. Hash a list of keys
keys = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'mango', 'plum']

def hash_keys(keys):
    for key in keys:
        print(f"Key: {key}, Hash Value: {simple_hash(key)}")
hash_keys(keys)

# 4. Collision resolution
BUCKET_SIZE = 10

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, bucket):
        self.__bucket = bucket
        # hash table with empty linked lists
        self.__table = [ None for _ in range(bucket)]

    # hash function
    def simple_hash(self, key):
        key_str = str(key)
        hash_value = 0
        for char in key_str:
            hash_value += ord(char)
        return hash_value % self.__bucket
        
    def insertItem(self, key, value):
        index = self.simple_hash(key)
        if self.__table[index] is None:
            self.__table[index] = Node(key, value)
        else:
            current = self.__table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)
          

    # search function
    def searchItem(self, key):
        index = self.simple_hash(key)
        if self.__table[index] is None:
            print("Key not found")
            return None
        else:
            current = self.__table[index]
            while current is not None: 
                if current.key == key:
                    print(f"Key: {key}, Value: {current.value}")
                    return current.value
                current = current.next
            print("Key not found")
            return None

