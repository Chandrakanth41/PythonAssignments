subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# using list comprehension
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)