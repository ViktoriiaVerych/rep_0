# first stage
salary = int(input('Enter your salary: '))
percentage_invest = float(input('Enter invest percentage: '))
property_value = int(input('Enter property value: '))
first_invest_percentage = float(input('Enter needed percentage of first invest: '))
year_invest_percentage = float(input("Enter year invest percentage: "))
balance = 0
month = 0
year = 0

monthly_invest_percentage = year_invest_percentage / 12
while balance < first_invest_percentage * property_value :
    balance += salary * percentage_invest + (balance * monthly_invest_percentage)
    month += 1
    if month == 12 :
        year += 1
        month = 0

print('years: ' + str(year) + "month: " + str(month))

# second stage

user_answer1 = input('Do you want to count credit body? ')
if  user_answer1 == 'No' :
    print('Ok.')
elif user_answer1 == 'Yes' :
    credit_years = int(input('Number of years of lending: '))
    annual_percentage = float(input('Number of annual percentage: '))
    credit_body_total = property_value * credit_years * annual_percentage
    credit_body_wo_inc = float(credit_body_total + property_value - (first_invest_percentage * property_value))
    credit_body_wo_inc_monthly = credit_body_wo_inc // (12 * credit_years)
    if credit_body_wo_inc_monthly > salary :
        print('It is impossible to take a loan')
    else :
        print(credit_body_wo_inc_monthly)
else:
    print('Entered wrong answer')
