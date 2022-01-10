# filter function used to filter the even numbers
def myFilter(is_even,list_2):
    return is_even()


def is_even():
    list_3=[]
    for i in list_2:
        if i%2==0:
            list_3.append(i)
    print(list_3)

list_2=[2,3,4,5,6,7,8,9,10]
myFilter(is_even,list_2)