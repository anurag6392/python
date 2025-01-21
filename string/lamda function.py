starts_with = lambda string, char: string.startswith(char)
string = input("Enter the string: ")
char = input("Enter the character to check: ")
if len(char) != 1:
    print("Please enter exactly one character.")
else:
    result = starts_with(string, char)
    print(f"Does the string start with '{char}'? {result}")