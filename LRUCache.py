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
        self.after[self.start] = self.end
        self.before[self.end] = self.start


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

    def deleteKey(self, key):
        if key in self.cache:
            self.cache.pop(key)
            self.after[self.before[key]] = self.after[key]
            self.before[self.after[key]] = self.before[key]
            self.before.pop(key)
            self.after.pop(key)
    
    def renewKey(self, key, value):
        print(self.cache)
        print('before', self.before)
        print('after', self.after)
        self.deleteKey(key)
        self.cache[key] = value
        self.after[key] = self.end
        self.before[key] = self.before[self.end]
        self.after[self.before[key]] = key
        self.before[self.end] = key
