brackets = input()
print("Part 1:", brackets.count('(') - brackets.count(')'))

def find_fault(brackets):
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == ')':
            if not stack:
                return i + 1
            stack.pop()
        else:
            stack.append(brackets[i])
    return i + 1
print("Part 2:", find_fault(brackets))