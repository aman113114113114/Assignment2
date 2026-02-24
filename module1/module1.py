student_name = "John Doe"
student_age = 20
student_course = "Python Programming"
student_college = "ABC University"
student_email = "john@example.com"

# Creating the top and bottom borders
border = "╔" + "═" * 32 + "╗"
bottom_border = "╚" + "═" * 32 + "╝"

# Printing the formatted bio card
print(border)

# Centering the title
print("║{:^32}║".format("STUDENT BIO CARD"))

# Printing a separator line below the title
print("╠" + "═" * 32 + "╣")

# Printing each piece of information
# The <32 ensures everything is aligned properly to the left
print("║{:<32}║".format(f"Name : {student_name}"))
print("║{:<32}║".format(f"Age : {student_age} years"))
print("║{:<32}║".format(f"Course : {student_course}"))
print("║{:<32}║".format(f"College : {student_college}"))
print("║{:<32}║".format(f"Email : {student_email}"))

# Printing the bottom border of the card
print(bottom_border)
