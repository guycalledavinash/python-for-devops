class OperatorDemo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def arithmetic_operations(self):
        """Performs arithmetic operations and returns results in a dictionary."""
        try:
            results = {
                "addition": self.a + self.b,
                "subtraction": self.a - self.b,
                "multiplication": self.a * self.b,
                "division": self.a / self.b if self.b != 0 else "Undefined (division by zero)",
                "floor_division": self.a // self.b if self.b != 0 else "Undefined (division by zero)",
                "modulus": self.a % self.b if self.b != 0 else "Undefined (division by zero)",
                "exponentiation": self.a ** self.b
            }
            return results
        except Exception as e:
            return {"error": str(e)}

    def assignment_operations(self):
        """Demonstrates assignment operators."""
        x = self.a
        x += self.b
        x -= self.b
        x *= self.b
        if self.b != 0:
            x /= self.b
            x //= self.b
            x %= self.b
        x **= 2
        return x

    def relational_operations(self):
        """Returns relational operator comparisons."""
        return {
            "equal": self.a == self.b,
            "not_equal": self.a != self.b,
            "greater_than": self.a > self.b,
            "less_than": self.a < self.b,
            "greater_than_or_equal": self.a >= self.b,
            "less_than_or_equal": self.a <= self.b
        }

    def logical_operations(self):
        """Returns logical operator results."""
        return {
            "and_operator": (self.a > 0 and self.b > 0),
            "or_operator": (self.a > 0 or self.b > 0),
            "not_operator": not (self.a > self.b)
        }

    def identity_operations(self):
        """Checks if two variables refer to the same object."""
        return {
            "is_operator": self.a is self.b,
            "is_not_operator": self.a is not self.b
        }


if __name__ == "__main__":
    obj = OperatorDemo(10, 5)  # Example inputs
    print("Arithmetic Operations:", obj.arithmetic_operations())
    print("Assignment Operations Result:", obj.assignment_operations())
    print("Relational Operations:", obj.relational_operations())
    print("Logical Operations:", obj.logical_operations())
    print("Identity Operations:", obj.identity_operations())
