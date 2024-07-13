class Calculator:
    def __init__(self, ):
        pass

    def addition(self,a, b):
        return a + b

    def subtraction(self,a, b):
        return a - b

    def division(self,a, b):
        if b == 0:
            return "Division by zero is not allowed."
        return a / b
    def multiplication(self,a, b):
        return a * b

    def handle_user_input(self):
        while True:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            print("\nSelect operation:")
            print("1. addition")
            print("2. subtraction")
            print("3. division")
            print("4. multiplication")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '1':
                print(f"{a} + {b} = {self.addition(a, b)}")
            elif choice == '2':
                print(f"{a} - {b} = {self.subtraction(a,b)}")
            elif choice == '3':
                print(f"{a} / {b} = {self.division(a,b)}")
            elif choice == '4':
                print(f"{a} x {b} = {self.multiplication(a,b)}")
            elif choice == '5':
                print("Exiting the calculator.")
                break
            else:
                print("Invalid choice. Please try again.")

# Creating an instance of the SimpleCalculator class
calc = Calculator()

# Using the handle_user_input method to dynamically call the functions based on user input
calc.handle_user_input()