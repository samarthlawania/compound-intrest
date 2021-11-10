P = int(input("Enter the principal amount"))
r = int(input("Enter the rate applied"))
n = float(input("Enter the number of times intrest applied per time period"))
t = float(input("Enter the number of time period elapse"))
A = P * (1 +(r/n)) ** n * t
C = A - P
print(f"The amount of compound intrest is {C}")
