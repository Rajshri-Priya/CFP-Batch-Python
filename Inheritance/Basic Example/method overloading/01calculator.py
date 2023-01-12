class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a  # work with one argument
        else:
            return a + b  # work with one argument


calculator = Calculator()

print(calculator.add(5))
print(calculator.add(5, 6))


# ---------------------------------------------


class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def add(self, a: str, b: str) -> str:  # concatenation
        return a + b


calculator = Calculator()

print(calculator.add(5, 6))
print(calculator.add("Hello", "World"))


# -------------------------------------------
class Calculator:
    def add(self, *args) -> str:  # *args used for multiple value
        result = 0
        for arg in args:
            result += arg
        return result


calculator = Calculator()

print(calculator.add(5))
print(calculator.add(1, 2))
print(calculator.add(1, 2, 3, 4, 5))
