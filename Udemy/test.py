def spccharcheck(PASS):
    if PASS.isalnum() == True:
        return True
    else:
        print ("password does not contain special char")

password = input("Enterpass: ")
if spccharcheck == True:
    print('has specail char')
else:
    print('noob')