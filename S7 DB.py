# Define the actions for each choice we want to offer.
def Add():
    fw = open('DATA.txt','a+')

    rn = input("Enter your Roll No: ")

    fw.write(rn+"_")

    nm = input("Enter your Name: ")
    fw.write(nm+"_")

    mk = input("Enter your Marks : ")
    fw.write(mk)

    fw.write("\n")

    print("Your data is saved to DATA.txt")

    fw.close()

def Search():
    
    file_name = 'DATA.txt'
    sts = input("Enter your Roll No : ") + "_"
    
    line_number = 0
    list_of_results = []
    
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if sts in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))

    matched_lines = list_of_results

    for elem in matched_lines:
        print('Your data : ',elem[1])

def print_file():
    f = open('DATA.txt','r')
    #print(f.readlines())
    print("\n")
    for line in f :
        print(line)
    
    f.close()

print("\nWelcome to the DataBASE. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Insert your DATA !")
    print("[2] Search your DATA.  Sorry ! Only available if have inserted your DATA !")
    print("[3] View Full DataBASE. Sorry ! Only available if have inserted your DATA !")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == '1':
        Add()
    elif choice == '2':
        Search()
    elif choice == '3':
        print_file()
    elif choice == 'q':
        print("\nThanks for Interacting with S7 DataBASE. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        
# Print a message that we are all finished.
print("Thanks again, Suggestions are welcomed !.")