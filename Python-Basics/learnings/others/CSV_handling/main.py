# CSV Files - Comma-Seperated Values
import models.functions as fun

if __name__ == "__main__":
    fun.read_csv("data.csv")
    fun.read_dict_csv('employee_records.csv')
    fun.write_data_to_csv('university_records.csv')
    fun.read_csv('university_records.csv')
    fun.write_dictionary('university_records.csv')
    fun.read_csv('university_records.csv')
