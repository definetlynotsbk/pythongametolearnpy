#login prompt
print('welcome to login_sys')
def SUorLI(userchoice):
    i = 3
    while i > 0:
        if userchoice == 'login':
            return 'LI'
        elif userchoice == 'signup':
            return 'SU'
        else:
            print('please enter choice again!')
            userchoice = input('do you want to login or signup?(login/signup): ')
            if userchoice == 'login':
                return 'LI'
            elif userchoice == 'signup':
                return 'SU'
            else:
                i -= 1
                if i == 2:
                    print('2 more chances left!')
                elif i == 1:
                    print('1 more chance!')
                else:
                    print('no more chances!')
#passcheckfunc--done but add 3 chances if you want
import base64
def pass_len_check(pass_word):
    if len(pass_word) >= 1:
        return True 
def loginpassscheck(PASSWORD, Exmail):
    i = 3
    while i > 0:
        if pass_len_check(PASSWORD) == True:
            with open('logindetails.txt') as content:
                while True:
                    cr = content.readline()
                    if cr.__contains__(Exmail):
                        a = base64.b64encode(PASSWORD.encode("utf-8"))
                        hashedpass = a.decode("utf-8")
                        if cr.__contains__(hashedpass):
                            return True
                        else:
                            print('wrong pass!')
                            break
        else:
            print('password input not valid!')
            PASSWORD = input('enter password again: ')
            if pass_len_check(PASSWORD) == True:
                with open('logindetails.txt') as content:
                    while True:
                        cr = content.readline()
                        if cr.__contains__(Exmail):
                            a = base64.b64encode(PASSWORD.encode("utf-8"))
                            hashedpass = a.decode("utf-8")
                            if cr.__contains__(hashedpass):
                                return True
                            else:
                                print('wrong pass!')
                                break
            else:
                i -= 1
                if i == 2:
                    print('2 more chances left!')
                elif i == 1:
                    print('1 more chance!')
                else:
                    print('no more chances!')
#mailcheckfunc
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
#new account mail check/write
def add_new_mail(newmail):
    myfile = open('logindetails.txt', 'a+')
    existingmails = myfile.read()
    if existingmails.__contains__(newmail):
        print('this mail already exists!')
    else:
        myfile.seek(0)
        myfile.write('\n')
        myfile.write(newmail)
        myfile.write(' :')
        print('new mail created!')
        return True
#new pass add
def add_pass(newpass):
    myfile = open('logindetails.txt', 'a+')
    existingpass = myfile.read()
    if existingpass.__contains__(newpass.decode("utf-8")):
        print('this pass already exists!')
    else:
        myfile.seek(0)
        myfile.write(' ')
        myfile.write(str(newpass.decode("utf-8")))
        print('pass added!')
        return True
#PROMPT START
print('If you have an account please login, if not signup!')
suorli = SUorLI(input('do you want to login or signup?(login/signup): '))
if suorli == 'LI':
    Exmail = input('enter your mail: ')
    flag, Exmail=loginmailcheck(Exmail)
    if flag == True:
        PASSWORD = input('Enter your password: ')
        if loginpassscheck(PASSWORD, Exmail) == True:
            print('You have logged in!')
elif suorli == 'SU':
    Nmail = input('enter new mail: ')
    if add_new_mail(Nmail) == True:
        nayapass = input('enter new pass: ')
        newpass = base64.b64encode(nayapass.encode("utf-8"))
        if add_pass(newpass) == True:
            print('new account created!')
else:
    print('WIP')