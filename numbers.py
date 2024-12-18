# 10-037 Data Types and Conditional Statements
# *********** AUTO GRATED TASK 2 **********

# ===== Enter three different integers ===========================
three_integers = [int(input(f"Enter integer {i+1}: ")) for i in range(3)]
print(f"The three different integers are : {three_integers}")

# ==== The sum of all the numbers ================================
print(f"The sum of all the numbers is: {sum(three_integers)}")

# ==== The first number minus the second number ==================
difference = three_integers[0]-three_integers[1]
print(f"The first number minus the second number is: {difference}")

# ==== The third number multiplied by the first number ===========
product = three_integers[2] * three_integers[0]
print(f"The third number multiplied by the first number is: {product}")

# ==== The sum of all three numbers divided by the third number ==
if three_integers[2]!=0:        # test if the third number is different to 0
    quotient = sum(three_integers) / three_integers[2]
    print(f"The sum of all three numbers divided by the third number is: {quotient}")
else:                           # if the third number is 0, Error
    print("The sum of all three numbers cannot be divided by the third number (= 0)")




