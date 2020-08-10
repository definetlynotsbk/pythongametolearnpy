def negIndex(LIST, index):
    return index - len(LIST)

LIST = [1,2,3,4,5,6,7,8,9,10]
index = 2 
print (index) #2
print (LIST[index]) #3

newIndex = negIndex(LIST, index)
print (newIndex) #-8
print (LIST[newIndex]) #3