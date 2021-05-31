# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.before = {}
        self.after = {}
        self.start = 'start'
        self.end = 'end'
        self.connect(self.start, self.end)


    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if len(self.cache) >= self.maxSize:
            self.deleteKey(self.after[self.start])
        self.renewKey(key, value)

    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cache:
            return None
        val = self.cache[key]
        self.renewKey(key, val)
        return val

    def getMostRecentKey(self):
        # Write your code here.
        key = self.before[self.end]
        val = self.cache[key]
        self.renewKey(key, val)
        return key
    
    def connect(self, a, b):
        self.after[a], self.before[b] = b, a

    def deleteKey(self, key):
        if key in self.cache:
            self.cache.pop(key)
            self.connect(self.before[key], self.after[key])
            self.before.pop(key)
            self.after.pop(key)
    
    def renewKey(self, key, value):
        self.deleteKey(key)
        self.cache[key] = value
        self.connect(self.before[self.end], key)
        self.connect(key, self.end)
