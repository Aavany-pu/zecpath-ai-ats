import sys


class MemoryCache:
    def __init__(self):
        self.cache = {}

    def store(self, key, value):
        self.cache[key] = value

    def retrieve(self, key):
        return self.cache.get(key)

    def remove(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache.clear()

    def size(self):
        return len(self.cache)


def estimate_memory_usage(data):
    return sys.getsizeof(data)


def optimize_memory(data):
    memory_before = estimate_memory_usage(data)

    optimized_data = data

    memory_after = estimate_memory_usage(optimized_data)

    return {
        "Status": "Memory Usage Analyzed",
        "Memory Before": memory_before,
        "Memory After": memory_after,
        "Data": optimized_data
    }