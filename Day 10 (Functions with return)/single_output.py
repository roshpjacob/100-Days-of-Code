def format_name(fname, lname):
    fst = fname.title()
    lst = lname.title()
    return fst + " " + lst


first = input("Enter your First Name: ")
last = input("Enter your Last Name: ")
fname = format_name(first, last)

print("\nYour Full Name is: ", fname)
