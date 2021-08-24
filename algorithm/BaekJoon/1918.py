opper = ["+", "-", "*", "/", "(", ")"]

st = input()

stack = []
op = []
for ch in st:
    if not ch in opper:
        stack.append(ch)
    elif ch == "(":
        op.append(ch)
    elif ch == ")":
        while op[-1] != "(":
            stack.append(op.pop())
        op.pop()
    elif ch == "+" or ch == "-":
            while op and op[-1] != "(":
                stack.append(op.pop())
            op.append(ch)
    elif ch == "*" or ch == "/":
        while op and op[-1] != "(" and op[-1] != "+" and op[-1] != "-":
                stack.append(op.pop())
        op.append(ch)

while op :
    stack.append(op.pop())
op.append(ch)

print(''.join(stack))