# import statements


# functions

# checks that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        
        # If name is not blank, program continues
        if response != "":
            return response

            # If name is blank, show error (& repeat loop)
        else:
            print(error_message)



# Main Routine

# set up dictionaries / lists needed to hold data

# ask user if they have the program before & show instructions if necessary

# loop to get ticket details

# get name (can't be blank)
    name = not_blank("Name: ",
    "Sorry - this can't be blank, "
    "please enter your name")

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necessary)

    
# Calculate Total sales and profit

# Output data to text file