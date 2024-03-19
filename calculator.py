class Calculator:
    def __init__(self):
        self.res = None

    def add(self, a, b):
        self.res = a + b
        return self.res

    def sub(self, a, b):
        self.res = a - b
        return self.res

    def mul(self, a, b):
        self.res = a * b
        return self.res

    def div(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            self.res = a / b
            return self.res

def main():
    calc = Calculator()

    print("Welcome to Calculator!")

    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.sub(num1, num2))
        elif choice == '3':
            print("Result:", calc.mul(num1, num2))
        elif choice == '4':
            print("Result:", calc.div(num1, num2))
    else:
        print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
