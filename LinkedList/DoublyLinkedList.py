class Node:

    def __init__(self, next=None,prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def valueAt(self, index):

        if index < 0 or index >= self.size:
            return None

        i = 0
        tmp = self.head
        while i < index and tmp:
            i+=1
            tmp = tmp.next
        
        return tmp.data
    
    def pushFront(self, item):
        node = Node(data=item)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
        self.size += 1

    def popFront(self):
        if not self.head:
            return None
        
        val = self.head.data
        self.head = self.head.next
        self.head.prev = None
        
        return val

    def pushBack(self, item):
        node = Node(data=item)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def popBack(self):

        if not self.tail:
            return None
        
        val = self.tail.data

        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def front(self):
        if not self.head:
            return None
        
        return self.head.data

    def back(self):
        if not self.tail:
            return None
        
        return self.tail.data
    
    def insert(self, value, index):

        if index < 0 or index > self.size:
            return IndexError("Index out of bounds")

        if index == 0:
            self.pushFront(value)
        elif index == self.size:
            self.pushBack(value)
        else:
            i = 0
            prev = None
            tmp = self.head
            while i< index and tmp:
                i+=1
                prev = tmp
                tmp = tmp.next

            node = Node(tmp,prev,value)
            prev.next = node
            tmp.pre = node
            self.size+=1

    def removeAt(self,index):
        if index < 0 or index >= self.size:
            return IndexError("Index out of bounds")

        if index == 0:
            return self.popFront()
        elif index == self.size-1:
            return self.popBack()
        
        i = 0
        prev = None
        tmp = self.head

        while tmp and i < index:
            i+=1
            prev = tmp
            tmp = tmp.next
        
        prev.next = tmp.next
        tmp.next.prev = prev

        return tmp.data

    def show(self):

        tmp = self.head
        while tmp:
            print(tmp.data,end=' ')
            tmp = tmp.next
        print()

linked_list = DoublyLinkedList()

linked_list.insert(0,0)
linked_list.insert(1,1)
linked_list.insert(2,2)

linked_list.show()

print(linked_list.valueAt(1))

linked_list.pushFront(-1)
linked_list.show()
print(linked_list.front())
print(linked_list.popFront())

linked_list.pushBack(3)
linked_list.show()
print(linked_list.back())
print(linked_list.popBack())

print(linked_list.removeAt(1))
linked_list.show()




