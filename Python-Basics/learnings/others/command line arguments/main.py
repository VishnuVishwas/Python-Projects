import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

# Arguments passed 
print("Name of the python script: ", sys.argv[0])

print("Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers 
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])

print("The sum will be: ", sum)

# output 
# py main.py 1 2 344 544 23
# Total arguments passed:  6
# Name of the python script:  main.py
# Arguments passed: 1 2 344 544 23 The sum will be:  914