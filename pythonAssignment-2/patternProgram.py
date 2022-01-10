n = 5 
 
# upperTriangle pattern
for i in range(0, n):  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
        print()  
# lowerTriangle pattern
for i in range(n, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  