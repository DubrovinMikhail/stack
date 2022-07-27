class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) > 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        removed = self.stack.pop()
        return removed

    def pep(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    brackets = '()[]{}'
    stack_brackets = Stack()
    text = input()
    count = 0
    for bracket in text:
        if bracket in brackets[::2]:
            stack_brackets.push(bracket)
            count += 1

        elif stack_brackets.isEmpty() and bracket == brackets[brackets.index(stack_brackets.pep())+1]:
            stack_brackets.pop()
            count += 1

    if stack_brackets.size() == 0 and count == len(text):
        print("Сбалансированно")
    else:
        print("Несбалансированно")


