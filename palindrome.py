def checkpalindrome(str):

    # cleaning the str
    clean_str=(str.replace(" ","")).lower()

    reverse_str=clean_str[::-1]
    return clean_str==reverse_str



str=input("Enter a string:")
if checkpalindrome(str):
    print("it is palindrome string")
else:
    print("not a palindrome")
        


