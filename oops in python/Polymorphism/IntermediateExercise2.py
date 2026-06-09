# Base class: MathUtility
class MathUtility:
    # Runtime polymorphism: virtual method to override
    def advanced_operation(self, data):
        print("Performing a generic advanced math operation on:", data)

    # Compile-time polymorphism simulation using *args
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) > 2:
            result = 0
            for num in args:
                result += num
            return result
        else:
            print("Unsupported number of arguments")

    def subtract(self, a, b):
        return a - b


# Derived class: CalculusUtility
class CalculusUtility(MathUtility):
    # Override advanced_operation for runtime polymorphism
    def advanced_operation(self, func):
        print(f"Integrating function: {func}")
        # Simulate integration
        print("Integration result: ∫", func, "dx")


# Derived class: DifferentiationUtility
class DifferentiationUtility(MathUtility):
    def advanced_operation(self, func):
        print(f"Differentiating function: {func}")
        # Simulate differentiation
        print("Derivative result: d/dx", func)


# Example usage
if __name__ == "__main__":
    # Compile-time polymorphism: add different number of arguments
    math_util = MathUtility()
    print("Add 2 numbers:", math_util.add(5, 10))
    print("Add 4 numbers:", math_util.add(1, 2, 3, 4))

    # Runtime polymorphism: advanced operations
    calculus_util = CalculusUtility()
    diff_util = DifferentiationUtility()

    instruments = [calculus_util, diff_util]

    for tool in instruments:
        tool.advanced_operation("x^2 + 3x + 2")
