'''
Implement LRU cache. 
Get will return value of a key if present and moves the node to the beginning else -1
Set will add a key,value pair at the beginning of the linked list making room if needed 
by deleting Least Recently Used entries
Idea: use hash map and doubly linked list
Formal defnition:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
The LRUCache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.
'''
class Node:
   def __init__(self, key, value):
       self.key = key
       self.value = value
       self.next_link = None
       self.prev_link = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.h = {}
        self.head = None
        self.tail = None
        self.current_capacity = 0

    def refresh(self, node):
        np = node.next_link
        pp = node.prev_link
        if pp is not None:
            pp.next_link = np
        if np is not None:
            np.prev_link = pp
        if self.tail == node:
            self.tail = pp
        node.next_link = self.head
        node.prev_link = None
        self.head.prev_link = node
        self.head=node
        return node.value

    # @return an integer
    def get(self, key):
        if key in self.h:
            node = self.h[key]
            if self.head == node:
                return node.value
            return self.refresh(node)
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.h: 
            self.h[key].value = value
            node = self.h[key]
            if self.head == node:
                return 
            self.refresh(node)
        elif self.current_capacity < self.capacity: #enough room
            new_node = Node(key,value)
            self.current_capacity+=1
            if self.head == None: # first node
                self.head = new_node
                self.tail = new_node
            else:
                self.head.prev_link = new_node
                new_node.next_link = self.head
                self.head = new_node
            self.h[key]=new_node
        else: #time to delete last entry
            del_node = self.tail
            del self.h[del_node.key]
            if del_node.prev_link is not None:
                del_node.prev_link.next_link = None
                self.tail = del_node.prev_link
            else:
                self.tail = None
                self.head = None
            new_node = Node(key,value)
            self.h[key]=new_node
            if self.head == None: # first node
                self.head = new_node
                self.tail = new_node
            else:
                self.head.prev_link = new_node
                new_node.next_link = self.head
                self.head = new_node
            
if __name__ == '__main__':
    n,c = map(int, raw_input().strip().split())
    lc = LRUCache(c)    
    for _ in xrange(n):
        ip = raw_input().strip().split()
        if ip[0]=='G':
            print lc.get(int(ip[1]))
        elif ip[0]=='S':
            lc.set(int(ip[1]), int(ip[2]))
'''
example command line input:
7 2
S 1 10
S 2 20
G 1
G 2
S 3 30
G 3
G 1
'''
