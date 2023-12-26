import math

# calculate future Value
def future_value(present_value, annual_interest_rate, compounding_periods_per_year, years):
    r = annual_interest_rate / compounding_periods_per_year
    n = compounding_periods_per_year * years
    return present_value * (1 + r / compounding_periods_per_year) ** n

# Calculate periodic Payment Loan
def periodic_payment_loan(loan_amount, annual_interest_rate, compounding_periods_per_year, years):
    r = annual_interest_rate / compounding_periods_per_year
    n = compounding_periods_per_year * years
    return loan_amount * (r / (1 - (1 + r / compounding_periods_per_year) ** -n))

# calucate periodic payment annumity
def periodic_payment_annuity(future_value, annual_interest_rate, compounding_periods_per_year, years):
    r = annual_interest_rate / compounding_periods_per_year
    n = compounding_periods_per_year * years
    return future_value * (r / ((1 + r / compounding_periods_per_year) ** n - 1))

# calculate rate of intrest
def interest_rate(present_value, future_value, compounding_periods_per_year, years):
    return compounding_periods_per_year * ((future_value / present_value) ** (1 / (compounding_periods_per_year * years)) - 1)

#calculate number of compouding periods
def number_of_compounding_periods(present_value, future_value, annual_interest_rate, compounding_periods_per_year):
    r = annual_interest_rate / compounding_periods_per_year
    return math.log(future_value / present_value) / (compounding_periods_per_year * math.log(1 + r / compounding_periods_per_year))

# calculating the present value
def present_value(future_value, annual_interest_rate, compounding_periods_per_year, years):
    r = annual_interest_rate / compounding_periods_per_year
    n = compounding_periods_per_year * years
    return future_value / (1 + r / compounding_periods_per_year) ** n

# user input 
pv = float(input("Enter the present value: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
n_per_year = int(input("Enter the number of compounding periods per year: "))
time_years = float(input("Enter the number of years: "))


# call functions and print the answer which were returned by called function
print("Future Value:", future_value(pv, rate, n_per_year, time_years))

loan_amount = float(input("Enter the loan amount: "))
print("Periodic Payment (Loan):", periodic_payment_loan(loan_amount, rate, n_per_year, time_years))

fv_annuity = float(input("Enter the future value of the annuity: "))
print("Periodic Payment (Annuity):", periodic_payment_annuity(fv_annuity, rate, n_per_year, time_years))

print("Interest Rate:", interest_rate(pv, fv_annuity, n_per_year, time_years))

print("Number of Compounding Periods:", number_of_compounding_periods(pv, fv_annuity, rate, n_per_year))

print("Present Value:", present_value(fv_annuity, rate, n_per_year, time_years))
