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

    if not any(pswdInput.islower() for x in pswdInput):
        return 1
    if not any(pswdInput.isupper() for x in pswdInput):
        return 2
    if not any(pswdInput.isnumeric() for x in pswdInput):
        return 3
    if len(pswdInput) >= 8:
        return 4

def main():
    print(check_pswd(get_pswd()))

main()

#mindst 8 tegn
#mindst 1 lille bogstav
#mindst 1 stor bogstav
#mindst 1 tal