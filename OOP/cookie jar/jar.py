class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.remains=0

    def __str__(self):
        return self.remains*"🍪"

    def deposit(self, n):
        if self.remains+n<=self.capacity:
            self.remains+=n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.remains-n>=0:
            self.remains-=n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if not capacity or capacity<0:
            raise ValueError
        self._capacity=capacity


    @property
    def size(self):
        return self.remains