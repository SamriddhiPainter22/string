from itertools import count


str="The Poetic Vibe Sama"

print("The original String : ")

reverse_string =""
count=len(str)

while count>0:
    reverse_string+=str[count-1]

    count=count-1
print("The reverse string using a while loop is: ",reverse_string)