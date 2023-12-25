# Body Mass Calculator 

# The calucultions is done of meteric measures i.e 
# height in meters and weight in kilograms

# Get user input
height = float(input("Enter the height in m : "))
weight = float(input("Enter the weight in kgs : "))

#calculate the bmi 
bmi = round( (weight/(height*height)) , 1)
print("Your BMI is : " + str(bmi))

# Notify the user, what should be the next step
if bmi < 18.5:
    print("Underweight!, need to gain weight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight!!, Perfect")
elif bmi >= 25 and bmi < 30:
    print("Over weight!!, Time to work")
else:
    print("Obesity!!, Health is wealth")
