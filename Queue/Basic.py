class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty")
    def size(self):
        return len(self.items)
queue = Queue()
print("Is queue empty: ",queue.is_empty())
queue.enqueue(1)  
print("Is queue empty: ",queue.is_empty())
queue.enqueue(2)
queue.enqueue(3)
print("Item dequeuing from th queue is: ",queue.dequeue())
queue.enqueue(4)
queue.enqueue(5)
print("Items of the queue is: ",queue.items)
print("Size of the queue is: ",queue.size())