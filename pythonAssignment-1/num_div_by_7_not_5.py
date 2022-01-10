a_list = []
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        a_list.append(i)
converted_list = [str(element) for element in a_list]
joined_string = ",".join(converted_list)
print(joined_string)
