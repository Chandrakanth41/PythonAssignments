#defining the list
numberList=[]

#iterating through the numberList
for i in range(2000, 3201):
    #checking the condition weather the number from the range is divisible by 7
    # checking the condition that it should not be nultiple of 5
    if (i%7==0) and (i%5!=0):
        #appending to the list after converting to interger type to string 
        numberList.append(str(i))
#joining all the strings in the list by seperating them with "," by using join method
print (','.join(numberList))