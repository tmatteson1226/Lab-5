myList = [1,2,3,4,5,6,7,8,9,10]
for thing in myList:
    print myList

for item in range(11,21,1):
    print item
    
for item in range(99,0,-2):
    print item
    
myList = []
for item in range(0,5,1):
    userinput = raw_input()
    myList.append(userinput)
    
for item in myList:
    print item