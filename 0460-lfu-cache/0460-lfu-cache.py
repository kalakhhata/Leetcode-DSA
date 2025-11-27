class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1


class DLL:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_back(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def pop_front(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.size = 0
        self.minfreq = 0
        self.keymap = {}    # key -> node
        self.freqmap = {}   # freq -> DLL

    def _update_freq(self, node):
        oldfreq = node.freq
        self.freqmap[oldfreq].remove(node)

        # update minfreq if needed
        if oldfreq == self.minfreq and self.freqmap[oldfreq].size == 0:
            self.minfreq += 1

        # new freq
        node.freq += 1
        newfreq = node.freq

        if newfreq not in self.freqmap:
            self.freqmap[newfreq] = DLL()

        # add node to new freq DLL
        self.freqmap[newfreq].add_back(node)


    def get(self, key):
        if key not in self.keymap:
            return -1

        node = self.keymap[key]
        self._update_freq(node)
        return node.val


    def put(self, key, value):
        if self.cap == 0:
            return

        # update existing
        if key in self.keymap:
            node = self.keymap[key]
            node.val = value
            self._update_freq(node)
            return

        # evict if needed
        if self.size >= self.cap:
            lfu_list = self.freqmap[self.minfreq]
            evict = lfu_list.pop_front()
            del self.keymap[evict.key]
            self.size -= 1

        # insert new node
        node = Node(key, value)
        self.keymap[key] = node

        if 1 not in self.freqmap:
            self.freqmap[1] = DLL()

        self.freqmap[1].add_back(node)
        self.minfreq = 1
        self.size += 1
