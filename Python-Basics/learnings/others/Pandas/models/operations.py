import pandas as pd

# Data frames in Pandas
column = ["Vishnu", "Batman", "Heman"]
titled_column = {"name": column,
                 "height": [1.67, 1.9, 0.25], 
                 "weight" : [55, 43, 88]
                }

# creating a data frame
data = pd.DataFrame(titled_column)
print("\nPrint all the elements of dictionary")
print(data)

# Accessing specific column
print("\nSepcific column")
select_column = data["weight"][1]
print(select_column)

# Accessing specific row
print("\nprint specific row")
select_row = data.iloc[1]
print(select_row)

# Accessing specific row of column
print("\nAccessing weight of personn using row")
select_row_weight = data.iloc[1]["weight"]
print(select_row_weight)


# manipulate data frames
bmi = []
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

# adding the dictionary to CSV file
data["bmi"] = bmi
data.to_csv("bmi.csv", index=False)