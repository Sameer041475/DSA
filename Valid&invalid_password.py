s = input()

if any(char.isdigit() for char in s):
    print("Valid")
else:
    print("Invalid")