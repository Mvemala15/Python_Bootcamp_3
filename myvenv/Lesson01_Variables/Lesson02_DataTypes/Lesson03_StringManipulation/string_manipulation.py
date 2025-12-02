# STRING CREATION
text1 = 'Hello World'
text2 = "Python Bootcamp"
text3 = """This is a
multi-line
string"""

print(text1)
print(text2)
print(text3)

# STRING INDEXING & SLICING (Page 3)
text = "Python Programming"

print(text[0])      # first character
print(text[-1])     # last character
print(text[0:6])    # slice 0 to 5
print(text[:6])     # start to 5
print(text[7:])     # 7 to end

# STRING METHODS (Page 4)
name = "  Vemala the Tamil Language Teacher  "

print(len(name))         # length
print(name.strip())      # remove whitespace
print(name.upper())      # uppercase
print(name.lower())      # lowercase
print(name.title())      # title case
print(name.replace("bob", "jane"))  # replace text

# STRING FORMATTING (Page 5)
name = "Vemala"
age = 45

msg1 = f"My name is {name} and I am {age} years old."
msg2 = "My name is {} and I am {} years old.".format(name, age)
msg3 = "My name is %s and I am %d years old." % (name, age)

print(msg1)
print(msg2)
print(msg3)
