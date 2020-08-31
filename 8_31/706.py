class ListNode:
    def __init__(self,key:int = 0, value:int = 0, next:ListNode = None):
        self.value = value
        self.key = key
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        # self.myhashh =[ListNode(None)] * 1000
        self.table = collections.defaultdict(ListNode)

        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
        return
    

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p =  self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            return
        p =  self.table[index]
        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                return
            p = p.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)