def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Create closures with different factors
# double will remeber the argument 2 and 3 and then used in when it called.
double = multiplier(2)
triple = multiplier(3)

# Use closures
result1 = double(5)
result2 = triple(4)

print(result1)  # Outputs: 10
print(result2)  # Outputs: 12

if __name__ == "__main__":
    pass