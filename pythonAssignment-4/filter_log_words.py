class List:
 def __init__(self, wordlist):
  self.wordlist = wordlist

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

instance = List(["This","is","a","beautiful","day"])
print ("New List of Words  => " + str(instance.filter_long_words(3)) ) 