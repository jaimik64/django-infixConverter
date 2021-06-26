# Description: Program converts infix to postfix notation

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)


class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''

        for c in expr:
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()
                else:
                    while (not self.stack.isEmpty()) and self.hasLessOrEqualPriority(c, self.stack.peek()):
                        output += self.stack.pop()
                    self.stack.push(c)

        while (not self.stack.isEmpty()):
            output += self.stack.pop()
        return output

    def toPrefix(self, expr):
        reverse_expr = ''
        for c in expr[::-1]:
            if c == '(':
                reverse_expr += ")"
            elif c == ')':
                reverse_expr += "("
            else:
                reverse_expr += c

        reverse_postfix = self.toPostfix(reverse_expr)

        return reverse_postfix[::-1]

    def evaluatePrefix(self, expression):
        """
        Evaluate a given expression in prefix notation.
        Asserts that the given expression is valid.
        """
        # iterate over the string in reverse order
        for c in expression[::-1]:

            # push operand to stack
            if self.isOperand(c):
                self.stack.push(int(c))

            else:
                # pop values from stack can calculate the result
                # push the result onto the stack again
                o1 = self.stack.pop()
                o2 = self.stack.pop()

                if c == '+':
                    self.stack.push(o1 + o2)

                elif c == '-':
                    self.stack.push(o1 - o2)

                elif c == '*':
                    self.stack.push(o1 * o2)

                elif c == '/':
                    self.stack.push(o1 / o2)

        return self.stack.pop()

    def evaluatePostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.stack.push(i)

            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.stack.pop()
                val2 = self.stack.pop()
                self.stack.push(str(eval(val2 + i + val1)))

        return int(self.stack.pop())
