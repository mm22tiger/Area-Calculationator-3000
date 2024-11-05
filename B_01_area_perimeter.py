# Auther Matthew M
# Date 12/12/1212
# Ask use for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
        
        try:
            responce = float(input(question))
            
            if responce > 0:
                return responce
            else:
                print(error)
            
        except ValueError:
            print(error)

# Main Routine starts here...

keep_going = ""
while keep_going == "":
    
    # Get width and height
    width = num_check("width: ")
    height = num_check("Height: ")
    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)
    
    #Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask the usrr if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()
    
print("Thank you for useing the area / perimeter calculator")