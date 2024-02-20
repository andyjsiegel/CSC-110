print("hello" + "world")
# helloworld
print("abc"*4)
# abcabcabcabc
print("abc", 4)
# print("abc" + 4) DOES NOT WORK BECAUSE "abc" and 4 are different types; comma concatenation ignores types
print(("A" + "a") * 10)
print("\n~~~~~~~~~~~~~\n")

# prints all on separate lines
print('Are')
print('You')
print('In')
print('College?')
# Prints on same line: 
print('Are', end=" ")
print('You', end=" ")
print('In', end=" ")
print('College?', end="\n")
# many many characters work for the end argument
print("\n~~~~~~~~~~~~~\n")

print('He said, "What is up?"\nJoe\'s friend didn\'t reply.')

print("\n~~~~~~~~~~~~~\n")
# variables
first_name = "Mary"
family_name = "Silva"
# print them:
print(first_name, family_name)

print("\n~~~~~~~~~~~~~\n")

# expressions vs statements
print(3+4) # 3+4 is an expression, print is a statement -- this particular statement has an expression within it as an argument.

print("\n~~~~~~~~~~~~~\n")

string = "hello"
int = 3
float = 3.14
bool = True 

print(type(string)) # class 'str'
print(type(int)) # class 'int'
print(type(float)) # class 'float'
print(type(bool)) # class 'bool'

print("\n~~~~~~~~~~~~~\n")

print(5 + 2)# + addition
print(5 - 2) # - subtraction
print(5 * 2) # * multiplication
print(5 / 2) # / division | RETURNS FLOAT! (2.5)
print(5 // 2) # // floor division | RETURNS INT (2)
print(5 % 2 )# %mModulus operator / Remainder
print(5 ** 2) # ** to the power of; 5^2

print("\n~~~~~~~~~~~~~\n")

x = 5
print(x)
x = x + 2 # adds 2 to x's current value (5); 5+2 = 7
print(x)

print("\n~~~~~~~~~~~~~\n")

# assign a radius value
radius = 3
# compute the area of a circle
area = 3.1415 * radius ** 2

print(area)

# # will mark a comment, then the compiler will ignore the line (all the green text)