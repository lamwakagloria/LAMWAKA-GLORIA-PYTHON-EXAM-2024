def calculate_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Cannot divide by zero"
    
    return sum_result, difference_result, product_result, quotient_result

num1 = 10
num2 = 5
results = calculate_operations(num1, num2)

print(f"Sum: {results[0]}")
print(f"Difference: {results[1]}")
print(f"Product: {results[2]}")
print(f"Quotient: {results[3]}")
