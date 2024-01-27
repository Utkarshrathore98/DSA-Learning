# Implementation of Stack using List.

stack = []

def push():
    if len(stack) == n:
        print('Stack is full!')
    else:
        element = input('Enter the element: ')
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print('Stack is empty!')
    else:
        e = stack.pop()
        print('removed element:', e)
        print(stack)

def top_element():
    print(stack[-1])

n = int(input('Enter the limit of stack: '))
while True:
    print('Select the operation 1. push 2. pop 3. check last element 4. quit')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        top_element()
    elif choice == 4:
        break
    else:
        print('Enter the correct option!')



