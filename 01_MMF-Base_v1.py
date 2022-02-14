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

def int_check(question, low_num, high_num):

    error="Please enter a whole number between {} " \
        "and {}".format(low_num, high_num)

    valid=False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error        
        except ValueError:
                print(error)

# Main Routine

# set up dictionaries / lists needed to hold data

# ask user if they have the program before & show instructions if necessary

# loop to get ticket details

# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats "
        "left".format(MAX_TICKETS - count))

        # warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")  

    # Get details...

    # Get name (can't be blank)
    name = input("Name: ")

    # End the loop if the exit code is entered
    if name == "xxx":
        break

    count += 1

    # Get age (between 12 and 130)
    age = int_check("Age: ", 12, 130)

# End of tickets loop

# Calculate profit etc...
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
    "There are {} places still available"
    .format(count, MAX_TICKETS - count))

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