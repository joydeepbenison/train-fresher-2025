def changecase(func):
  def myinner(): # Inner function that actually modifies the result
    return func().upper()  # Call the original function and convert its result to uppercase
  return myinner # Return the modified function
# Apply the decorator to myfunction 
@changecase
def myfunction():
  return "Hello "
#Apply the decorator to another function
@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())
