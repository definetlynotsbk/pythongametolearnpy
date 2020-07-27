password = input('enter password: ')
#len check
def lenchecker(PASS):
    if len(PASS) >= 8:
        return True
    else:
        print ("password not long enough!")
#numcheck
def numcheck(PASS):
    if PASS.isalpha() == True:
        print ("password does not contain number(s)!")
    else:
        return True
#capitalcheck
def capitalcheck(PASS):
    if PASS.islower() == True:
        print ("password does not have an uppercase alpha!")
    else:
        return True
#spccharcheck
def spccharcheck(PASS):
    if PASS.isalnum() == True:
        return True
    else:
        print ("password does not contain special char")

#starting exec
if lenchecker(password) == True:
    if numcheck(password) == True:
        if capitalcheck(password) == True:
            if spccharcheck(password) == True:
                print("you have a strong pass!")