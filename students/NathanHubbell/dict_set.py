#Dictionaries

dictionary = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
print dictionary
dictionary.pop("cake")
print dictionary
dictionary["fruit"]="Mango"
print dictionary.keys()
print dictionary.values()
print "cake" in dictionary
print "Mango" in dictionary
x=range(16)
y=(u"0",u"1",u"2",u"3",u"4",u"5",u"6",u"7",u"8",u"9",u"a",u"b",u"c",u"d",u"e",u"f")
hexDict = dict(zip(x,y))
for keys in hexDict:
    hexDict[keys]=u"a"*keys


#Sets
s = set(range(20))