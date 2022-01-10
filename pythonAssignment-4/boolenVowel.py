
def is_vowel(ch):
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
        return True
    else:
        return False

if __name__ == "__main__":
    ch = input("ENTER A CHARACTER: ")
    print (is_vowel(ch))