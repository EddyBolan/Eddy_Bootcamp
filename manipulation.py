# 10-037 Data Types and Conditional Statements
#  *********** AUTO GRATED TASK 1 **********

# ===== Enter a sentence =================================================
str_manip = input("Enter a sentence: ")
# Example: str_manip = "This is a bunch of words"

# ===== The length of this sentence ======================================
print(f"The length of this sentence is : {len(str_manip)}")

# ===== Replace the last letter in this sentence with "@" ================
print(f"The new sentence is : {str_manip.replace(str_manip[-1], '@')}")

# ===== Print the last three characters in this sentence backwards =======
print(f"The last three characters is : {str_manip[-1:-4:-1]}")

# ===== five-letter word that is made up of the first three characters 
# ===== and the last two characters in this sentence ===
print(f"A five-letter word is : {str_manip[:3] + str_manip[-2:]}")

      



      