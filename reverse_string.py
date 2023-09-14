# reverse string slice method
string = "1234abcd"

def reverse_string(my_str):

    # Iterate from the last element in the list
    for a_char in my_str[::-1]:
        # The end keyword keeps the print statements on the same line
        print(a_char, end='')

# function call with string passed an arg
reverse_string(string)
