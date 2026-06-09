class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.page_faults = 0

    def access_page(self, page):
        if page in self.cache:
            self.cache.remove(page)
            self.cache.append(page)
        else:
            self.page_faults += 1
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(page)
        print("Frames:", self.cache)


class DemandPaging:
    def __init__(self, capacity):
        self.lru = LRUCache(capacity)

    def access_page(self, page):
        self.lru.access_page(page)


# Test Data
pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5]
frames = 3

dp = DemandPaging(frames)

for p in pages:
    dp.access_page(p)

print("Total Page Faults:", dp.lru.page_faults)