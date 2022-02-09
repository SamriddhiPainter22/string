def reverse_string(str):
    str1 =" " 
    #declaring empty string to fill the reversed string

    for i in str:
        str1=i+str1

    return str1

    #it will return the reverse string to thecaller function

str=" The Poetic Vibe Sama"

#given string

print("The original string is : ",str)

print("The reverse string is",reverse_string(str))

#function call
