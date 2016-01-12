myintegerlist = []
myintegerlist.append(1)
myintegerlist.append(2)
myintegerlist.append(3)
myintegerlist.append(4)
myintegerlist.append(1)
myintegerlist[4] = 123


print(myintegerlist[0])
print(myintegerlist[1])
print(myintegerlist[2])

for a in myintegerlist:
    print a
a = len(myintegerlist)
print a

mystringlist = []
mystringlist.append("mah")
mystringlist.append("mahesh")
mystringlist.append("mah")

print(mystringlist[0])
print(mystringlist[1])
print(mystringlist[2])

for b in mystringlist:
    print b

#c = mystringlist.count(mystringlist)
#print c

