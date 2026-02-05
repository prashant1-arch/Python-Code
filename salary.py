# print salary using da ta hra and ta
# Input basic salary
basic = float(input("Enter basic salary: "))

# Allowances
da = basic * 10 / 100
ta = basic * 20 / 100
hra = basic * 15 / 100

# Deduction
pf = basic * 14 / 100

# Total salary
total_salary = basic + da + ta + hra - pf

# Output
print("Basic Salary:", basic)
print("DA (10%):", da)
print("TA (20%):", ta)
print("HRA (15%):", hra)
print("PF (14%):", pf)
print("Total Salary:", total_salary)
