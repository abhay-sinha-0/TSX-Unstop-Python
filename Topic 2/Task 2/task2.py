# 1. Script to Calculate Area and Perimeter of a Rectangle
length=10
width=5
# Calculating area and perimeter
area=length *width
perimeter=2* (length + width)

# Displaying the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)


# 2. Script to Compare Two Numbers
num1= float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparing the numbers
if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The first number is less than the second.")
else:
    print("Both numbers are equal.")


# 3. Script to Check Leap Year
year=int(input("Enter a year: "))

# Checking leap year conditions
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 4. Experiment with Arithmetic and Logical Operators (In Interpreter)
>>> 5+3          # Addition
8
>>> 10-4         # Subtraction
6
>>> 6*7          # Multiplication
42
>>> 20/5         # Division
4.0
>>> 10%3         # Modulus (remainder)
1
>>> 2**3         # Exponentiation
8

>>> x=5
>>> y=10
>>> x>3 and y<15   # Logical AND
True
>>> x<3 or y==10   # Logical OR
True
>>> not(x==5)        # Logical NOT
False


# 5. Script to Concatenate Two Strings
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
full_name= first_name +" "+ last_name
print("Your full name is:",full_name)