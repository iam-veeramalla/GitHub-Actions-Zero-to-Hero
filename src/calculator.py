def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Example usage:
expression = input("Enter an expression to evaluate: ")

# Check if the expression has balanced parentheses
def has_balanced_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

if has_balanced_parentheses(expression):
    result = evaluate_expression(expression)
    print("Result:", result)
else:
    print("Error: Unbalanced parentheses in the expression.")
