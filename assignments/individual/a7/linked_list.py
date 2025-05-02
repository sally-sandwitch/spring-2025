__author__ = 'Adriana Jergusova'

class LinkedList:
    class Node:
        def __init__ (self,item,next=None):
            self.item=item
            self.next=next


    def __init__(self):
        self.anchor = None
        self.end = None

    def empty(self):
        return self.anchor == None


    def __repr__(self):
        l = '['
        if self.anchor:
            l += str(self.anchor.item)
            node = self.anchor.next
            while node:
                l += ', ' + str(node.item)
                node = node.next
        return l + ']'
    

    def add(self, item):
        n1= self.Node(item,None)
        if self.anchor == None:
            self.anchor=n1
            return
        else:
            n=self.anchor
            while not n.next==None:
                n=n.next
            n.next=n1

    def clear(self):
        self.anchor=None

    def contains(self, item):
        i = 0
        node = self.anchor
        while i < len(self):
            if node.item == item:
                return True
            i += 1
            node = node.next
        return False

    def get(self, i):
        index = 0
        node = self.anchor
        while index < i:
            index += 1
            node = node.next
        return node.item

    def index_of(self, item):
        i = 0
        node = self.anchor
        while i < len(self):
            if node.item == item:
                return i
            i += 1
            node = node.next
        return -1

    def remove_at(self, i):
        if i == 0:
            self.anchor = self.anchor.next
        else:
            index = 0
            node = self.anchor
            while index < i-1:
                index += 1
                node = node.next
            node.next = node.next.next


    def set(self, i, item):
        index = 0
        node = self.anchor
        while index < i:
            index += 1
            node = node.next
        node.item = item

    def __len__(self):
        if not self.anchor:
            return 0
        else:
            n=1
            node=self.anchor.next
            while node:
                n+=1
                node=node.next
        return n

    def __eq__(self, other):
        if len(self) != len(other): return False
        # Assertion: len(self) == len(other)
        elif not self.anchor and not other.anchor:
            return True
        else:
            node1 = self.anchor
            node2 = other.anchor
            while node1.item == node2.item:
                node1 = node1.next
                node2 = node2.next
                if node1 == node2 == None:
                    return True
        return False

    def __iter__(self):
        self.iter_index=0
        return self
    
    def __next__(self):
        if self.iter_index == len(self):
            raise StopIteration
        item= self.get(self.iter_index)
        self.iter_index +=1
        return item