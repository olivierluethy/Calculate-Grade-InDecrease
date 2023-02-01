def calculate_grade_increase(original_grade, new_grade):
    # Calculate the increase in grade
    increase = new_grade - original_grade
    # Calculate the percentage increase
    percentage_increase = (increase / original_grade) * 100
    return percentage_increase

# Prompt the user for the original grade
original_grade = float(input("Enter the original grade: "))
# Prompt the user for the new grade
new_grade = float(input("Enter the new grade: "))

# Call the function to calculate the percentage increase
percentage_increase = calculate_grade_increase(original_grade, new_grade)
# Print the result
print("The grade was increased by {:.2f}%".format(percentage_increase))