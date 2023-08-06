from collections import deque

class StackUsingQueue:
    def __init__(this):
        this.queue1 = deque()
        this.queue2 = deque()

    def push(this, item):
        # Add the new item to the queue2
        this.queue2.append(item)
        
        # Move all elements from queue1 to queue2
        while this.queue1:
            this.queue2.append(this.queue1.popleft())
        
        # Swap the queues to make queue2 as the main stack
        this.queue1, this.queue2 = this.queue2, this.queue1

    def pop(this):
        if this.queue1:
            return this.queue1.popleft()
        else:
            return None

    def peek(this):
        if this.queue1:
            return this.queue1[0]
        else:
            return None

    def is_empty(this):
        return len(this.queue1) == 0

# Example usage:
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.peek())  # Output: 1
print(stack.is_empty())  # Output: False
