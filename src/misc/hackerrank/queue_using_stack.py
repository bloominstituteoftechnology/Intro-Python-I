"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

You must use only standard operations of a stack 
-- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. 
You may simulate a stack by using a list or deque (double-ended queue), 
as long as you use only standard operations of a stack.
You may assume that all operations are valid 
(for example, no pop or peek operations will be called on an empty queue).
"""
import collections


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = collections.deque([])

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.storage.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        el = self.storage.popleft()
        return el

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.storage) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)
