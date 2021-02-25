#Write a function that determines whether or not a password is good. We 
# will define a good password to be a one that is at least 8 characters 
# long and contains at least one uppercase letter, at least one lowercase
#  letter, and at least one number. Your function should return true if the
#password passed to it as its only parameter is good. Otherwise it should 
# return false. Include a main program that reads a password from the user
#  and reports whether or not it is good.

def get_pswd():
    while True:
        pswdInput = input("Enter a password: ")
        return pswdInput

def check_pswd(pswdInput):

    if not (pswdInput.islower() for x in pswdInput):
        return False
    elif not (pswdInput.isupper() for x in pswdInput):
        return False
    elif not (pswdInput.isnumeric() for x in pswdInput):
        return False
    elif not len(pswdInput) >= 8:
        return False
    else:
        return True

def main():
    print(check_pswd(get_pswd()))

main()