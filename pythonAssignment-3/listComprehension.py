list = ['x','y','z']
result = [ item*num for item in list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in list  ]
print("['x','y','z'] => " +   str(result))



list = [2,3,4]
result = [ [item+num] for item in list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


list = [2,3,4,5]
result = [ [item+num for item in list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


list=[1,2,3]
result = [ (b,a) for a in list for b in list]
print("[1,2,3] =>" +  str(result))