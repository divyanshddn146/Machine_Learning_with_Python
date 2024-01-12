user_hourly_wage = int(input("Enter hourly wage:"))
user_regular_hour = float(input("Enter regualar hours you worked:"))
user_overtime_hour = float(input("Enter overtime hours you worked:"))

print(f"Your total weekly pay is {user_overtime_hour*user_hourly_wage+user_regular_hour*user_hourly_wage}")
