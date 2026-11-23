p = float(input("Enter principal amount (Rs.): "))
r = float(input("Enter rate of interest (%): "))
t = float(input("Enter time in years: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", round(ci,3))
print("Total Amount =", round(amount,2))

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100: print("Invalid marks")
elif marks >= 90: print("Grade: A+")
elif marks >= 80: print("Grade: A")
elif marks >= 70: print("Grade: B")
elif marks >= 60: print("Grade: C")
elif marks >= 40: print("Grade: D")
else: print("Fail")