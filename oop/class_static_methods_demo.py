class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not depend on class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Can access class-level attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
