user_input = input("Enter your word: ").strip().title()
p = []

# Reverse
palindrome = ""
for w in reversed(user_input):
    palindrome += w
    p.append(w)  # Append each character to the list P
if user_input == palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
print("Reversed word:", ''.join(p))
