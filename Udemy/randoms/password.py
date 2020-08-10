def pass_len_check(pass_word):
    if len(pass_word) >= 8:
        return True 
    else:
        print('not long enough')
#1^
def pass_case_check(pass_word):
    if pass_word == pass_word.lower():
        print('not case sensitive')
    else:
        return True
#2^
def pass_num_check(pass_word):
    if pass_word.isalpha():
        print('does not have number/numbers!')
    else:
        return True
#3^
def pass_spec_char_check(pass_word):
    if pass_word.isalnum():
        print ('does not have special character/characters')
    else:
        return True
#4^ 
password_by_user = input("Enter Password: ")
print('checking passsword!')
if pass_len_check(password_by_user) == True:
    print('...')
    if pass_case_check(password_by_user) == True:
        print('...')
        if pass_num_check(password_by_user) == True:
           print('...')
           if pass_spec_char_check(password_by_user) == True:
               print('...')
               print('Strong Password!')