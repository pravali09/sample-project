# Simple Calculator Project
# This program takes two numbers and performs basic arithmetic.

def calculator(a, b):
    results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "Cannot divide by zero"
    }
    return results

# MAIN PROGRAM
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

output = calculator(num1, num2)

print("\n--- Results ---")
for operation, value in output.items():
    print(f"{operation}: {value}")

# Also write results to a file
with open("data.txt", "w") as f:
    for operation, value in output.items():
        f.write(f"{operation}: {value}\n")

print("\nResults saved to data.txt")

