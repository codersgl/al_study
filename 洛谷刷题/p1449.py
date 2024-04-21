"""
A suffix expression, also known as Reverse Polish Notation (RPN),
is a representation of a mathematical expression.
In a suffix expression, the operator is placed after the operand,
rather than between the operands in traditional prefix or infix notation.
This representation eliminates the need for parentheses because
the order of operations is entirely determined by the order of the operators.
"""


# sequential stack
class Stack:
    def __init__(self):
        self.elem = []  # 初始化栈为一个空列表
        # the sequential stack
        self.top, self.base = 0, 0
        # top and base all points to the position of
        # the bottom element of the stack in the order stack, empty stack
        self.stack_size = 0  # set the stack_size to the 0

    def push(self, e):
        # 将元素压入栈，栈顶指针加一
        self.elem.append(e)
        self.top += 1

    def pop(self):
        # 将栈顶元素弹出
        if self.top == self.base:
            raise Exception("栈已空")
        self.top -= 1
        return self.elem.pop()

    def get_top(self):
        # 返回栈顶元素
        if self.top == self.base:
            raise Exception("栈已空")
        else:
            return self.elem[self.top]

    def stack_empty(self):
        return self.top == self.base

    def __len__(self):
        return self.top - self.base


# input
expression = input()

# 建立运算符列表
lis1 = ['+', '-', '*', '/']
# 建立操作符列表
lis2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 实例化一个栈
stack = Stack()
s = ''
for e in expression:
    if e in lis2:
        s += e
    elif e == '.':
        stack.push(s)
        s = ''
    elif e in lis1:
        a = stack.pop()
        b = stack.pop()
        if e == '+':
            c = int(b) + int(a)
            stack.push(str(c))
        elif e == '-':
            c = int(b) - int(a)
            stack.push(str(c))
        elif e == '*':
            c = int(b) * int(a)
            stack.push(str(c))
        else:
            c = int(b) // int(a)
            stack.push(str(c))
    elif e == "@":
        break
# output
print(stack.pop())
