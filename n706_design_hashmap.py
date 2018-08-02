class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.items_per_bucket = 1001
        self.map = [[]] * self.buckets

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, pos = key % self.buckets, key // self.buckets
        if not self.map[bucket]:
            self.map[bucket] = [None] * self.items_per_bucket
        self.map[bucket][pos] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, pos = key % self.buckets, key // self.buckets
        print(bucket, pos)
        if not self.map[bucket] or self.map[bucket][pos] is None:
            return -1
        else:
            return self.map[bucket][pos]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, pos = key % self.buckets, key // self.buckets
        if self.map[bucket]:
            self.map[bucket][pos] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)