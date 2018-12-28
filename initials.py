from cs50 import get_string
s = get_string("name: ")
initials = ""
#for each character in the string s, if the character is uppercase, append it to the string initials and print it
for c in s:
    if c.isupper():
        initials += c
print(initials)