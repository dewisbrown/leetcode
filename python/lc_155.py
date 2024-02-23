"""
155. Min Stack

Design a stack that supports push, pop, top, 
and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""
class MinStack:
    """
    Stack implementation using linked list nodes.
    """
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        """
        Adds number to top of stack.
        """
        if not self.head:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        """
        Removes number from top of stack.
        """
        self.head = self.head.next

    def top(self) -> int:
        """
        Returns value at the top of the stack.
        """
        return self.head.val

    def getMin(self) -> int:
        """
        Returns minimum value in stack.
        """
        return self.head.min


class Node:
    """
    Linked list node that also holds the minimum value of the list.
    """
    def __init__(self, val, min_val, next_node):
        self.val = val
        self.min = min_val
        self.next = next_node


# ["MinStack","push","push","push","getMin","pop","top","getMin"]
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())

# [[],[-2],[0],[-3],[],[],[],[]]