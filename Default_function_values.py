# the keyword argument values will only be used regardless of what values parameters have.
def default(x = 1, y = 3 , z = 7):
    print(x,y,z)
    return ((x + y - z) ** 4) / 8
   


print(default(y= 2 , x = 1, z = 1) )  # keyword arguments
