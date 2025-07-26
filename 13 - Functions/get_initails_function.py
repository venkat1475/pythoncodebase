# Create function getfuntionname to accept a name and 
# return the first letter of the name in uppercase


# Parameters:
#   name: the name of a person
# Return value:
#   first letter of name passed in as a parameter in uppercase 



def get_initial(name):
    initial = name[0:1].upper()
   
    return initial

# This program will ask for someone's name and return the initials
first_name = input('Enter your first name: ')
# Call get_initial to retrieve initial of name
first_name_initial = get_initial(first_name)


print(f"Your first name initial is: {first_name_initial}")