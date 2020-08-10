def domaincheck(Exmail):
    domains = ['.com','.net','.co','.gov','.org']
    for d in domains:
        if Exmail.__contains__(d):
            return True
def loginmailcheck(Exmail):
    domains = ['.com','.net','.co','.gov','.org']
    if Exmail.__contains__('@'):
        if domaincheck(Exmail) == True:
            with open('logindetails.txt') as content:
                i = 3
                cr = content.read()
                while i > 0:
                    if cr.__contains__(Exmail):
                        return True,Exmail
                    else:
                        print('please enter mail again!')
                        email = input('enter your mail: ')
                        if cr.__contains__(email):
                            return True,email
                        else:
                            i -= 1
                            if i == 2:
                                print('2 more chances left!')
                            elif i == 1:
                                print('1 more chance!')
                            else:
                                print('no more chances!')
        else:
            print('mail not valid')
    else:
        print('mail not valid')

print(loginmailcheck(input()))