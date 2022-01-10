def div_by_zero():
 return 5/0

if __name__ == "__main__":
    try:
     div_by_zero()
    except ZeroDivisionError as e:
     print("'div by 0'error:", e)