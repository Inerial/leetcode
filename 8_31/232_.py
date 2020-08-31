class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.output = [] ## 내보낼것들 대기
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output: # output이 비어있다면
            while self.queue: # queue가 빌때까지
                self.output.append(self.queue.pop()) # queue에서 꺼내서 output에 넣기
        return self.output[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.output) + len(self.queue) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()