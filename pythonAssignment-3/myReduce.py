def myReduce(f, *args):
    if len(args) == 0:
        return None
    result = args[0]
    for i in range(1, len(args)):
        result = f(result, args[i])
    return result

# print(my_reduce()) # prints TypeError: my_reduce() takes at least 1 argument (0 given) if not arguments passed to function
print(myReduce(lambda x,y: x+y))             #prints None if length is zero
print(myReduce(lambda x,y: x+y, 3))          #prints 3
print(myReduce(lambda x,y: x+y, -1, 4, -2))  #prints 1

print(myReduce(lambda x,y: x*y, -1, 4, -2))  #prints  8