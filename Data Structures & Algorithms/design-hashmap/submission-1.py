class MyHashMap:

    def __init__(self):
        self.data = []
        self.keys = []

    def put(self, key: int, value: int) -> None:
        self.entry = [key, value]
        if key in self.keys:
            self.data[self.keys.index(key)][1] = value
        else:
            self.keys.append(key)
            self.data.append(self.entry)

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.data[self.keys.index(key)][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.data.pop(index)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)