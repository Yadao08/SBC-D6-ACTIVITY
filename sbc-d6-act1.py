p = []
user_input = input("Enter the word: ")
palindrome = "".join(reversed(user_input.replace(" ","").upper()))

rep = user_input.replace(" ","").upper()
p.append(rep)

for i in p:
    if i == palindrome:
       print( user_input, "Is a Palindrome" )
    else:
       print( user_input,"Is not a palindrome",)
print("Reversed word:", '',palindrome)
