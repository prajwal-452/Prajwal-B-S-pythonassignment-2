# Student Information Provided
name = "John Doe"
age = 20
course = "Python Programming"
college = "ABC University"
email = "john@example.com"
width = 36  # Width inside the box
print("╔" + "═" * width + "╗")#repeat the symbol ""=" with size of width
print("║" + "STUDENT BIO CARD".center(width) + "║")
print("╔" + "═" * width + "╗")
print("║" + f"Name    : {name}".ljust(width) + "║")#ljust to automatically adjust the box width length
print("║" + f"Age     : {age} years".ljust(width) + "║")
print("║" + f"Course  : {course}".ljust(width) + "║")
print("║" + f"College : {college}".ljust(width) + "║")
print("║" + f"Email   : {email}".ljust(width) + "║")
print("╚" + "═" * width + "╝")