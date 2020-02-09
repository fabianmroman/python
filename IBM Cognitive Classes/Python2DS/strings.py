mike = 'Michael Jackson'

print (mike[0]) # First character
print (mike[-1]) # Last character
print (len(mike)) # Lenght of string 
print (mike[-len(mike)]) # First character

# Print the string forward
for i in range(len(mike)):
    print (mike[i], end = '') # " end = '' " Prints everything in a single line
print('')

# Print the string backwards
for i in range(1, len(mike)+1): # Range specifying beginning and end
    print (mike[-i], end = '') # "-i" represents the negative values of string index
print('')

print (mike[::2]) # Stride - Zancada, paso largo
print (mike[::3])
print (mike[0:mike.find(' ')]) # Print the first name - Slicing 

# Prints from the first "el", if exists
if mike.find('el') != -1:  
  for i in range(mike.find('el'), len(mike)):
    print (mike[i], end = '') # " end = '' " Prints everything in a single line
print('')

print (mike.upper())

mike = mike + ' ' # Concatenate an space 
mike3 = 3*mike
print (mike3)


G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
H = G.replace("Mary", "Bob")
print (H)