class Stack:
    s = []
    empty = True

    def push(self, i):
        if self.empty:
            self.empty = False
        self.s = [i] + self.s
    
    def pop(self):
        if self.empty:
            return -1

        if len(self.s) == 1:
            self.empty=True
        return self.s.pop(0)

    def getsize(self):
        return len(self.s)

    def isEmpty(self):
        if self.empty:
            return 1
        return 0

    def top(self):
        if self.empty:
            return -1
        return self.s[0]

if __name__ == "__main__":
    N = int(input())

    answer = ""
    s = Stack()
    for _ in range(0, N):
        cmd = input().split(' ')
        if cmd[0] == 'push':
            s.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            answer = answer + str(s.pop()) + '\n'
        elif cmd[0] == 'size':
            answer = answer + str(s.getsize()) + '\n'
        elif cmd[0] == 'empty':
            answer = answer + str(s.isEmpty()) + '\n'
        elif cmd[0] == 'top':
            answer = answer + str(s.top()) + '\n'
        
    print(answer, end='')
