import csv

# Read CSV files
def read_csv(filename):
    try:
        fields = []
        rows = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # for row in csv_reader:
            #     print(row)

            # field names of first row
            fields = next(csv_reader)
            print("Field names of 1st row: ", fields)

            # or
            print("Field names are: " + ', '.join(field for field in fields))

            # number of rows in file
            print("Total no.of rows: ", csv_reader.line_num)

            # extracting rows of CSV file
            for row in csv_reader:
                rows.append(row)

            print('\nFirst 5 rows are:\n')
            for row in rows[:5]:
                # parsing each column of a row
                for col in row:
                    print("%10s" % col, end=" ")
                print('\n')
    except (IOError, csv.Error) as e:
        print(f"Error reading {filename}: {e}")

# Reading CSV files into a Dictionary with CSV
# headers - keys
# values - rest rows
        
def read_dict_csv(filename):
    try:
        with open (filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            data_list = []
            for row in csv_reader:
                data_list.append(row)

            for data in data_list:
                print(data)
    except (IOError, csv.Error) as e:
        print(f"Error reading {filename}: {e}")

def write_data_to_csv(filename):
    fields = ['Name', 'Branch', 'year', 'CGPA']
    rows = [['Nikhil', 'COE', '2', 9.0],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            # write fields
            csv_writer.writerow(fields)
            # write rows
            csv_writer.writerows(rows)
    except:
        print("could not write into file")

# Writing a dictionary to a CSV file
def write_dictionary(filename):
    mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]
    fields = ['name', 'branch', 'year', 'cgpa']

    with open(filename, 'w') as csv_file:
        # creating a csv dict writer object
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(mydict)

#Reading CSV Files With Pandas
def read_csv_with_pandas(filename):
    

if __name__ == "__main__":
    # read_csv("data.csv")
    # read_dict_csv('employee_records.csv')
    # write_data_to_csv('university_records.csv')
    # read_csv('university_records.csv')
    # write_dictionary('university_records.csv')
    # read_csv('university_records.csv')