class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, i):
        if not self.head:
            return -1
        cur = self.head
        n = 0
        while cur:
            if n == i:
                return cur.val
            cur = cur.next
            n += 1
        return -1

    def insertHead(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node

    def insertTail(self, val):
        node = Node(val)
        if not self.tail:
            self.tail = node
            self.head = node
        self.tail.next = node
        self.tail = node

    def remove(self, i):
        if not self.head:
            return False
        if i == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        cur = self.head
        n = 0
        while cur and n < i - 1:
            cur = cur.next
            n += 1
        if not cur or not cur.next:
            return False

        if cur.next == self.tail:
            cur.next = None
            self.tail = cur
            return True
        cur.next = cur.next.next
        return True

    def getValues(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
