import unittest

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

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

class TestExpressionEvaluation(unittest.TestCase):

    def test_valid_expression(self):
        expression = "3 + 4 * 2"
        assert evaluate_expression(expression) == 11

    def test_invalid_expression(self):
        expression = "3 + 4 * 2)"
        assert "Error: unexpected EOF while parsing" in evaluate_expression(expression)

    def test_unbalanced_parentheses(self):
        expression = "(3 + 4 * 2"
        assert not has_balanced_parentheses(expression)

if __name__ == '__main__':
    unittest.main()
