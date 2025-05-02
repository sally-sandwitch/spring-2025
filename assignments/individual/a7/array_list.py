__author__ = 'Adriana Jergusova'

class ArrayList:
    def __init__(self):
        self.size = 0
        self.data = [None]*1

    def _resize(self,new_size):
        new_data=[None]*new_size
        for i in range(len(self.data)):
            new_data[i]=self.data[i]
        self.data=new_data

    def __repr__(self):
        if self.size == 0: return '[]'
        s='['+ str(self.data[0])
        for i in range(1,self.size):
            s +=', ' + str(self.data[i])
        return s+ ']'

    def add(self, item):
        if self.size == len(self.data):self._resize(self.size*2)
        self.data[self.size]=item
        self.size+=1

    def clear(self):
        self.size = 0

    def contains(self, item):
        return item in self.data

    def get(self, index):
        return self.data[index]

    def index_of(self, item):
        for i in range(self.size):
            if self.data[i] == item: return i
        return -1

    def remove_at(self, index):
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def set(self, index, item):
        self.data[index] = item

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if self.size != other.size: return False
        # Assertion: len(self) == len(other)
        for i in range(self.size):
            if self.data[i] != other.data[i]: return False
        return True

    def __iter__(self):
        self.inter_index=0
        return self
    
    def __next__(self):
        if self.inter_index == self.size:
            raise StopIteration
        self.inter_index +=1
        return self.data[self.inter_index-1]