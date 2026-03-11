#Write a program to find the compound interest  


principal = float(input("Enter principal amount: $"))
rate = float(input("Enter annual interest rate (as %): "))
# Remember: convert % to decimal by dividing by 100
time = float(input("Enter time in years: "))
times_compounded = int(input("Times compounded per year: "))


rate_decimal = rate/ 100

# Apply the formula
amount = principal * (1 + rate_decimal / times_compounded) ** (times_compounded * time)

# For clean currency display
print(f"Final amount: ${amount:.2f}")
print(f"Interest earned: ${amount - principal:.2f}")