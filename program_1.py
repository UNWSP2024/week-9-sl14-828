# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    try:
        # Open the file in read mode
        with open('names.txt', 'r') as file:
            # Read all lines and count them
            namesList = file.readlines()
            numberOfNames = len(namesList)
        
        # Display the count of names
        print(f'The number of names in the file is: {numberOfNames}')
    except FileNotFoundError:
        print("The file 'names.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
