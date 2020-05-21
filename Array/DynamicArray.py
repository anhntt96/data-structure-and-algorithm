import ctypes

class DynamicArray(object):
    
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        
        if not 0 <= index < self.size:
            return IndexError("Index out of bounds")
       
        return self.A[index]
    
    def show(self):
        for i in range(self.size):
            print(self.A[i],end=' ')
        
        print()
            
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for i in range(self.size):
            B[i] = self.A[i]
        
        self.A = B
        self.capacity = new_cap
    
    def capacity(self):
        return self.capacity
    
    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object)()
        
    def append(self, ele):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.size] = ele
        self.size += 1
        
    def insert(self, item, index):
        if index < 0 or index > self.size:
            return IndexError("Index out of bounds")
        
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        
        for i in range(self.size, index, -1):
            self.A[i] = self.A[i-1]
        
        self.A[index] = item
        self.size+=1
    
    def removeAt(self, index):
        
        if index<0 or index >= self.size:
            return IndexError("Index out of bounds")
        
        val = self.A[index]
        
        
        for i in range(index, self.size-1):
            self.A[i] = self.A[i+1]
        
        self.A[self.size-1] = None
        self.size -= 1
        return val
    
    def pop(self):
        if self.size == 0:
            print("Array empty")
            return
        
        return self.removeAt(self.size-1)

    
    
    
arr = DynamicArray()
arr.append(1) # 1
arr.append(2) # 1 2

print(len(arr)) 

arr.insert(3,0) # 3 1 2
arr.show()

print(arr.removeAt(2)) 
arr.show() # 3 

print(arr.pop())
arr.show() # 3
    

        