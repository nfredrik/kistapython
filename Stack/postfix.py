from stack import Stack

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if  token == '' or token == ' ':
            continue
        if  token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()


if __name__ == '__main__':

    print eval_postfix(" 56 47 + 2 *")

    print eval_postfix(" 1 2 + 3 *")
